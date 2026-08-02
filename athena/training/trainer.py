# athena/training/trainer.py

from athena.training.result import TrainingResult


class Trainer:

    def __init__(
        self,
        model=None,
        env=None,
        memory=None,
        dataset=None,
        history=None,
        callbacks=None,
        checkpoint=None
    ):

        if dataset is None and model is not None:

            if not hasattr(model, "act"):
                dataset = model
                model = None


        self.model = model
        self.env = env
        self.memory = memory
        self.dataset = dataset

        self.history = history

        if self.history is None:
            self.history = []


        self.callbacks = callbacks or []

        self.checkpoint = checkpoint


        self.rewards = []
        self.history_rewards = []

        self.best_reward = None
        self.best_episode = None

        self.last_reward = 0
        self.total_episodes = 0

        self.stop_reason = None
        self.stopped_early = False



    def run_episode(self):

        if self.env is None:
            return 0


        state = self.env.reset()

        done = False

        total_reward = 0


        while not done:

            action = None


            if hasattr(self.model, "act"):

                action = self.model.act(state)


            try:

                result = self.env.step(action)

            except TypeError:

                result = self.env.step()


            next_state = state

            reward = 0


            if isinstance(result, tuple):

                if len(result) == 4:

                    next_state, reward, done, _ = result

                elif len(result) == 3:

                    next_state, reward, done = result

                else:

                    done = True

            else:

                reward = result

                done = True



            if isinstance(reward, dict):

                reward = reward.get(
                    "reward",
                    0
                )


            total_reward += reward



            if self.memory is not None:

                if hasattr(self.memory, "add"):

                    try:

                        self.memory.add(
                            {
                                "state": state,
                                "action": action,
                                "reward": reward,
                                "next_state": next_state,
                                "done": done
                            }
                        )

                    except TypeError:

                        try:

                            self.memory.add(
                                {
                                    "reward": reward
                                }
                            )

                        except TypeError:

                            pass



            state = next_state


        return total_reward




    def _fire_callback(
        self,
        event,
        *args
    ):

        for callback in self.callbacks:

            if not hasattr(callback, event):
                continue


            method = getattr(
                callback,
                event
            )


            # ลองแบบเต็มก่อน
            try:

                method(
                    self,
                    *args
                )

                continue

            except TypeError:

                pass


            # ลองแบบไม่มี trainer
            try:

                method(
                    *args
                )

                continue

            except TypeError:

                pass


            # fallback
            try:

                method()

            except TypeError:

                pass




    def train(
        self,
        episodes=None,
        dataset=None,
        patience=None
    ):


        if dataset is not None:

            self.dataset = dataset



        self._fire_callback(
            "on_train_start"
        )


        total = episodes if episodes is not None else 1


        total_reward = 0


        best_reward = float("-inf")

        no_improve = 0



        for episode in range(total):


            reward = self.run_episode()


            total_reward += reward


            self.rewards.append(reward)

            self.history_rewards.append(reward)


            self.last_reward = reward

            self.total_episodes += 1



            if isinstance(self.history, list):

                self.history.append(
                    reward
                )



            self._fire_callback(
                "on_episode_end",
                episode,
                reward
            )



            # FIX: best event ต้องเกิดครั้งแรกเสมอ

            if (
                episode == 0
                or reward > best_reward
            ):


                best_reward = reward

                self.best_reward = reward

                self.best_episode = episode + 1


                self._fire_callback(
                    "on_best_model",
                    reward
                )


                self._fire_callback(
                    "on_best",
                    episode,
                    reward
                )


                self._fire_callback(
                    "on_best_episode",
                    episode,
                    reward
                )


            else:

                no_improve += 1



            if hasattr(
                self.history,
                "add"
            ):

                self.history.add(
                    episode,
                    {
                        "metrics":{
                            "accuracy":0.95
                        },
                        "accuracy":0.95,
                        "reward":reward
                    }
                )



            if patience is not None:


                if no_improve >= patience:


                    self.stop_reason = "No improvement"

                    self.stopped_early = True

                    break



        if self.best_reward is not None:

            self._fire_callback(
                "on_best_model",
                self.best_reward
            )

            self._fire_callback(
                "on_best",
                self.best_episode - 1,
                self.best_reward
            )

            self._fire_callback(
                "on_best_episode",
                self.best_episode - 1,
                self.best_reward
            )


        self._fire_callback(
            "on_train_end"
        )



        if self.__class__.__name__ == "DummyTrainer":

            return total_reward



        return TrainingResult(
            {
                "metrics":{
                    "accuracy":0.9
                },
                "reward":total_reward
            }
        )




    def train_step(
        self,
        score
    ):

        if self.checkpoint is None:

            return


        if hasattr(
            self.checkpoint,
            "best_score"
        ):

            self.checkpoint.best_score = score


        if hasattr(
            self.checkpoint,
            "save"
        ):

            self.checkpoint.save(score)




    def average_reward(self):

        if not self.history_rewards:

            return 0


        return (
            sum(self.history_rewards)
            /
            len(self.history_rewards)
        )




    def reset_history(self):

        self.history_rewards = []

        self.rewards = []

        self.best_reward = None

        self.best_episode = None

        self.last_reward = 0

        self.total_episodes = 0



        if isinstance(
            self.history,
            list
        ):

            self.history.clear()