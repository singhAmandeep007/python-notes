"""
This is the `test_utils` module.
"""

import unittest

from testing.utils import capitalize, compare_sem_version


# This is a test class for the `capitalize` function from the `tictactoe` module.
class TestCapitalize(unittest.TestCase):
    """
    This is a test class for the `capitalize` function
    It inherits from the `unittest.TestCase` class
    which provides assertion methods to check for and report failures.
    """

    def test_one_word(self):
        """
        Test for a single word.
        :return:
        """
        text = "hello"
        result = capitalize(text)
        self.assertEqual(result, "Hello")

    def test_multiple_words(self):
        """
        Test for multiple words.
        :return:
        """
        text = "hello World hi"
        result = capitalize(text)
        self.assertEqual(result, "Hello World Hi")


class TestCompareSemVersion(unittest.TestCase):
    """
    This is a test class for the `compare_sem_version` function.
    It inherits from the `unittest.TestCase` class which provides
    assertion methods to check for and report failures.
    """

    def test_equal_versions(self):
        """
        Test for equal versions.
        """
        self.assertEqual(compare_sem_version("1.0.0", "1.0.0"), 0)

    def test_v1_less_than_v2(self):
        """
        Test for version1 less than version2.
        """
        self.assertEqual(compare_sem_version("1.0.0", "1.0.1"), -1)

    def test_v1_greater_than_v2(self):
        """
        Test for version1 greater than version2.
        """
        self.assertEqual(compare_sem_version("1.0.1", "1.0.0"), 1)


# if run directly
if __name__ == "__main__":
    # unittest.main() method is called to run all the tests on the methods that we defined.
    unittest.main()
