#!/usr/bin/python3
"""Unittests for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer()"""

    def test_max_at_end(self):
        """Test max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        """Test max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test list with one negative number"""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_only_negatives(self):
        """Test list with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
