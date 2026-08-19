#!/usr/bin/python3
"""
Unittest module for the Base class.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_save_to_file_rectangle(self):
        """Test writing the JSON string representation of rectangles to a file."""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
            expected = Rectangle.to_json_string([r.to_dictionary()])
            self.assertEqual(content, expected)
            os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None handles it gracefully (writes '[]')."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def tearDown(self):
        """Clean up any files created during tests."""
        files = ["Rectangle.json", "Square.json", "Rectangle.csv", "Square.csv"]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def test_from_json_string(self):
        """Test static method from_json_string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        result = Base.from_json_string(json_str)
        self.assertEqual(result, [{"id": 89, "width": 10, "height": 4}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create_rectangle(self):
        """Test class method create for Rectangle."""
        r = Rectangle(3, 5, 1, 2, 99)
        r_dict = r.to_dictionary()
        r_copy = Rectangle.create(**r_dict)
        self.assertEqual(str(r), str(r_copy))
        self.assertIsNot(r, r_copy)

    def test_create_square(self):
        """Test class method create for Square."""
        s = Square(4, 1, 1, 77)
        s_dict = s.to_dictionary()
        s_copy = Square.create(**s_dict)
        self.assertEqual(str(s), str(s_copy))
        self.assertIsNot(s, s_copy)

    def test_load_from_file_json(self):
        """Test load_from_file method for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        
        list_rects = Rectangle.load_from_file()
        self.assertEqual(len(list_rects), 2)
        self.assertEqual(str(list_rects[0]), str(r1))
        self.assertEqual(str(list_rects[1]), str(r2))

    def test_save_and_load_file_csv(self):
        """Test CSV serialization and deserialization for Rectangle and Square."""
        r1 = Rectangle(4, 5, 1, 2, 10)
        Rectangle.save_to_file_csv([r1])
        
        self.assertTrue(os.path.exists("Rectangle.csv"))
        
        list_rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rects), 1)
        self.assertEqual(str(list_rects[0]), str(r1))

        # Test Square CSV as well
        s1 = Square(3, 2, 1, 20)
        Square.save_to_file_csv([s1])
        self.assertTrue(os.path.exists("Square.csv"))
        
        list_squares = Square.load_from_file_csv()
        self.assertEqual(len(list_squares), 1)
        self.assertEqual(str(list_squares[0]), str(s1))

if __name__ == '__main__':
    unittest.main()
