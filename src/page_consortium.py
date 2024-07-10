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
from dataclasses import dataclass

# Ecosystem #

# Project #

from config import *

#
# Defs
#


#
# MAIN
#

print("Hi")

project_config = load_project_config();

#print(vars(project_config))

project_credentials = load_credentials_config();

#print(vars(project_credentials))

from llm import LLM
from consortium import Consortium
llm = LLM(project_credentials,project_config)
print(llm._call_wordware("dummy_prompt", {"topic":"bees"}))

pages = [
    "This is the first page.",
    "This is the second page.",
    "This is the third page.",
]

consortium = Consortium(pages,llm)

consortium.run()