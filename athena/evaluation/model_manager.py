class ModelManager:
    """
    Manage champion and challenger models.
    """


    def __init__(
        self,
        champion=None
    ):

        self.champion = champion
        self.challenger = None



    def set_challenger(
        self,
        model
    ):

        self.challenger = model



    def promote(
        self
    ):

        if self.challenger is None:

            raise RuntimeError(
                "No challenger model"
            )


        self.champion = self.challenger

        self.challenger = None


        return self.champion



    def has_champion(
        self
    ):

        return self.champion is not None