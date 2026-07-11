# Import the requests library so we can send HTTP requests to websites
# import requests

# # Import BeautifulSoup so we can parse and search through HTML later
# from bs4 import BeautifulSoup

# # Store the website URL we want to request
# url = "https://www.livescore.com/en/"

# # Send a GET request to the website and store the response
# response = requests.get(url)


# # Get the HTTP status code from the response
# status = response.status_code

# content = response.content
# soup = BeautifulSoup(content, "html.parser")

# # Print the status code to the terminal
# print(status)
# print(soup.title)
# print(soup.title.get_text)
# print(soup.body)  # gives the whole page on the website

y = " great"
def myfunc():
    y = "fabulous"
    print("my day was" + y)

myfunc()
print(f"my day was {y}")

def global_func():
    global x
    x = "interesting"

global_func()
print(f"I had a quite an {x} day")

#test addition
def add(a, b):
    return a + b


#test math utils
from math import add


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -5) == -7


def test_add_zero():
    assert add(0, 7) == 7


def reverse(text):
    return text[::-1]


#Testing String Reversal :from strings import reverse


def test_reverse_word():
    assert reverse("python") == "nohtyp"


def test_reverse_empty_string():
    assert reverse("") == ""


def test_reverse_single_letter():
    assert reverse("A") == "A"


#even number
def is_even(number):
    return number % 2 == 0

from numbers import is_even


def test_even_number():
    assert is_even(10)


def test_odd_number():
    assert not is_even(9)


def test_zero_is_even():
    assert is_even(0)

#email validation test
def is_valid_email(email):
    return "@" in email and "." in email

#from validation import is_valid_email


def test_valid_email():
    assert is_valid_email("john@gmail.com")


def test_missing_at_symbol():
    assert not is_valid_email("johngmail.com")


def test_missing_dot():
    assert not is_valid_email("john@gmail")

#number sorting
def sort_numbers(numbers):
    return sorted(numbers)