import random
from llm import LLM
from consortium import Consortium


class Agent:
    def __init__(self, id: int, page: str, llm: LLM, consortium: Consortium):
        self.id = id
        self.page = page
        self.llm = llm
        self.consortium = consortium

        # Random until we figure out whether this can be done in one prompt or needs a decide action.
        if random.random() > 0.5:
            return self.propose()
        return self.query()

    def propose(self):
        return (
            self.id,
            self.llm.propose_prompt(self.id, self.page, self.consortium.flat_history()),
        )

    def query(self):
        query = self.llm.query_prompt(
            self.id, self.consortium.flat_history(), self.page
        )
        answers = self.consortium.query(query, self.id)
        return (self.id, {"query": query, "responses": answers})

    # respond is not called during your step, it's called during someone else's, via consortium.query
    def respond(self, query):
        return (
            self.id,
            self.llm.respond_prompt(
                self.id, self.consortium.flat_history(), self.page, query
            ),
        )
