from athena.experience.experience import Experience


class ExperienceBuilder:
    """
    Convert match result into learning experience.
    """


    def build(
        self,
        result
    ):

        winner = result.get(
            "winner"
        )


        reward = 0


        if winner:

            reward = 1



        return Experience(

            state={
                "agent_a": result.get(
                    "agent_a"
                ),

                "agent_b": result.get(
                    "agent_b"
                )
            },

            action="play",

            reward=reward,

            next_state=None,

            done=True
        )
