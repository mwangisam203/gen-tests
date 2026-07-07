from learning_lab.word_games import anagram_key, are_anagrams, is_palindrome


def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("Never odd or even")


def test_anagram_key_sorts_lowercase_letters():
    assert anagram_key("Tea") == "aet"


def test_are_anagrams_compares_letters():
    assert are_anagrams("listen", "silent")
    assert not are_anagrams("python", "tests")
