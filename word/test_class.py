import unittest
import sys
import what
from window import App


class TestStringMethods(unittest.TestCase):

#note: method needs "word" as prefix for method name

    def test_stuff(self):
        self.assertEqual("a", "b","?")

    def test_num(self):
        self.assertEqual(1, 1)

    def test_contains_nums(self):
        self.assertIn(1, [x for x in range(10)])




if __name__ == "__main__":

    unittest.main()

