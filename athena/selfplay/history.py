from dataclasses import dataclass, asdict, field
from datetime import datetime, UTC
from typing import List, Dict, Any


@dataclass
class MatchHistory:

    model_a: str
    model_b: str

    winner: str | None

    score_a: float
    score_b: float

    elo_a_before: float
    elo_b_before: float

    elo_a_after: float
    elo_b_after: float

    episodes: int = 1
    
    timestamp: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat()
    )


class SelfPlayHistory:


    def __init__(self):

        self.records: List[MatchHistory] = []



    def add_match_history(self, result):
        """
        รับผลจาก Match.run()
        """

        if isinstance(result, dict):

            return self.add_match(

                model_a=str(
                    result.get(
                        "agent_a",
                        "unknown"
                    )
                ),

                model_b=str(
                    result.get(
                        "agent_b",
                        "unknown"
                    )
                ),

                winner=result.get(
                    "winner"
                ),

                score_a=result.get(
                    "score_a",
                    0
                ),

                score_b=result.get(
                    "score_b",
                    0
                ),

                elo_a_before=result.get(
                    "elo_a_before",
                    0
                ),

                elo_b_before=result.get(
                    "elo_b_before",
                    0
                ),

                elo_a_after=result.get(
                    "elo_a_after",
                    0
                ),

                elo_b_after=result.get(
                    "elo_b_after",
                    0
                ),

                episodes=result.get(
                    "episodes",
                    1
                )

            )


        return self.add_match(

            model_a=str(result.model_a),

            model_b=str(result.model_b),

            winner=result.winner,

            score_a=result.score_a,

            score_b=result.score_b,

            elo_a_before=result.elo_a_before,

            elo_b_before=result.elo_b_before,

            elo_a_after=result.elo_a_after,

            elo_b_after=result.elo_b_after,

            episodes=getattr(
                result,
                "episodes",
                1
            )

        )



    def add_match(

        self,

        model_a: str,

        model_b: str,

        winner: str | None,

        score_a: float,

        score_b: float,

        elo_a_before: float,

        elo_b_before: float,

        elo_a_after: float,

        elo_b_after: float,

        episodes: int = 1

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

            episodes=episodes
            
            # ไม่ต้องส่ง timestamp แล้ว ปล่อยให้ default_factory จัดการ

        )


        self.records.append(record)


        return record



    def get_all(self) -> List[Dict[str, Any]]:

        return [
            asdict(record)
            for record in self.records
        ]



    def latest(self):

        if not self.records:

            return None

        return self.records[-1]



    def count(self) -> int:

        return len(self.records)



    def clear(self):

        self.records.clear()