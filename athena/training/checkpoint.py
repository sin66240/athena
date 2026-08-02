class Checkpoint:
    """
    Stores best performing model.
    """


    def __init__(self):

        self.best_model = None

        self.best_score = None



    def save_if_best(
        self,
        model,
        score
    ):


        if (
            self.best_score is None
            or score > self.best_score
        ):

            self.best_score = score

            self.best_model = model

            return True


        return False
