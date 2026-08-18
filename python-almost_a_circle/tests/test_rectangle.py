#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def test_is_base_instance(self):
        """Test that Rectangle is an instance of Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_id_inheritance(self):
        """Test that id is correctly inherited and managed via Base."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, id=98)
        r3 = Rectangle(5, 5)
        
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 98)
        self.assertEqual(r3.id, 2)

    def test_attribute_initialization(self):
        """Test that required and optional attributes are assigned correctly."""
        r = Rectangle(5, 10, 2, 3, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_default_values(self):
        """Test default values for x, y, and id."""
        r = Rectangle(4, 6)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_getters_and_setters(self):
        """Test public getters and setters for all attributes."""
        r = Rectangle(1, 1)
        
        r.width = 15
        r.height = 25
        r.x = 5
        r.y = 10
        
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    def test_private_attributes(self):
        """Test that underlying attributes are private and raise AttributeError if accessed directly."""
        r = Rectangle(10, 20)
        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__height)


if __name__ == '__main__':
    unittest.main()
