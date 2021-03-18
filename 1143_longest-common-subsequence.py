"""
最长公共子序列

链接：https://leetcode-cn.com/problems/longest-common-subsequence

标签：动态规划

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3:
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

提示:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。

官方解法：
1. 动态规划。
时间复杂度：O(m*n)
空间复杂度：O(m*n)

"""
import unittest
from typing import List


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """动态规划。"""
        n, m = len(text1), len(text2)
        if n * m == 0:
            return 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def longest_common_subsequence_2(self, text1: str, text2: str) -> int:
        """动态规划。"""
        n, m = len(text1), len(text2)
        dp: List[List[int]] = [[0 for __ in range(m)] for _ in range(n)]

        # base case
        if text1[0] == text2[0]:
            dp[0][0] = 1

        # 初始化第一列。
        for i in range(1, n):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        # 初始化第一行。
        for j in range(1, m):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        # 状态转移。
        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_longest_common_subsequence(self) -> None:
        self.assertEqual(
            self.s.longest_common_subsequence("abcde", "ace"),
            3,
        )
        self.assertEqual(
            self.s.longest_common_subsequence("", ""),
            0,
        )
        self.assertEqual(
            self.s.longest_common_subsequence("abc", "abc"),
            3,
        )


if __name__ == "__main__":
    unittest.main()
