import unittest
from app import largest_palindrome_in_range


class TestPalindrome(unittest.TestCase):
    def test_largest_palindrome_in_range(self):
        # Test cases
        self.assertEqual(largest_palindrome_in_range(100, 200), 191)
        self.assertEqual(largest_palindrome_in_range(200, 300), 292)
        self.assertEqual(largest_palindrome_in_range(500, 600), 595)
        self.assertEqual(largest_palindrome_in_range(0, 100), 99)
        self.assertEqual(largest_palindrome_in_range(999, 1000), -1)
        self.assertEqual(largest_palindrome_in_range(1000, 2000), 1991)
        self.assertEqual(largest_palindrome_in_range(2000, 3000), 2992)
        self.assertEqual(largest_palindrome_in_range(5000, 6000), 5995)
        self.assertEqual(largest_palindrome_in_range(123, 125), -1)
        self.assertEqual(largest_palindrome_in_range(100, 101), -1)


if __name__ == '__main__':
    unittest.main()
