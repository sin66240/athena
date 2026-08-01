class ModelManager:
    """
    Manage champion and challenger models.
    """


    def __init__(
        self,
        champion=None,
        storage=None,
        registry=None
    ):

        self.champion = champion
        self.challenger = None

        self.storage = storage
        self.registry = registry



    def set_challenger(
        self,
        model
    ):

        self.challenger = model



    def register_challenger(
        self,
        reward=0
    ):

        if self.registry is None:

            raise RuntimeError(
                "Model registry required"
            )


        if self.challenger is None:

            raise RuntimeError(
                "No challenger model"
            )


        return self.registry.register(
            self.challenger,
            reward=reward
        )



    def load(
        self
    ):

        if self.storage is None:

            return None


        model = self.storage.load()


        if model is not None:

            self.champion = model


        return self.champion



    def load_champion(
        self
    ):

        return self.load()



    def promote(
        self
    ):

        if self.challenger is None:

            raise RuntimeError(
                "No challenger model"
            )


        self.champion = self.challenger


        if self.storage is not None:

            self.storage.save(
                self.champion
            )


        if self.registry is not None:

            latest = self.registry.latest()


            if latest is not None:

                self.registry.promote(
                    latest["version"]
                )


        self.challenger = None


        return self.champion



    def has_champion(
        self
    ):

        return self.champion is not None