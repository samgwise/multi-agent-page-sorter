class Agent:

    def __init__(self,id,page, llm, consortium):
        self.id = id
        self.page = page
        self.llm = llm
        self.consortium = consortium

    #Respond with a tuple of the form id:message
    def step():
        pass
    
    #respond is not called during your step, it's called during someone else's, via consortium.query
    def respond():
        pass