from dataclasses import dataclass
from typing import Any


@dataclass
class Experience:
    """
    Single learning experience.
    """

    state: Any

    action: Any

    reward: float

    next_state: Any

    done: bool
