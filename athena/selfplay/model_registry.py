from dataclasses import dataclass, field



@dataclass
class ModelVersion:

    name: str
    generation: int

    elo: float = 1200

    wins: int = 0
    losses: int = 0

    status: str = "challenger"



class ModelRegistry:


    def __init__(self):

        self.models = []



    def register(
        self,
        model
    ):

        self.models.append(model)

        return model



    def get_champion(self):

        champions = [
            m for m in self.models
            if m.status == "champion"
        ]

        if not champions:
            return None

        return max(
            champions,
            key=lambda x: x.elo
        )



    def promote(
        self,
        model
    ):

        for m in self.models:
            if m.status == "champion":
                m.status = "archived"


        model.status = "champion"

        return model
