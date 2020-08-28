from django.test import TestCase
from .calc import add_numbers, subtract_numbers


class CalcTests(TestCase):
    # Test functions need to begin with test_
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add_numbers(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract_numbers(5, 11), 6)