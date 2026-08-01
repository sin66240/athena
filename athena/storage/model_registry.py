class ModelRegistry:
    """
    Track model versions and metadata.
    """


    def __init__(self):

        self.models = []
        self.current_version = 0



    def register(
        self,
        model,
        reward=0,
        status="candidate"
    ):

        self.current_version += 1


        record = {
            "version": self.current_version,
            "model": model,
            "reward": reward,
            "status": status
        }


        self.models.append(
            record
        )


        return record



    def latest(
        self
    ):

        if not self.models:
            return None


        return self.models[-1]



    def champion(
        self
    ):

        champions = [
            m for m in self.models
            if m["status"] == "champion"
        ]


        if not champions:
            return None


        return max(
            champions,
            key=lambda x: x["reward"]
        )



    def promote(
        self,
        version
    ):

        for model in self.models:

            if model["version"] == version:

                model["status"] = "champion"

            else:

                if model["status"] == "champion":

                    model["status"] = "archive"


        return self.champion()