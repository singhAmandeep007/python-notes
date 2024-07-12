import time
import pytest


# MARKERS
# custom markers can be defined in pytest.ini
@pytest.mark.slow
def test_slow():
    time.sleep(1)
    result = 1
    assert result == 1


# inbuilt markers
# skip test
@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    assert True


# mark test as expected to fail
@pytest.mark.xfail(reason="Test is expected to fail")
def test_expected_fail():
    assert False
