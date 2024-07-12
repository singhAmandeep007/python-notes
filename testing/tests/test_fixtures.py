import pytest
import os

from testing.Shape import Shape


# FIXTURES
# a function that runs before and after each test function
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height


# class based test (won't require fixtures)
class TestRectangle:
    def setup_method(self, method):
        print(f"Setting up {method.__name__} method")
        self.rectangle = Rectangle(2, 3)

    def test_area(self):
        assert self.rectangle.area() == 6

    def test_perimeter(self):
        assert self.rectangle.perimeter() == 10

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__} method")
        del self.rectangle


# function based test (will require fixtures)
@pytest.fixture
def get_rectangle():
    return Rectangle(2, 3)


def test_rectangle_area(get_rectangle):
    assert get_rectangle.area() == 6


def test_rectangle_perimeter(get_rectangle):
    assert get_rectangle.perimeter() == 10


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# factories as fixtures
@pytest.fixture
def make_square():
    def _make_square(s):
        return Square(s)

    return _make_square


def test_rectangle_not_equal_square(get_rectangle, make_square):
    get_square = make_square(3)
    assert get_rectangle != get_square


# using global fixtures defined in conftest.py
def test_animal_same_legs(make_dog, make_cat):
    assert make_dog.legs() == make_cat.legs()


def test_animal_speak_different(make_dog, make_cat):
    assert make_dog.speak() != make_cat.speak()


weekdays = ["mon", "tue", "wed", "thu"]
weekends = ["sat", "sun"]


# fixtures can yield values
@pytest.fixture
def get_weekdays():
    copy = weekdays.copy()
    copy.append("fri")
    yield copy
    print("Cleaning up weekdays")
    copy.pop()


@pytest.fixture
def get_weekends():
    yield weekends.copy()
    print("Cleaning up weekends")


def test_week(
    get_weekends,
    get_weekdays,
):
    days = get_weekdays + get_weekends

    assert days == ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    assert len(days) == 7


@pytest.fixture
def append_text_to_file():
    filename = "test.txt"
    file_path = os.path.join(os.path.dirname(__file__), filename)

    # Check if file already exists
    if not os.path.exists(file_path):
        # Create the file if it doesn't exist
        open(file_path, "w").close()

    def _append_text_to_file(text: str):
        with open(file_path, "a") as f:
            f.write(text)

    yield _append_text_to_file
    print("Cleaning up file")
    # Remove the file after the test
    os.remove(file_path)


def test_append_text_to_file(append_text_to_file):
    append_text_to_file("Pytest")

    file_path = os.path.join(os.path.dirname(__file__), "test.txt")

    with open(file_path, "r") as f:
        assert f.read() == "Pytest"
    with open(file_path, "a") as f:
        f.write(" is awesome")
    with open(file_path, "r") as f:
        assert f.read() == "Pytest is awesome"
