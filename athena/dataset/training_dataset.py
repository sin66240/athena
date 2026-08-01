class TrainingDataset:
    """
    Stores training samples for poker AI.
    """

    def __init__(self):

        self.samples = []

    def add(self, state, action, reward):

        self.samples.append(
            {
                "state": state,
                "action": action,
                "reward": reward,
            }
        )

    def __len__(self):

        return len(self.samples)

    def clear(self):

        self.samples.clear()