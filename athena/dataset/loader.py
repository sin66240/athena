import pandas as pd


class DatasetLoader:
    """
    Load training dataset.
    """


    def load(
        self,
        path
    ):

        return pd.read_csv(
            path
        )
