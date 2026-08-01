class FeatureSchema:
    """
    Define feature contract.
    """


    def __init__(
        self,
        version="v1"
    ):

        self.version = version


        self.features = [
            "pot",
            "player_count",
            "street"
        ]
