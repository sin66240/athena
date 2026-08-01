import pandas as pd
from athena.dataset.loader import DatasetLoader


def test_loader(tmp_path):

    file = tmp_path / "data.csv"


    pd.DataFrame(
        {
            "x":[1,2,3]
        }
    ).to_csv(
        file,
        index=False
    )


    loader = DatasetLoader()

    data = loader.load(
        file
    )


    assert len(data) == 3
