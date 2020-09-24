"""
无重复字符的最长子串

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters

给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

我的解题思路：
1. 滑动窗口（双指针）。
特值：
1) s 长度为 0，返回 0。
2) s 长度为 1，返回 1。

遍历字符串 s，用字典记录每个字符 c 及索引位置，当出现重复字符时，移动指针至重复字符的下一字符位置，并比较最大子串长度，重新记录字典。

"""
import unittest


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        length = 0
        cache = {}

        i = 0
        while i <= len(s) - 1:
            c = s[i]
            # 记录尚未重复的字符及位置。
            if not cache.__contains__(c):
                cache[c] = i
                i += 1
                continue

            # 存在重复字符，计算当前最大长度。
            length = max(length, len(cache))
            # 移动指针位置至重复字符的下一字符。
            i = cache[c] + 1
            # 重新记录不重复元素字典。
            cache = {s[i]: i}
            i += 1

        length = max(length, len(cache))
        return length


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_length_of_longest_substring(self) -> None:
        self.assertEqual(
            self.s.length_of_longest_substring(''),
            0,
        )
        self.assertEqual(
            self.s.length_of_longest_substring('a'),
            1,
        )
        self.assertEqual(
            self.s.length_of_longest_substring('abcabcbb'),
            3,
        )
        self.assertEqual(
            self.s.length_of_longest_substring('bbbbb'),
            1,
        )
        self.assertEqual(
            self.s.length_of_longest_substring('pwwkew'),
            3,
        )
        self.assertEqual(
            self.s.length_of_longest_substring('dvdf'),
            3,
        )


if __name__ == '__main__':
    unittest.main()
