import pytest

from testing.Animal import Dog, Cat


@pytest.fixture
def make_dog():
    return Dog("Buddy")


@pytest.fixture
def make_cat():
    return Cat("Whiskers")
