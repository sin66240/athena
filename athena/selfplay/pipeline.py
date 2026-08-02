from dataclasses import dataclass

from athena.selfplay.promotion import PromotionPolicy


@dataclass
class PipelineResult:
    promoted: bool
    games: int
    wins: int



class SelfPlayPipeline:

    def __init__(
        self,
        promotion_policy=None
    ):

        self.promotion_policy = (
            promotion_policy
            or PromotionPolicy()
        )


    def run(
        self,
        wins,
        games
    ):

        result = self.promotion_policy.evaluate(
            wins=wins,
            games=games
        )

        return PipelineResult(
            promoted=result.promoted,
            games=games,
            wins=wins
        )
