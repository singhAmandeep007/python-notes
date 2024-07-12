def capitalize(sentence):
    """
    This function takes a sentence as input and
    returns the sentence with the first letter of each word capitalized.

    :param sentence: A string that represents the sentence to be capitalized.
    :type sentence: str
    :return: The input sentence with the first letter of each word capitalized.
    :rtype: str
    """
    return " ".join(
        list(map(lambda word: word[0].upper() + word[1:], sentence.split(" ")))
    )


def compare_sem_version(version1, version2):
    """
    This function compares two semantic version numbers and returns the result.

    :param version1: The first semantic version number.
    :type version1: str
    :param version2: The second semantic version number.
    :type version2: str
    :return: 0 if the versions are equal,
        -1 if version1 is less than version2,
        1 if version1 is greater than version2.
    :rtype: int
    """
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))

    for i in range(3):
        if v1[i] < v2[i]:
            return -1
        if v1[i] > v2[i]:
            return 1

    return 0
