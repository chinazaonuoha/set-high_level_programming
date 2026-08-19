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
        self.assertEqual(r2.id, 98)
        self.assertEqual(r3.id, r1.id + 1)

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

    # --- Validation Tests ---

    def test_width_type_validation(self):
        """Test TypeError for invalid width types."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_height_type_validation(self):
        """Test TypeError for invalid height types."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_x_type_validation(self):
        """Test TypeError for invalid x types."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "0", 1)

    def test_y_type_validation(self):
        """Test TypeError for invalid y types."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "1")

    def test_width_value_validation(self):
        """Test ValueError for invalid width values (<= 0)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)

    def test_height_value_validation(self):
        """Test ValueError for invalid height values (<= 0)."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_value_validation(self):
        """Test ValueError for invalid x values (< 0)."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)

    def test_y_value_validation(self):
        """Test ValueError for invalid y values (< 0)."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)
   
    def test_area(self):
        """Test the area calculation of the Rectangle."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 1)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test the display method of the Rectangle."""
        r1 = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        self.assertEqual(r1.display(), expected_output)

        r2 = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        self.assertEqual(r2.display(), expected_output)

    def test_str_representation(self):
        """Test the __str__ method output format."""
        r = Rectangle(4, 6, 2, 1, 12)
        expected_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_str)

    def test_str_with_defaults(self):
        """Test __str__ method with default x, y, and generated id."""
        r = Rectangle(5, 10)
        self.assertTrue(str(r).startswith("[Rectangle]"))
        self.assertIn("0/0 - 5/10", str(r))
    
    def test_display_with_x_and_y(self):
        """Test the display method with x and y offsets."""
        import sys
        from io import StringIO
        r = Rectangle(2, 3, 2, 1)
        expected_output = "\n  ##\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__ 
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_method(self):
        """Test the update method with positional arguments."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_to_dictionary(self):
        """Test the dictionary representation of a Rectangle."""
        r = Rectangle(5, 10, 2, 1, 9)
        r_dict = r.to_dictionary()
        expected_dict = {
            "id": 9,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 1
        }
        self.assertEqual(r_dict, expected_dict)
        self.assertIsInstance(r_dict, dict)


if __name__ == '__main__':
    unittest.main()

