import unittest

import numpy as np
from context import src
from src.type_checked_funcs import square, derivative


class FuncTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_square(self):

        a = np.array([1, 2, 3, 4])
        b = np.array([1, 4, 9, 16])
        assert((square(a) == b).all())

    def test_derivative(self):
        def func(x):
            return x * x
        a = 2.0
        da = 4.0
        delta = 1e-4
        out = derivative(func, a, delta)
        assert(da - out < 1e-5)


if __name__ == '__main__':
    unittest.main()
