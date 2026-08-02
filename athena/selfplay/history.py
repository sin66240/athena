from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict, Any


@dataclass
class MatchHistory:

    model_a: str
    model_b: str

    winner: str

    score_a: float
    score_b: float

    elo_a_before: float
    elo_b_before: float

    elo_a_after: float
    elo_b_after: float

    timestamp: str = None


class SelfPlayHistory:

    def __init__(self):

        self.records: List[MatchHistory] = []


    def add_match(
        self,
        model_a: str,
        model_b: str,
        winner: str,
        score_a: float,
        score_b: float,
        elo_a_before: float,
        elo_b_before: float,
        elo_a_after: float,
        elo_b_after: float,
    ):

        record = MatchHistory(

            model_a=model_a,

            model_b=model_b,

            winner=winner,

            score_a=score_a,

            score_b=score_b,

            elo_a_before=elo_a_before,

            elo_b_before=elo_b_before,

            elo_a_after=elo_a_after,

            elo_b_after=elo_b_after,

            timestamp=datetime.utcnow().isoformat()

        )


        self.records.append(record)


        return record



    def get_all(self) -> List[Dict[str, Any]]:

        return [
            asdict(record)
            for record in self.records
        ]



    def count(self) -> int:

        return len(self.records)



    def latest(self):

        if not self.records:

            return None


        return self.records[-1]



    def clear(self):

        self.records.clear()
