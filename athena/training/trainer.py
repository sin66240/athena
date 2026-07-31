class Trainer:
    """
    Controls agent training loop.
    """

    def __init__(
        self,
        agent,
        environment,
        memory
    ):

        self.agent = agent
        self.environment = environment
        self.memory = memory


    def run_episode(self):

        state = self.environment.reset()

        done = False
        total_reward = 0


        while not done:

            action = self.agent.decide(
                state
            )


            result = self.environment.step()


            reward = result["reward"]


            self.memory.add(
                {
                    "state": state,
                    "action": action,
                    "reward": reward,
                    "next_state": result
                }
            )


            total_reward += reward

            done = True


        return total_reward