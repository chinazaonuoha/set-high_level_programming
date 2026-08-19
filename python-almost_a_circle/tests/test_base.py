#!/usr/bin/python3
"""
Unittest module for the Base class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


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


    def test_to_json_string_normal(self):
        """Test converting a standard list of dictionaries to a JSON string."""
        d_list = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        json_str = Rectangle.to_json_string(d_list)
        self.assertIsInstance(json_str, str)
        self.assertIn('"id": 1', json_str)
        self.assertIn('"width": 2', json_str)

    def test_to_json_string_none(self):
        """Test that passing None returns the empty JSON list string '[]'."""
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test that passing an empty list returns the empty JSON list string '[]'."""
        self.assertEqual(Rectangle.to_json_string([]), "[]")

if __name__ == '__main__':
    unittest.main()
