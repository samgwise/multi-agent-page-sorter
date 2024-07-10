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
class ProjectConfigWordWare:
    # Delete this once stub is integrated
    dummy_prompt: str
    decide_prompt: str
    propose_prompt: str
    query_prompt: str
    respond_prompt: str


@dataclass
class ProjectConfig:
    wordware: ProjectConfigWordWare

    def __post_init__(self):
        self.wordware = ProjectConfigWordWare(**self.wordware)


def load_project_config():
    return ProjectConfig(**load_config("project_config.toml"))


## credentials loader
@dataclass
class CredentialsWordWare:
    api_key: str


@dataclass
class Credentials:
    wordware: CredentialsWordWare

    def __post_init__(self):
        self.wordware = CredentialsWordWare(**self.wordware)


def load_credentials_config():
    return Credentials(**load_config("credentials.toml"))
