from dataclasses import dataclass


@dataclass
class Match:
    agent_a: str
    agent_b: str
    episodes: int = 1

    def run(self):
        return {
            "agent_a": self.agent_a,
            "agent_b": self.agent_b,
            "episodes": self.episodes
        }
