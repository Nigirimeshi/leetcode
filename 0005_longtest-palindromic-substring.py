"""
最长回文子串

链接：https://leetcode-cn.com/problems/longest-palindromic-substring

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

我的解题思路：
1. 动态规划。
特征：
1) 字符串中只出现 1 次的字符不存在回文子串；

官方解法：
1. 动态规划。
“回文” 天然具有状态转移性质 --- 一个回文去掉两头后，剩下的部分依然是回文。

回文串的定义：
1) 如果一个字符串头尾不相同，那一定不是回文串；
2) 如果一个字符串头尾相同，才有必要继续判断：
2.1) 如果里面的字符串是回文，整体就是回文串；
2.2) 如果里面的字符串不是回文，整体就不是回文串。
即：在头尾字符相同的情况下，里面的子串决定了整个字符串的回文性质，这就是状态转移。
因此可以把 “状态” 定义为 “原字符串的一个子串是否为回文”。

动态规划过程：
1) 定义状态：dp[i][j] 表示子串 s[i...j] 是否为回文子串。

2) 状态转移方程：dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]。

3) 边界条件：要使表达式 [i+1, j-1] 不构成区间，则 (j-1) - (i+1) + 1 < 2，可得 j - i < 3。

4) 初始化：单个字符一定是回文串，所以把 dp 表格对角线先初始化为 true，即 dp[i][i] = true。

5) 输出：只要一得到 dp[i][j] = true，就记录子串的长度和起始位置，没有必要截取字符串。

时间复杂度：O(N^2)。
空间复杂度：，二维 dp 问题，一个状态得用二维有序数对表示，因此空间复杂度是 O(N^2)。

"""
import unittest


class OfficialSolution:
    def longest_palindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # 子串起始位置及最大长度。
        begin, max_len = 0, 1

        # 初始化 dp。
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 注意：左下角先填。
        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][j] == true，就表示子串 s[i...j] 是回文，此时需要记录回文长度及起始位置。
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = TestOfficialSolution()

    def test_longest_palindrome(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
