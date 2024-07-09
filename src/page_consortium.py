#! /usr/bin/env python

#
# Page Consortium sorts a collection of pages using multiple llm agents.
#
# This script orchestrates the flow of information between agents and tracks the consortium's progress towards a complete answer.
#

#
# Imports
#

# Core #
import tomllib
from dataclasses import dataclass

# Ecosystem #

# Project #

#
# Defs
#

## Generic config loader
def load_config(path):
    with open(path, 'rb') as conf:
        return tomllib.load(conf)

## Project config loader
@dataclass
class ProjectConfigWordWare:
    # Delete this once stub is integrated
    dummy_prompt: str
    propose_prompt: str
    query_prompt: str
    respond_prompt: str

@dataclass
class ProjectConfig:
    wordware: ProjectConfigWordWare 

    def __post_init__(self):
        self.wordware = ProjectConfigWordWare( **self.wordware )

def load_project_config():
    return ProjectConfig( **load_config("project_config.toml") )

## credentials loader
@dataclass
class CredentialsWordWare:
    api_key: str

@dataclass
class Credentials:
    wordware: CredentialsWordWare 

    def __post_init__(self):
        self.wordware = CredentialsWordWare( **self.wordware )

def load_credentials_config():
    return Credentials( **load_config("credentials.toml") )

#
# MAIN
#

print("Hi")

project_config = load_project_config();

print(vars(project_config))

project_config = load_credentials_config();

print(vars(project_config))