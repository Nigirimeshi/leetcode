"""
最大子序和

链接：https://leetcode-cn.com/problems/maximum-subarray

给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

我的解题思路：
1. 动态规划。

官方解法：
1. 动态规划。
dp(i) 为连续子数组的和。
dp[i] = max(dp[i-1] + dp[i], dp[i])

时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest
from typing import List


class OfficialSolution:
    def max_sub_array(self, nums: List[int]) -> int:
        pre = 0
        max_value = nums[0]
        for num in nums:
            pre = max(pre + num, num)
            max_value = max(max_value, pre)
        return max_value


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_max_sub_array(self) -> None:
        self.assertEqual(
            self.s.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6,
        )


if __name__ == '__main__':
    unittest.main()
