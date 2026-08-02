from athena.experience.replay_buffer import ReplayBuffer
from athena.experience.experience import Experience



def test_buffer_add():

    buffer = ReplayBuffer()


    exp = Experience(
        "s",
        "a",
        1,
        "ns",
        False
    )


    buffer.add(exp)


    assert buffer.count() == 1



def test_buffer_limit():

    buffer = ReplayBuffer(
        capacity=2
    )


    for i in range(3):

        buffer.add(
            Experience(
                i,
                i,
                1,
                i,
                False
            )
        )


    assert buffer.count() == 2
