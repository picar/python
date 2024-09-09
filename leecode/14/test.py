import unittest
from longest_common_prefix import Solution


class TestRomanSolution(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(Solution().longestCommonPrefix(
            [
                "flower",
                "flow",
                "flight"
            ]),
            "fl"
        )
    def test_solution_2(self):
        self.assertEqual(Solution().longestCommonPrefix(
            [
                "dog",
                "racecar",
                "car"
            ]), 
            ""
        )