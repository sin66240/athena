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


        for model in self.models:

            if model["version"] == self.current_version:

                return model


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


        self.current_version = version


        return self.champion()



    def rollback(
        self,
        version
    ):

        target = None


        for model in self.models:

            if model["version"] == version:

                target = model
                break



        if target is None:

            raise ValueError(
                "Version not found"
            )



        self.current_version = version



        for model in self.models:

            if model["version"] == version:

                model["status"] = "champion"

            else:

                if model["status"] == "champion":

                    model["status"] = "archive"



        return target
