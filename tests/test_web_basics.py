from learning_lab.web_basics import link_texts, page_title


HTML = """
<html>
  <head><title>Practice Page</title></head>
  <body>
    <a href="/one">One</a>
    <a href="/two">Two</a>
    <a href="/empty"></a>
  </body>
</html>

"""


def test_page_title_extracts_text():
    assert page_title(HTML) == "Practice Page"


def test_page_title_returns_empty_string_when_missing():
    assert page_title("<main>No title</main>") == ""


def test_link_texts_ignores_empty_links():
    assert link_texts(HTML) == ["One", "Two"]


from bs4 import BeautifulSoup

def page_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    return title.text if title else ""

def link_texts(html):
    soup = BeautifulSoup(html, "html.parser")
    return [
        link.get_text(strip=True)
        for link in soup.find_all("a")
        if link.get_text(strip=True)
    ]