from collections import deque
from random import sample


class ReplayBuffer:
    """
    Stores and samples agent experiences.
    """

    def __init__(self, capacity=1000):

        self.buffer = deque(
            maxlen=capacity
        )


    def add(self, experience):

        self.buffer.append(
            experience
        )


    def sample(self, batch_size):

        return sample(
            self.buffer,
            batch_size
        )


    def __len__(self):

        return len(
            self.buffer
        )