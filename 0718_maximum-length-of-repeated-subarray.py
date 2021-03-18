"""
最长重复子数组

链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray

给两个整数数组 A 和 B，返回两个数组中公共的、长度最长的子数组的长度。

示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。

提示：
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

解法：
1. 动态规划。
状态：
 - A 的下标 i，B 的下标 j。
 - dp[i][j] 表示以 A[i] 和 B[j] 为尾元素的公共子数组的长度。

状态转移方程：
 - 当 A[i] == B[j] 时，dp[i][j] = dp[i-1][j-1] + 1
 - 当 A[i] != B[j] 时，dp[i][j] = 0

base case：
 - i == 0 或 j == 0 时，若 A[i] == B[j]，则 dp[i][j] = 1。

"""
import unittest
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        动态规划。

        状态：
         - A 的下标 i，B 的下标 j。
         - dp[i][j] 表示以 A[i] 和 B[j] 为尾元素的公共子数组的长度。

        状态转移方程：
         - 当 A[i] == B[j] 时，dp[i][j] = dp[i-1][j-1] + 1
         - 当 A[i] != B[j] 时，dp[i][j] = 0

        base case：
         - i == 0 或 j == 0 时，若 A[i] == B[j]，则 dp[i][j] = 1。
        """
        n, m = len(A), len(B)
        dp: List[List[int]] = [[0 for __ in range(m)] for _ in range(n)]

        # base case
        for i in range(n):
            if A[i] == B[0]:
                dp[i][0] = 1

        for j in range(m):
            if B[j] == A[0]:
                dp[0][j] = 1

        max_len = 0
        for i in range(1, n):
            for j in range(1, m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == "__main__":
    unittest.main()
