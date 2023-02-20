class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["eggs", "bacon", "spam"]


def silly_function(year, color):
    """
    Function find a color for approriate year

    year: value of chosen year

    color: string color type

    return: value

    """

    return None
