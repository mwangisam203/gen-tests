from learning_lab.tokenizer import bigrams, words


def test_words_returns_lowercase_tokens():
    assert words("Python, Tests!") == ["python", "tests"]


def test_bigrams_returns_neighbor_pairs():
    assert bigrams("one two three") == [("one", "two"), ("two", "three")]
