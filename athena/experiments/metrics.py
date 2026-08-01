class Metrics:
    """
    Stores experiment evaluation metrics.
    """


    def __init__(
        self,
        reward=None,
        accuracy=None,
        loss=None,
        win_rate=None
    ):

        self.reward = reward

        self.accuracy = accuracy

        self.loss = loss

        self.win_rate = win_rate



    def to_dict(
        self
    ):

        return {
            "reward": self.reward,
            "accuracy": self.accuracy,
            "loss": self.loss,
            "win_rate": self.win_rate
        }

