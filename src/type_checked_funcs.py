import numpy as np
from numpy import ndarray
from typing import Callable

from numpy.lib.function_base import delete


def square(array: ndarray) -> ndarray:
    """square each elements of an ndarray

    extended_summary

    :param array: ndarray
    :type array: ndarray
    :return: ndarray containing square of each elements
    :rtype: ndarray
    """
    return array * array


def derivative(func: Callable, x: float, delta: float) -> float:
    """calculate derivative of func at x

    numerically calculate derivative of func at x by calculating rate of change in the neighbourhood
    delta of x 

    :param func: any Callable
    :type func: Callable
    :param x: calculat func at
    :type x: float
    :param delta: neighborhood 
    :type delta: float
    :return: derivative of func at x in neighborhood delta
    :rtype: float
    """
    return (func(x + delta) - func(x - delta)) / (2.0 * delta)
