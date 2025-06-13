#
# Code for defining and managing configuration and credentials used in the consortium
#
import tomllib
from dataclasses import dataclass


## Generic config loader
def load_config(path: str):
    with open(path, "rb") as conf:
        return tomllib.load(conf)


## Project config loader
@dataclass
class DiscussionPromptsConfig:
    decide: str
    propose: str
    query: str
    respond: str

@dataclass
class initialPromptsConfig:
    all: str

@dataclass
class ProjectConfig:
    discussion_prompts: DiscussionPromptsConfig
    initial_prompts: initialPromptsConfig

    def __post_init__(self):
        self.discussion_prompts = DiscussionPromptsConfig(**self.discussion_prompts)
        self.initial_prompts = initialPromptsConfig(**self.initial_prompts)


def load_project_config():
    return ProjectConfig(**load_config("default_prompts.toml"))


## credentials loader
@dataclass
class CredentialsConfig:
    api_key: str


@dataclass
class Credentials:
    llm: CredentialsConfig

    def __post_init__(self):
        self.llm = CredentialsConfig(**self.llm)


def load_credentials_config():
    return Credentials(**load_config("credentials.toml"))
