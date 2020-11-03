"""
乘积最大子数组

链接：https://leetcode-cn.com/problems/maximum-product-subarray

标签：数组

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

我的解题思路：
1. 暴力迭代。（提交超时）

官方解法：
1. 动态规划。
注意负负得正，没准当前是最大值，下一个值为负数，相乘就变成最小值了，该题需要维护最大值和最小值。
dp_max[i] = max(nums[i-1], dp_max[i-1] * nums[i], dp_min[i] * nums[i])
dp_min[i] = min(nums[i-1], dp_max[i-1] * nums[i], dp_min[i] * nums[i])

时间复杂度：O(n)
空间复杂度：O(1)

"""
from typing import List
import unittest


class Solution:
    def max_product(self, nums: List[int]) -> int:
        """暴力迭代。"""
        size = len(nums)
        ans = nums[0]
        for i in range(size):
            tmp = nums[i]
            products = [tmp]
            for j in range(i + 1, size):
                products.append(tmp * nums[j])
                tmp *= nums[j]
            ans = max(ans, max(products))
        return ans


class OfficialSolution:
    def max_product(self, nums: List[int]) -> int:
        """动态规划。"""
        dp_max = nums[0]
        dp_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            _max, _min = dp_max, dp_min
            dp_max = max(nums[i], _max * nums[i], _min * nums[i])
            dp_min = min(nums[i], _max * nums[i], _min * nums[i])
            ans = max(dp_max, ans)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_max_product(self):
        self.assertEqual(
            self.s.max_product([2, 3, -2, 4]),
            6,
        )
        self.assertEqual(
            self.s.max_product([-4, -3, -2]),
            12,
        )


if __name__ == '__main__':
    unittest.main()
