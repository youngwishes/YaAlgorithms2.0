from unittest import TestCase


def main(m, lrs_list):
    main_set = set(range(0, m + 1))
    segments = []
    for left, right in lrs_list:

        if left == right == 0:
            break
        if left <= 5000 and right >= 0:

            if left < 0:
                temp_l = 0
            else:
                temp_l = left

            segments.append((right - temp_l, left, right))

    segments.sort(reverse=True)
    count = 0
    ans = []
    for d, l, r in segments:
        s = set(range(l, r + 1))
        if main_set.intersection(s):
            main_set.difference_update(s)
            count += 1
            ans.append((l, r))

    if not main_set:
        ans.sort()
        return count, ans
    else:
        return "No solution"


class TestEx3(TestCase):
    def test_1(self):
        self.assertEqual(main(1, [(-1, 0), (-5, -3), (2, 5), (0, 0)]), "No solution")

    def test_2(self):
        self.assertEqual(main(1, [(-1, 0), (0, 1), (0, 0)]), (1, [(0, 1)]))

    def test_3(self):
        self.assertEqual(main(10, [(-5, 5), (2, 4), (6, 8), (7, 10)]), (3, [(-5, 5), (6, 8), (7, 10)]))

    def test_4(self):
        self.assertEqual(main(10, [(-100, 10), (0, 4), (6, 8), (7, 10)]), (1, [(-100, 10)]))

    def test_5(self):
        self.assertEqual(main(10, [(0, 5), (1, 6), (2, 7), (3, 8), (6, 8), (9, 10)]), (3, [(0, 5), (6, 8), (9, 10)]))
