from agent import Agent

class Consortium:    
    def __init__(self, pages, llm):
        self.agents = [Agent(i, p, llm, self) for i,p in enumerate(pages)]
        self.history = [(-1,"START")]
        self.solution = self.init_solution(len(pages))

    def step(self):
        selected_agent = self.select_agent()
        self.update_history(selected_agent.step())
        self.has_solution()

    #For now, make this a trivial "Next agent in the list".
    def select_agent(self):
        current_agent = self.history[-1][0]
        return self.agents((current_agent+1)%len(self.agents))

    #This probably needs to be smarter in future.
    def update_history(self,message):
        self.history.append(message)

    #Returns a flat string version of the history to be used as input for LLMs.
    def get_flat_history(self):
        flat_history = []
        for id,event in self.history:
            if type(event) is str: #We're dealing with a proposal.
                flat_history.append(f"AGENT {id} PROPOSED: {event}")
            else: #We're dealing with a query.
                flat_history.append(f"AGENT {id} ASKED: {event['query']}")
                for response in event["responses"]:
                    flat_history.append(f"  * AGENT {id} ANSWERED: {response}")
        return "\n".join(flat_history)

    #This is a stub, we'll have to implement this at some point.
    def has_solution(self):
        return len(self.history) > 20

    def init_solution(self):
        pass

    def query(self, query, source_agent):
        responses = [(id,self.agents[id].respond(query)) for id in range(len(self.agents)) if id != source_agent]
        responses = [(id,response) for (id,response) in responses if response != "Nothing."]
        return responses