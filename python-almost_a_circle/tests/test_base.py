#!/usr/bin/python3
"""
Unittest module for the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_nb_objects_private(self):
        """Test that __nb_objects is a private class attribute."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_id_automatic(self):
        """
        Test automatic ID assignment
        when id is not provided.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_explicit(self):
        """Test explicit ID assignment."""
        b = Base(98)
        self.assertEqual(b.id, 98)


if __name__ == '__main__':
    unittest.main()
