import pytest
from testing.Shape import Shape

ONE = 1


# FUNCTION BASED TESTS
def test_function_passes():
    assert ONE == 1


@pytest.mark.xfail(reason="Test is expected to fail")
def test_function_fails():
    assert ONE == 2


def func_raise_error():
    raise SystemExit(1)


# assert that a certain exception is raised
def test_function_raise_error():
    with pytest.raises(SystemExit):
        func_raise_error()


def func_divide(num, den):
    if den == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    return num / den


def test_function_divide():
    with pytest.raises(ZeroDivisionError):
        assert func_divide(10, 0)


# CLASS BASED TESTS
# group multiple test cases in a class
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = {"hello": 1, "check": 2}
        assert "check" in x


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method.__name__} method")
        self.circle = Circle(3)

    def test_area(self):
        assert self.circle.area() == 28.26

    def test_perimeter(self):
        assert self.circle.perimeter() == 18.84

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__} method")
        del self.circle
