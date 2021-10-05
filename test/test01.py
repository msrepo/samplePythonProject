import unittest

import numpy as np
from context import src
from src.type_checked_funcs import square


class FuncTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_square(self):

        a = np.array([1, 2, 3, 4])
        b = np.array([1, 4, 9, 16])
        assert((square(a) == b).all())


if __name__ == '__main__':
    unittest.main()
