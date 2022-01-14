import unittest
from just_test import fun


class Test(unittest.TestCase):
    def test_def(self):
        self.assertEqual(fun(2, 2), 6)
