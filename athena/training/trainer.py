class Trainer:
    """
    Controls agent training loop.
    """

    def __init__(
        self,
        agent=None,
        environment=None,
        memory=None,
        dataset=None,
        callbacks=None
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


        # Callbacks
        self.callbacks = callbacks or []


        # Training history
        self.history = []


        # Training metrics
        self.best_reward = None
        self.best_episode = None
        self.last_reward = None
        self.total_episodes = 0


        # Early stopping
        self.stopped_early = False
        self.stop_reason = None



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



    def train(
        self,
        episodes,
        patience=None
    ):

        no_improvement = 0

        self.stopped_early = False
        self.stop_reason = None


        # callback start
        for callback in self.callbacks:
            callback.on_train_start(self)



        for _ in range(episodes):

            reward = self.run_episode()


            self.history.append(
                reward
            )


            self.total_episodes += 1

            self.last_reward = reward


            improved = False


            if (
                self.best_reward is None
                or reward > self.best_reward
            ):

                self.best_reward = reward
                self.best_episode = self.total_episodes

                improved = True



            # callback episode end
            for callback in self.callbacks:
                callback.on_episode_end(
                    self,
                    self.total_episodes,
                    reward
                )



            if improved:

                no_improvement = 0


                # callback best model
                for callback in self.callbacks:
                    callback.on_best_model(
                        self,
                        reward
                    )


            else:

                no_improvement += 1



            if (
                patience is not None
                and no_improvement >= patience
            ):

                self.stopped_early = True

                self.stop_reason = "No improvement"

                break



        # callback end
        for callback in self.callbacks:
            callback.on_train_end(self)



        return sum(self.history)



    def average_reward(
        self
    ):

        if not self.history:
            return 0


        return sum(self.history) / len(self.history)



    def reset_history(
        self
    ):

        self.history = []

        self.best_reward = None
        self.best_episode = None
        self.last_reward = None
        self.total_episodes = 0

        self.stopped_early = False
        self.stop_reason = None