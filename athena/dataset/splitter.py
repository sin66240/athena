from sklearn.model_selection import train_test_split


class DatasetSplitter:
    """
    Split dataset into train and validation sets.
    """


    def split(
        self,
        data,
        test_size=0.2
    ):

        return train_test_split(
            data,
            test_size=test_size,
            random_state=42
        )
