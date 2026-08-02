from athena.dataset.training_dataset import TrainingDataset


class ExperienceDatasetBuilder:
    """
    Convert replay experiences into TrainingDataset.
    """


    def build(
        self,
        experiences
    ):

        dataset = TrainingDataset()


        for exp in experiences:

            dataset.add(
                state=exp.state,
                action=exp.action,
                reward=exp.reward
            )


        return dataset
