#
# Defines an interface for an llm for use in a consortium of agents.
#

import json

import requests

from config import PromptsConfig, CredentialsConfig


class LLM:
    def __init__(
        self, credentials: CredentialsConfig, project_config: PromptsConfig
    ):
        self.credentials = credentials
        self.configuration = project_config

    # Internal request method
    def _llm_request(self, prompt_id: str, json_body: dict):
        # topic = "bees"
        # Execute the prompt
        r = requests.post(
            f"https://app.wordware.ai/api/prompt/{prompt_id}/run",
            json=json_body,
            headers={"Authorization": f"Bearer {self.credentials.api_key}"},
            stream=True,
        )

        # Ensure the request was successful
        if r.status_code != 200:
            # TODO: Update once logging is adopted
            print("Request failed with status code", r.status_code)
            print(json.dumps(r.json(), indent=4))
        else:
            for line in r.iter_lines():
                if line:
                    content = json.loads(line.decode("utf-8"))
                    value = content["value"]
                    # We can print values as they're generated
                    # if value['type'] == 'generation':
                    #    if value['state'] == "start":
                    #        print("\nNEW GENERATION -", value['label'])
                    #    else:
                    #        print("\nEND GENERATION -", value['label'])
                    # elif value['type'] == "chunk":
                    #    print(value['value'], end="")
                    if value["type"] == "outputs":
                        # Or we can read from the outputs at the end
                        # Currently we include everything by ID and by label - this will likely change in future in a breaking
                        # change but with ample warning
                        # print("\nFINAL OUTPUTS:")
                        # print(json.dumps(value, indent=4))
                        return json.dumps(value["values"]["result"])

    def dummy_prompt(self, topic="bees"):
        return self._llm_request(
            self.configuration.dummy_prompt, {"inputs": {"topic": topic}}
        )

    # Stubs for primary prompts

    def decide_prompt(self, agent_id: int, history: str, page: str):
        return self._llm_request(
            self.configuration.decide_prompt,
            {
                "inputs": {
                    "agent_id": agent_id,
                    "history": history,
                    "page": page,
                }
            },
        )

    def propose_prompt(self, agent_id: int, history: str, page: str):
        return self._llm_request(
            self.configuration.propose_prompt,
            {
                "inputs": {
                    "agent_id": agent_id,
                    "history": history,
                    "page": page,
                }
            },
        )

    def query_prompt(self, agent_id: int, history: str, page: str):
        return self._llm_request(
            self.configuration.query_prompt,
            {
                "inputs": {
                    "agent_id": agent_id,
                    "history": history,
                    "page": page,
                }
            },
        )

    def respond_prompt(self, agent_id: int, history: str, page: str, query: str):
        return self._llm_request(
            self.configuration.respond_prompt,
            {
                "inputs": {
                    "agent_id": agent_id,
                    "history": history,
                    "page": page,
                    "query": query,
                }
            },
        )
