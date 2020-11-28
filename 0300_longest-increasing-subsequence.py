"""
最长上升子序列

标签：动态规划、贪心

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

进阶:
你能将算法的时间复杂度降低到O(n log n) 吗?

官方解法：
1. 动态规划。
状态定义：dp[i] 为第 i 个元素的最长上升子序列长度。
初始值：所有元素最小子序列长度为 1（既自己）。
状态转移方程：dp[i] = max(dp[i], dp[j] + 1)；j 的范围为 [0, i)。
 - 当 nums[i] > nums[j] 时，说明 nums[i] 可接在 nums[j] 之后，是递增子序列的一部分。
结果：即 dp 中最大的值。

空间复杂度：O(N^2)。
时间复杂度：O(N)。

2. 动态规划 + 贪心 + 二分查找。
"""
from typing import List
import unittest


class Solution:
    def length_of_LIS(self, nums: List[int]) -> int:
        """
        动态规划。
        状态定义：dp[i] 表示 nums 前 i 个数字的最长子序列长度。
        转移方程：dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
        初始状态：dp[i] = 1，每个数字自身构成子序列，长度为 1。
        返回值：max(dp)

        时间复杂度：O(N^2)，遍历 dp 列表要 O(N)，计算每个 dp[i] 要 O(N)。
        空间复杂度：O(N)。
        """
        if not nums:
            return 0
        
        n = len(nums)
        # 初始化 dp。
        dp = [1] * n
        for i in range(n):
            # 找出前 i 个 dp 中，小于 nums[i] 的最长子序列长度，并加 1。
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_length_of_LIS(self) -> None:
        self.assertEqual(
            self.s.length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]),
            4,
        )
        self.assertEqual(
            self.s.length_of_LIS([10, 9, 2, 5, 3, 4]),
            3,
        )


if __name__ == '__main__':
    unittest.main()
