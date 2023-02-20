import numpy as np


def set_of_values(min, max):
    """
    create a range of values

    min: left minimal value

    max: right maximal value
    """
    values = np.linspace(min, max, 10, endpoint=True)
    return list(values)
