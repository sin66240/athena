from athena.dataset.experience_dataset_builder import (
    ExperienceDatasetBuilder
)

from athena.experience.experience import Experience



def test_build_dataset():

    builder = ExperienceDatasetBuilder()


    experiences = [

        Experience(
            state={"card": "AA"},
            action="raise",
            reward=1,
            next_state=None,
            done=True
        )

    ]


    dataset = builder.build(
        experiences
    )


    assert len(dataset) == 1

    assert dataset.samples[0]["action"] == "raise"

    assert dataset.samples[0]["reward"] == 1
