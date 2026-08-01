class HyperParameters:
    """
    Store training hyperparameters.
    """


    def __init__(
        self,
        learning_rate,
        batch_size,
        epochs
    ):

        self.learning_rate = learning_rate

        self.batch_size = batch_size

        self.epochs = epochs



    def to_dict(
        self
    ):

        return {
            "learning_rate": self.learning_rate,
            "batch_size": self.batch_size,
            "epochs": self.epochs
        }
