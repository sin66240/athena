from dataclasses import dataclass



@dataclass
class SelfPlayCycle:

    generation: int
    status: str = "created"




class SelfPlayOrchestrator:


    def __init__(
        self,
        trainer_manager,
        pipeline,
        tournament,
        promotion
    ):

        self.trainer_manager = trainer_manager
        self.pipeline = pipeline
        self.tournament = tournament
        self.promotion = promotion

        self.cycles = []



    def create_cycle(
        self,
        generation
    ):

        cycle = SelfPlayCycle(
            generation=generation
        )

        self.cycles.append(cycle)

        return cycle



    def run_cycle(
        self,
        cycle
    ):

        cycle.status = "running"

        return cycle



    def complete_cycle(
        self,
        cycle
    ):

        cycle.status = "completed"

        return cycle



    def latest_cycle(self):

        if not self.cycles:
            return None

        return self.cycles[-1]
