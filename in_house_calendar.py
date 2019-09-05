# Your company built an in-house calendar tool called HiCal.
# You want to add a feature to see the times in a day when everyone is available.
import unittest

def merge_ranges(in_list: list):
    l = []

    for item in in_list:
        print(item)
        in_bound = False
        for idx, f_item in enumerate(l):
            # if item falls in f_item then merge lower and upper bound value of them
            if check_bound(item, f_item):
                in_bound = True
                l[idx] = merge_bound(item, f_item)
                print(l)

        # else add item as it is in f_item
        if in_bound == False:
            l.append(item)
    l.sort(key = lambda x: x[0])
    print('Result:', l)
    return l

def merge_bound(item, f_item):
    t = f_item + item
    new_t = (min(t), max(t))
    return new_t

def check_bound(item, f_item):
    in_bound = False
    if (
        (f_item[0] <= item[0] and item[0] <= f_item[1])
        or (f_item[0] <= item[1] and item[1] <= f_item[1])
        or (item[0] <= f_item[0] and f_item[0] <= item[1])
        or (item[0] <= f_item[1] and f_item[1] <= item[1])
    ):
        in_bound = True
    return in_bound

# input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# input = [(1, 2), (2, 3)]
# input = [(1, 5), (2, 3)]
# input = [(1, 10), (2, 6), (3, 5), (7, 9)]
# ouput = [(0, 1), (3, 8), (9, 12)]
# execute funtion
# merge_ranges(input)

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
