import json
import requests
import toml
from src import config
from src import prompt
cfg = config.load_project_config()
# credentials = toml.load("credentials.toml")

def main():
    topic = "bees"

    print("--- Initial prompt ---")
    print(f"All:  '{cfg.initial_prompts.all}'")

    print("--- Discussion prompt templates ---")
    print(f"Decide:  '{cfg.discussion_prompts.decide}'")
    print(f"Propose: '{cfg.discussion_prompts.propose}'")
    print(f"Query:   '{cfg.discussion_prompts.query}'")
    print(f"Respond: '{cfg.discussion_prompts.respond}'")

    print("--- Prompt demo ---")
    decide_demo = prompt.apply_to_template(cfg.discussion_prompts.decide, {
        "history": "I'm history",
        "page": "A long long time ago...",
    })
    print(f"Decide:  '{decide_demo}'")
   

if __name__ == '__main__':
    main()