from dataclasses import dataclass


@dataclass
class Experience:
    """
    Single agent experience record.
    Stores one decision cycle.
    """

    state: object
    action: str
    reward: float
    next_state: object