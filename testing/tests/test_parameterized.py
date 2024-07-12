import pytest

from testing.Shape import Shape


class EquilateralTriangle(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        self.height = round(
            ((self.side_length**2 - (self.side_length / 2) ** 2) ** 0.5), 2
        )

    def area(self):
        return round((0.5 * self.side_length * self.height), 2)

    def perimeter(self):
        return 3 * self.side_length


@pytest.mark.parametrize(
    "side_length, expected_area", [(2, 1.73), (12, 62.34), (20, 173.2)]
)
def test_triangle_area(side_length, expected_area):
    d = EquilateralTriangle(side_length)
    assert d.area() == expected_area


@pytest.fixture
def get_triangle():
    def _get_triangle(side_length):
        return EquilateralTriangle(side_length)

    return _get_triangle


# with fixtures as well
@pytest.mark.parametrize(
    "side_length, expected_height", [(15, 12.99), (64, 55.43), (512, 443.41)]
)
def test_triangle_height(
    get_triangle,
    side_length,
    expected_height,
):
    t = get_triangle(side_length)
    assert t.height == expected_height
