class Trainer:
    """
    Controls agent training loop.
    """

    def __init__(
        self,
        agent=None,
        environment=None,
        memory=None,
        dataset=None
    ):

        # Support Trainer(dataset)
        if (
            environment is None
            and memory is None
            and dataset is None
            and agent is not None
            and hasattr(agent, "add")
        ):
            dataset = agent
            agent = None


        self.agent = agent
        self.environment = environment
        self.memory = memory
        self.dataset = dataset


    def run_episode(self):

        if (
            self.agent is None
            or self.environment is None
            or self.memory is None
        ):
            raise RuntimeError(
                "Agent, environment and memory required"
            )


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