from unittest import TestCase
from main import main
from solution_with_tl import with_tl


class TestEx4(TestCase):
    def test_1_main(self):
        n = 5
        m = 5
        points = [1, 3, 5, 7, 9]
        lrs = [(0, 5), (0, 6), (0, 7), (2, 4), (1, 9)]

        ans = [3, 3, 4, 1, 5]
        self.assertEqual(main(n, m, points, lrs), ans)

    def test_1_with_tl(self):
        n = 5
        m = 5
        points = [1, 3, 5, 7, 9]
        lrs = [(0, 5), (0, 6), (0, 7), (2, 4), (1, 9)]

        ans = [3, 3, 4, 1, 5]
        self.assertEqual(with_tl(n, m, points, lrs), ans)

    def test_2_with_main(self):
        n = 1
        m = 5
        points = [1]
        lrs = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4)]

        ans = [1, 1, 1, 1, 0]
        self.assertEqual(main(n, m, points, lrs), ans)

    def test_2_with_tl(self):
        n = 1
        m = 5
        points = [1]
        lrs = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4)]

        ans = [1, 1, 1, 1, 0]
        self.assertEqual(with_tl(n, m, points, lrs), ans)

    def test_3_with_main(self):
        n = 2
        m = 5
        points = [1, 999]
        lrs = [(0, 1), (0, 2), (0, 3), (1, 1000), (1, 1)]

        ans = [1, 1, 1, 2, 1]
        self.assertEqual(main(n, m, points, lrs), ans)

    def test_3_with_tl(self):
        n = 2
        m = 5
        points = [1, 999]
        lrs = [(0, 1), (0, 2), (0, 3), (1, 1000), (1, 1)]

        ans = [1, 1, 1, 2, 1]
        self.assertEqual(with_tl(n, m, points, lrs), ans)

    def test_4_with_main(self):
        n = 5
        m = 3
        points = [0, 10, 100]
        lrs = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 3)]

        ans = [1, 1, 0, 0, 0]
        self.assertEqual(main(n, m, points, lrs), ans)

    def test_4_with_tl(self):
        n = 5
        m = 3
        points = [0, 10, 100]
        lrs = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 3)]

        ans = [1, 1, 0, 0, 0]
        self.assertEqual(with_tl(n, m, points, lrs), ans)