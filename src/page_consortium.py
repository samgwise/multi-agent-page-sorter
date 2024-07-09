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

print(vars(project_config))

project_config = load_credentials_config();

print(vars(project_config))