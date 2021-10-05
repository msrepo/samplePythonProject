import numpy as np
from numpy import ndarray


def square(array: ndarray) -> ndarray:
    """square each elements of an ndarray

    extended_summary

    :param array: ndarray
    :type array: ndarray
    :return: ndarray containing square of each elements
    :rtype: ndarray
    """
    return array * array
