from unittest import TestCase
from ex4 import build_school


class TestEx4(TestCase):
    def test_with_1_2_3(self):
        n = 3
        points = [1, 2, 3]

        self.assertEqual(build_school(n, points), 2)

    def test_with_1_2_3_4(self):
        n = 4
        points = [1, 2, 3, 4]

        self.assertIn(build_school(n, points), [2, 3])

    def test_with_1_0_1(self):
        n = 3
        points = [-1, 0, 1]

        self.assertEqual(build_school(n, points), 0)

    def test_with_2_4_6(self):
        n = 3
        points = [2, 4, 6]

        self.assertEqual(build_school(n, points), 4)

    def test_with_1_3_6(self):
        n = 3
        points = [1, 3, 6]

        self.assertEqual(build_school(n, points), 3)

    def test_with_0_1_7(self):
        n = 3
        points = [0, 1, 7]

        self.assertEqual(build_school(n, points), 1)

    def test_with_0_1_3_4_7(self):
        n = 5
        points = [0, 1, 3, 4, 7]

        self.assertEqual(build_school(n, points), 3)

    def test_with_0_1_5_6_7(self):
        n = 5
        points = [0, 1, 5, 6, 7]

        self.assertEqual(build_school(n, points), 5)

    def test_with_1_0_1_7(self):
        n = 5
        points = [-1, 0, 1, 7]

        self.assertIn(build_school(n, points), [0, 1])

    def test_with_0_1(self):
        n = 2
        points = [0, 1]

        self.assertIn(build_school(n, points), [0, 1])

    def test_with_0_1_2_3_4_5_6_7_8_9_10(self):
        n = 11
        points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(build_school(n, points), 5)

    def test_with_0_1_2_5_6_7_8_9_10(self):
        n = 9
        points = [0, 1, 2, 5, 6, 7, 8, 9, 10]

        self.assertEqual(build_school(n, points), 6)
