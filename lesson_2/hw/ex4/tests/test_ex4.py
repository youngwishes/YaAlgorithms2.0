from main import check_bench
from unittest import TestCase


class TestEx4(TestCase):
    def test_with_2(self):
        self.assertEqual(check_bench('2 1', '1'), 1)

    def test_with_1(self):
        self.assertEqual(check_bench('1 1', '0'), 0)

    def test_with_0_2(self):
        self.assertEqual(check_bench('5 2', '0 1 2 3 4 5'), 2)

    def test_with_1_4_8_11(self):
        self.assertSequenceEqual(check_bench('13 4', '0 1 2 3 4 5 7 8 9 10 11 12 13'), (5, 7))

    def test_with_1_6_8_11_12_13(self):
        self.assertSequenceEqual(check_bench('14 6', '1 6 8 11 12 13'), (6, 8))

    def test_with_with_0_2_3(self):
        self.assertEqual(check_bench('5 3', '0 2 3'), 2)

    def test_with_with_0_3_6(self):
        self.assertEqual(check_bench('6 3', '0 3 6'), 3)

    def test_with_with_0_8_12(self):
        self.assertSequenceEqual(check_bench('14 3', '0 8 12'), [0, 8])

    def test_with_0_7_12(self):
        self.assertEqual(check_bench('14 3', '0 7 12'), 7)

    def test_with_with_0_10(self):
        self.assertSequenceEqual(check_bench('10 2', '0 10'), [0, 10])

    def test_with_with_0_9(self):
        self.assertSequenceEqual(check_bench('9 2', '0 9'), [0, 9])

    def test_with_with_0_1_9(self):
        self.assertSequenceEqual(check_bench('9 3', '0 1 9'), [1, 9])

    def test_with_with_0_5_9(self):
        self.assertEqual(check_bench('9 3', '0 4 9'), 4)

    def test_with_2(self):
        self.assertEqual(check_bench('5 1', '2'), 2)

    def test_with_0_3(self):
        self.assertEqual(check_bench('6 2', '0 1 2 3 4 5 6'), 3)


