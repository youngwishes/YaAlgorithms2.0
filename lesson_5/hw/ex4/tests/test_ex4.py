from unittest import TestCase
from main import check_str


class TestEx4(TestCase):
    def test_1(self):
        self.assertEqual(check_str('()'), "YES")

    def test_2(self):
        self.assertEqual(check_str('(()'), "NO")

    def test_3(self):
        self.assertEqual(check_str('(())'), "YES")

    def test_4(self):
        self.assertEqual(check_str('(()()())'), "YES")

    def test_5(self):
        self.assertEqual(check_str('()()(()()'), "NO")

    def test_6(self):
        self.assertEqual(check_str('()()(()())'), "YES")

    def test_7(self):
        self.assertEqual(check_str('()()('), "NO")

    def test_8(self):
        self.assertEqual(check_str('('), "NO")

    def test_9(self):
        self.assertEqual(check_str(')'), "NO")

    def test_10(self):
        self.assertEqual(check_str('(('), "NO")

    def test_11(self):
        self.assertEqual(check_str('))'), "NO")

    def test_12(self):
        self.assertEqual(check_str('()())('), "NO")

    def test_13(self):
        self.assertEqual(check_str(')('), 'NO')
