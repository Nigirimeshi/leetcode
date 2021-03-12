"""
字符串的排列

链接：https://leetcode-cn.com/problems/permutation-in-string

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例 2：
输入: s1= "ab" s2 = "eidboaoo"
输出: False

提示：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

解法：
1. 滑动窗口。

"""
import unittest
from collections import defaultdict
from typing import Dict


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """滑动窗口。"""
        need: Dict[str, int] = defaultdict(int)
        window: Dict[str, int] = defaultdict(int)

        for c in s1:
            need[c] += 1

        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while (right - left) >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_check_inclusion(self) -> None:
        self.assertTrue(self.s.check_inclusion("", "a"))
        self.assertTrue(self.s.check_inclusion("abc", "asdfasdfbacdew"))
        self.assertFalse(self.s.check_inclusion("abc", "adbc"))


if __name__ == "__main__":
    unittest.main()
