from athena.evaluation.model_comparator import ModelComparator



def test_challenger_wins():

    comparator = ModelComparator()


    result = comparator.compare(
        0.70,
        0.80
    )


    assert result["winner"] == "challenger"

    assert result["promote"] is True



def test_champion_wins():

    comparator = ModelComparator()


    result = comparator.compare(
        0.90,
        0.80
    )


    assert result["winner"] == "champion"

    assert result["promote"] is False



def test_difference():

    comparator = ModelComparator()


    result = comparator.compare(
        0.70,
        0.85
    )


    assert result["difference"] == 0.15