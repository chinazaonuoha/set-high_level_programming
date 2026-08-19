import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test suite for the Square class."""

    def test_square_str_representation(self):
        """Test the overloaded __str__ output for Square."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_is_rectangle(self):
        """Test that Square is an instance of Rectangle and object."""
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)

    def test_initialization_basic(self):
        """Test basic initialization with just a size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_square_size_only(self):
        """Test creating a Square with only size (width and height validation)."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_area(self):
        """Test that the area() method correctly calculates the area of a Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)
        s2 = Square(10)
        self.assertEqual(s2.area(), 100)
        
    def test_square_to_dictionary(self):
        """Test the dictionary representation of a Square."""
        s = Square(5, 2, 1, 12)
        s_dict = s.to_dictionary()
        expected_dict = {
            "id": 12,
            "size": 5,
            "x": 2,
            "y": 1
        }
        self.assertEqual(s_dict, expected_dict)
        self.assertIsInstance(s_dict, dict)