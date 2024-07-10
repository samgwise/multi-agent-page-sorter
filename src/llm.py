#
# Defines an interface for an llm for use in a consortium of agents.
#

import json

import requests

from config import ProjectConfigWordWare, CredentialsWordWare

class LLM:

    def __init__(self, credentials: CredentialsWordWare, project_config: ProjectConfigWordWare):
        self.credentials = credentials
        self.configuration = project_config

    # Internal request method
    def _llm_request(self, prompt_id, json_body: dict):
        # topic = "bees"
        # Execute the prompt
        r = requests.post(f"https://app.wordware.ai/api/prompt/{prompt_id}/run",
                        json=json_body,
                        headers={"Authorization": f"Bearer {self.credentials.api_key}"},
                        stream=True
                        )

        # Ensure the request was successful
        if r.status_code != 200:
            # TODO: Update once logging is adopted
            print("Request failed with status code", r.status_code)
            print(json.dumps(r.json(), indent=4))
        else:
            for line in r.iter_lines():
                if line:
                    content = json.loads(line.decode('utf-8'))
                    value = content['value']
                    # We can print values as they're generated
                    #if value['type'] == 'generation':
                    #    if value['state'] == "start":
                    #        print("\nNEW GENERATION -", value['label'])
                    #    else:
                    #        print("\nEND GENERATION -", value['label'])
                    #elif value['type'] == "chunk":
                    #    print(value['value'], end="")
                    if value['type'] == "outputs":
                        # Or we can read from the outputs at the end
                        # Currently we include everything by ID and by label - this will likely change in future in a breaking
                        # change but with ample warning
                        #print("\nFINAL OUTPUTS:")
                        #print(json.dumps(value, indent=4))
                        return json.dumps(value["values"]["result"])

    def dummy_request(self, topic = "bees"):
        return self._request(
            self.configuration.dummy_prompt,
            {
                "inputs": {
                    "topic": topic
                }
            }
        )