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

2. 中心扩散法。
子串边界情况：1 或 2 个字符串。
可以枚举每个子串边界情况，并从对应的子串不断从中心向两边扩散，
 - 若两边的字母相同，则可以继续扩散。
 - 若两边的字母不同，则停止扩散，因为在这之后不可能是回文串了。

时间复杂度：O(n^2)
空间复杂度：O(1)

"""
import unittest
from typing import List


class OfficialSolution:
    def longest_palindrome(self, s: str) -> str:
        """动态规划。"""
        n = len(s)
        if n < 2:
            return s

        # 子串起始位置及最大长度。
        begin, max_len = 0, 1

        # 初始化 dp。
        dp = [[False] * n for _ in range(n)]
        # 单个字符一定是回文串，dp[i][i] = True。
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

    def longest_palindrome_2(self, s: str) -> str:
        """
        动态规划。
        
        状态：dp[i][j] 表示 s 下标 [i, j] 的子串是否为回文串。
        状态转移方程：
         - 易知：若字符串去除头尾字符的子串也是回文串，且字符串的头尾字符相等，则该字符串是回文串。
         - dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        初始值：
         - 空字符串是回文串。
         - 单个字符是回文串 dp[i][i] = True。

         时间复杂度：O(n^2)
         空间复杂度：O(n^2)
        """
        n = len(s)
        ans = ''

        dp = [[False] * n for _ in range(n)]
        # 枚举字符串的长度。
        for length in range(n):
            # 枚举字符串的起始位置 i，结束位置 j = i + length。
            for i in range(n):
                j = i + length
                if j >= n:
                    break

                # 单个字符串是回文串。
                if length == 0:
                    dp[i][j] = True
                # 2 个字符的字符串，若 2 字符相等，则为回文串。
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                # 字符大于 2 个的字符串，若其子串是回文串，且其头尾字符相同，则该字符串为回文串。
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

                # 更新最长回文串。
                if dp[i][j] and length + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def longest_palindrome_3(self, s: str) -> str:
        """
        中心扩散法。
        """
    
        def extend(s: str, left: int, right: int) -> List[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return [left + 1, right - 1]
    
        start, end = 0, 0
        for i in range(len(s)):
            # 从单个字符开始扩散。
            left1, right1 = extend(s, i, i)
            # 从 2 个字符开始扩散。
            left2, right2 = extend(s, i, i + 1)
        
            # 更新最长回文子串起始、结束下标。
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_longest_palindrome(self) -> None:
        self.assertEqual(
            'bab',
            self.s.longest_palindrome_2('babad')
        )
        self.assertEqual(
            'bb',
            self.s.longest_palindrome_2('cbbd')
        )
        self.assertEqual(
            'a',
            self.s.longest_palindrome_2('a')
        )
        self.assertEqual(
            'a',
            self.s.longest_palindrome_2('ac')
        )
        self.assertEqual(
            'bb',
            self.s.longest_palindrome_2('cbbd')
        )


if __name__ == '__main__':
    unittest.main()
