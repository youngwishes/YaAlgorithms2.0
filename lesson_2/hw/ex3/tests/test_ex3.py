from unittest import TestCase
from ex3 import palindrome


class TestEx3(TestCase):
    def test_with_a(self):
        s = 'a'
        self.assertEqual(palindrome(s), 0)

    def test_with_ab(self):
        s = 'ab'
        self.assertEqual(palindrome(s), 1)

    def test_with_cognitive(self):
        s = 'cognitive'
        self.assertEqual(palindrome(s), 4)

    def test_with_cbdfc(self):
        s = 'cbdfc'
        self.assertEqual(palindrome(s), 1)
