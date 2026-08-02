from typing import List
from athena.experience.experience import Experience


class ReplayBuffer:
    """
    Store AI learning experiences.
    """


    def __init__(
        self,
        capacity=10000
    ):

        self.capacity = capacity

        self.buffer: List[Experience] = []



    def add(
        self,
        experience: Experience
    ):

        self.buffer.append(
            experience
        )


        if len(self.buffer) > self.capacity:

            self.buffer.pop(0)



    def sample(
        self,
        size
    ):

        return self.buffer[:size]



    def count(self):

        return len(self.buffer)



    def clear(self):

        self.buffer.clear()
