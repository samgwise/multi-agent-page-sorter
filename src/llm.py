#
# Defines an interface for an llm for use in a consortium of agents.
#

from config import ProjectConfigWordWare, CredentialsWordWare

class LLM:

    def __init__(self, credentials, project_config):
        self.credentials = credentials
        self.configuration = project_config