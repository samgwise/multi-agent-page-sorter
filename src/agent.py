import random
class Agent:

    def __init__(self,id,page, llm, consortium):
        self.id = id
        self.page = page
        self.llm = llm
        self.consortium = consortium

    #Random until we figure out whether this can be done in one prompt or needs a decide action.
        if random.random() > 0.5:
            return self.propose()
        return self.query()
    
    def propose(self):
        inputs = {
                "id":self.id,
                "page":self.page,
                "history":self.consortium.get_flat_history()
            }
        return (self.id,self.llm.call("propose_prompt",inputs))

    def query(self):
        inputs = {
                "id":self.id,
                "page":self.page,
                "history":self.consortium.get_flat_history()
            }
        query = self.llm.call("query_prompt",inputs)
        answers = self.consortium.query(query,self.id)
        return (self.id,{"query":query, "responses":answers})

    #respond is not called during your step, it's called during someone else's, via consortium.query
    def respond(self,query):
        inputs = {
                "query":query,
                "id":self.id,
                "page":self.page,
                "history":self.consortium.get_flat_history()
            }
        return (self.id,self.llm.call("respond_prompt",inputs))