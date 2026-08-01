from athena.agents.base import BaseAgent
from athena.models.poker_model import PokerModel


class AIAgent(BaseAgent):
    """
    Agent that uses PokerModel to make decisions.
    """

    def __init__(self, name):

        super().__init__(name)

        self.model = PokerModel()

        # สำหรับตอนนี้ให้ถือว่า model พร้อมใช้งาน
        self.model.train([], [])

    def decide(self, state):

        return self.model.predict(state)

    def decide_action(self, state):

        action = self.decide(state)

        return action.upper()