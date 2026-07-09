from learning_lab.sanitizer import collapse_spaces, escape_html


def test_collapse_spaces_normalizes_whitespace():
    assert collapse_spaces("  learn   python\nnow ") == "learn python now"


def test_escape_html_escapes_tags_and_quotes():
    assert escape_html('<a href="x">link</a>') == "&lt;a href=&quot;x&quot;&gt;link&lt;/a&gt;"
