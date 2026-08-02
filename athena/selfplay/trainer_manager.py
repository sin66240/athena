from dataclasses import dataclass


@dataclass
class TrainingJob:

    model_name: str
    generation: int

    status: str = "created"



class TrainerManager:


    def __init__(
        self,
        registry
    ):

        self.registry = registry
        self.jobs = []



    def create_job(
        self,
        model_name,
        generation
    ):

        job = TrainingJob(
            model_name=model_name,
            generation=generation
        )

        self.jobs.append(job)

        return job



    def start_training(
        self,
        job
    ):

        job.status = "training"

        return job



    def complete_training(
        self,
        job
    ):

        job.status = "completed"

        return job



    def latest_job(self):

        if not self.jobs:
            return None

        return self.jobs[-1]
