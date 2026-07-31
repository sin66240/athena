from athena.memory.experience import Experience
from athena.memory.replay_buffer import ReplayBuffer


def test_buffer_add():

    buffer = ReplayBuffer()

    exp = Experience(
        state="s",
        action="call",
        reward=1,
        next_state="s2"
    )

    buffer.add(exp)

    assert len(buffer) == 1



def test_buffer_sample():

    buffer = ReplayBuffer()

    for i in range(5):

        buffer.add(
            Experience(
                state=i,
                action="call",
                reward=i,
                next_state=i+1
            )
        )


    batch = buffer.sample(3)

    assert len(batch) == 3