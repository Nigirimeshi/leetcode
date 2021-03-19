"""
正则表达式匹配

链接：https://leetcode-cn.com/problems/regular-expression-matching

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串 s 的，而不是部分字符串。

示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。
因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false

提示：
0 <= s.length <= 20
0 <= p.length <= 30
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符

解法：
1. 动态规划。
基本思想：
 - 从 s[:1] 和 p[:1] 是否匹配开始判断，每次添加一个字符并判断是否匹配，直到添加完整个字符串 s 和 p。
 - 假设 s[:i] 和 p[:j] 可以匹配，那么下一次就需要判断 2 种状态：
   1. 添加 1 个字符 s(i+1) 后能否匹配？
   2. 添加 1 个字符 p(i+1) 后能否匹配？
 - 因此，共有 m * n 种状态。
 - 此外，需要根据 “普通字符”，“.”，“*” 做出不同的状态转移。
 
状态：dp[i][j] 代表 s 的前 i 个字符串和 p 的前 j 的字符串能否匹配。

状态转移：
 - 注意：dp[0][0] 是空字符串，为 True；另外 dp[i][j] 对应添加的字符是 s[i-1] 和 p[j-1]。
 - 当 p[j-1] = '*' 时，以下任一条件成立时，dp[i][j] 为 True：
    - 当 dp[i][j-2] = True 时：即把 “p[j-2]*” 看作出现 0 次时，能否匹配。
    - 当 dp[i-1][j] = True 且 s[i-1] = p[j-2] 时：即让 p[j-2] 多出现 1 次时，能否匹配。
    - 当 dp[i-1][j] = True 且 p[j-2] = '.' 时：即让 '.' 多出现 1 次时，能否匹配。
 - 当 p[j-1] != '*' 时，以下任一条件成立时，dp[i][j] 为 True：
    - 当 dp[i-1][j-1] = True 且 s[i-1] = p[j-1] 时：即之前的字符都匹配，当前的字符相同。
    - 当 dp[i-1][j-1] = True 且 p[j-1] = '.' 时：即之前的字符都匹配，当前的 “.” 可匹配任一字符。
    
初始值：需要初始化首行。
 - dp[0][0] = True，即 2 个空字符串能够匹配。
 - 当 dp[0][j-2] = True 且 p[j-1] = '*' 时，dp[0][j] = True，相当于 p 的奇数位下标一直是 '*'，p 可以一直当作一个空字符串。
 
返回值：dp 矩阵右下角的值，代表 s 和 p 能否匹配。
"""
import unittest
from typing import List


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        """动态规划。"""
        s_len, p_len = len(s), len(p)

        # 初始化 dp。
        # 注意：dp[i][j] 对应 s[i-1] 和 p[j-1] 前的字符串能否匹配。
        dp: List[List[bool]] = [
            [False for __ in range(p_len + 1)] for _ in range(s_len + 1)
        ]
        # 2 个空字符串能够匹配。
        dp[0][0] = True

        # 初始化首行，避免后续判断时越界。
        # 若 p 的偶数位下标全是 '*'，可以将 p 视为空字符串。
        # 例如：p = 'a*b*c*' 能够和空字符串匹配。
        for j in range(2, p_len + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                # 当 p[j-1] = '*’ 时。
                if p[j - 1] == "*":
                    # 把 p[j-1]* 当作空字符的话，能否匹配。
                    # 例如：s = 'a' 和 p = 'ab*' 能够匹配。
                    if dp[i][j - 2]:
                        dp[i][j] = True

                    # p[j-2] 多一次的话，能否匹配。
                    # 例如：s = 'aa' 和 p = 'a*' 能够匹配。
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True

                    # p[j-2] 是 '.'，多一次的话，能否匹配。
                    # 例如：s = 'ab' 和 p = 'a.*' 能够匹配。
                    elif dp[i - 1][j] and p[j - 2] == ".":
                        dp[i][j] = True

                # 当 p[i-1] != '*' 时。
                else:
                    # 之前的字符串都匹配，且当前遍历到的字符也相同。
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True

                    # 之前的字符串都匹配，且当前 p[j-1] 为 '.'，可以充当任一字符，相当于匹配 s[i-1]。
                    elif dp[i - 1][j - 1] and p[j - 1] == ".":
                        dp[i][j] = True

        return dp[-1][-1]


class Case:
    def __init__(self, s: str, p: str, want: bool):
        self.s = s
        self.p = p
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_match(self):
        test_cases: List[Case] = [
            Case("", ".*", True),
            Case("aa", "a", False),
            Case("aa", "a*", True),
            Case("ab", ".*", True),
            Case("aab", "c*a*b", True),
            Case("mississippi", "mis*is*p*.", False),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.is_match(tc.s, tc.p))


if __name__ == "__main__":
    unittest.main()
