import json
import requests
import toml
config = toml.load("project_config.toml")
credentials = toml.load("credentials.toml")

def main():
    topic = "bees"
    # Execute the prompt
    r = requests.post(f"https://app.wordware.ai/api/prompt/{config['wordware']['dummy_prompt']}/run",
                      json={
                          "inputs": {
                              "topic": topic
                          }
                      },
                      headers={"Authorization": f"Bearer {credentials['wordware']['api_key']}"},
                      stream=True
                      )

    # Ensure the request was successful
    if r.status_code != 200:
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
                    print("RESULT:",json.dumps(value["values"]["result"]))


if __name__ == '__main__':
    main()