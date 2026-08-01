class ModelManager:
    """
    Manage champion and challenger models.
    """


    def __init__(
        self,
        champion=None,
        storage=None
    ):

        self.champion = champion
        self.challenger = None
        self.storage = storage



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


        if self.storage:

            self.storage.save(
                self.champion
            )


        return self.champion



    def load_champion(
        self
    ):

        if self.storage is None:

            raise RuntimeError(
                "Storage not configured"
            )


        self.champion = self.storage.load()


        return self.champion



    def has_champion(
        self
    ):

        return self.champion is not None