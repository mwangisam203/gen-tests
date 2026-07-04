from learning_lab.sets_basics import missing_items, shared_items, unique_names


def test_unique_names_normalizes_and_deduplicates():
    assert unique_names([" ada ", "Ada", "", "grace"]) == {"Ada", "Grace"}


def test_shared_items_returns_intersection():
    assert shared_items({"pen", "paper"}, {"paper", "book"}) == {"paper"}


def test_missing_items_returns_difference():
    assert missing_items({"id", "email"}, {"email"}) == {"id"}
