from learning_lab.leaderboard import add_score, top_scores


def test_add_score_keeps_highest_score():
    assert add_score({"Ada": 10}, "Ada", 8) == {"Ada": 10}
    assert add_score({"Ada": 10}, "Ada", 12) == {"Ada": 12}


def test_top_scores_returns_limited_ranking():
    scores = {"Ada": 10, "Grace": 12, "Katherine": 11}

    assert top_scores(scores, limit=2) == [("Grace", 12), ("Katherine", 11)]
