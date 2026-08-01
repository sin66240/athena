import pickle
import os


class ModelStorage:
    """
    Save and load trained models.
    """


    def __init__(
        self,
        path="champion_model.pkl"
    ):

        self.path = path



    def save(
        self,
        model
    ):

        with open(
            self.path,
            "wb"
        ) as file:

            pickle.dump(
                model,
                file
            )


        return True



    def load(
        self
    ):

        if not os.path.exists(
            self.path
        ):

            raise FileNotFoundError(
                "Model file not found"
            )


        with open(
            self.path,
            "rb"
        ) as file:

            model = pickle.load(
                file
            )


        return model