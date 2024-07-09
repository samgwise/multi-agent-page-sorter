from agent import Agent

class Consortium:    
    def __init__(self, pages, llm):
        self.agents = [Agent(p, llm, self) for p in pages]
        self.history = []
        self.solution = self.init_solution(len(pages))

    def step(self):
        selected_agent = self.select_agent()
        self.update_history(selected_agent.step())
        self.has_solution()

    def select_agent(self):
        pass

    def update_history(self,message):
        pass

    def has_solution(self):
        pass

    def init_solution(self):
        pass

    def query(self, source_agent):
        pass