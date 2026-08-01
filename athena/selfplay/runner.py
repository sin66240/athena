class SelfPlayRunner:
    """
    Runs AI agents against each other
    to generate training data.
    """

    def __init__(
        self,
        environment,
        agent1,
        agent2,
        dataset
    ):

        self.environment = environment
        self.agent1 = agent1
        self.agent2 = agent2
        self.dataset = dataset


    def run_game(self):

        state = self.environment.reset()

        agents = [
            self.agent1,
            self.agent2
        ]


        actions = []


        for agent in agents:

            action = agent.decide(
                state
            )

            actions.append(action)


        result = self.environment.step()


        reward = result["reward"]


        for agent, action in zip(
            agents,
            actions
        ):

            self.dataset.add(
                state=state,
                action=action,
                reward=reward
            )


        return {
            "actions": actions,
            "reward": reward
        }