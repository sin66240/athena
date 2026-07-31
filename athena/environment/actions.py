from enum import Enum


class Action(Enum):
    """
    Poker actions available for agents.
    """

    FOLD = "fold"
    CHECK = "check"
    CALL = "call"
    RAISE = "raise"