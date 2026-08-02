from dataclasses import dataclass


@dataclass
class PromotionResult:
    promoted: bool
    win_rate: float
    threshold: float



class PromotionPolicy:

    def __init__(
        self,
        threshold=0.55
    ):
        self.threshold = threshold


    def evaluate(
        self,
        wins,
        games
    ):

        if games == 0:
            return PromotionResult(
                False,
                0.0,
                self.threshold
            )


        win_rate = wins / games


        return PromotionResult(
            promoted=win_rate >= self.threshold,
            win_rate=win_rate,
            threshold=self.threshold
        )
