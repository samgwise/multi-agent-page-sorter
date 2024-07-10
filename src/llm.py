#
# Defines an interface for an llm for use in a consortium of agents.
#
import requests, json
from config import ProjectConfigWordWare, CredentialsWordWare

class LLM:

    def __init__(self, credentials, project_config):
        self.credentials = credentials
        self.configuration = project_config

    def _call_wordware(self, prompt, inputs, output="result"):
        r = requests.post(f"https://app.wordware.ai/api/prompt/{self.configuration['wordware'][prompt]}/run",
                        json={
                            "inputs": inputs
                        },
                        headers={"Authorization": f"Bearer {self.credentials['wordware']['api_key']}"},
                        stream=False
                        )
        if r.status_code != 200:
            print("Request failed with status code", r.status_code)
            print(json.dumps(r.json(), indent=4))
        else:
            for chunk in r.iter_lines():
                if chunk:
                    content = json.loads(chunk.decode('utf-8'))['value']
                    if content["type"] == "outputs":
                        return content["values"][output]

#Testing stuff
import toml
if __name__ == '__main__':
    llm = LLM(toml.load("credentials.toml"),toml.load("project_config.toml"))
    print(llm._call_wordware("dummy_prompt", {"topic":"bees"}))
