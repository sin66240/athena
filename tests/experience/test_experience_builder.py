from athena.experience.experience_builder import ExperienceBuilder



def test_build_experience():

    builder = ExperienceBuilder()


    result = {

        "agent_a":"Athena",

        "agent_b":"Bot",

        "winner":"Athena"

    }


    exp = builder.build(
        result
    )


    assert exp.reward == 1
    assert exp.done is True
