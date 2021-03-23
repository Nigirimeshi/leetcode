"""
分割等和子集

链接：https://leetcode-cn.com/problems/partition-equal-subset-sum

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

解法：
1. 动态规划。
问题可转变为 0、1 背包问题，背包大小为数组和除以 2。
数组和为奇数则不可能分割成两个相等子集。

状态：
 - dp[i][j]：前 i 个数字，能否填满 j。
 
状态转移：
 - dp[i][j] =


"""
import unittest
from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        """动态规划。"""
        n = len(nums)
        if n < 2:
            return False

        sum_ = sum(nums)
        # 数组和为奇数时，不可能分割成 2 个相等子集。
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2

        # 最大值比数组和的均值还大，肯定不能分割成 2 个相等子集。
        max_ = max(nums)
        if max_ > target:
            return False

        dp: List[List[bool]] = [[False] * (target + 1) for _ in range(n)]

        # 初始化 dp，dp[i][0] = True。
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                # 背包容量小于当前数字，则不装当前数字，继承上一个数字状态（容量不变）。
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    # 2 种情况：
                    # 1）不装当前数字，那直接继承上一个数字状态。
                    # 2）装当前数字，那得看 j - nums[i] 能不能装下。
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[n - 1][target]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == "__main__":
    unittest.main()
