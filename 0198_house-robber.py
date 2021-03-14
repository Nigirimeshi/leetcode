"""
打家劫舍

链接：https://leetcode-cn.com/problems/house-robber

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400

我的解题思路：
1. 动态规划。
状态转移方程：dp[i] = nums[i] + max(nums[i-2], nums[i-3])  {i >= 3}


官方解法：
1. 动态规划。
只有一间房屋时，则偷该房屋，得到的即最高金额。
有两件房屋时，由于房屋相邻，不能连续偷窃，只能偷其中金额较多的。假设 k 为房屋数量，由此可得边界条件：
{
    dp[0] = nums[0];                (k = 1)
    dp[1] = max(nums[0], nums[1])   (k = 2)
}

对于 k > 2 时，有以下情况：
1) 偷窃第 k 间，那么就不能偷连续的第 k - 1 间，偷窃总金额为前 k - 2 间房屋的最高总金额与第 k 间房屋的金额之和。
2) 不偷第 k 间，那么偷窃最高总金额为前 k - 1 间房屋的最高总金额。

可得状态转移方程： dp[i] = max(dp[i-2] + nums[i], dp[i-1])

时间复杂度：O(n)
空间复杂度：O(n)

2. 动态规划（优化空间）。
时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """动态规划。"""
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        ans = [0] * size
        ans[0:2] = nums[0:2]
        for i in range(2, size):
            prev_sum = ans[i - 2]
            if i - 3 >= 0:
                prev_sum = max(prev_sum, ans[i - 3])
            ans[i] = nums[i] + prev_sum

        return max(ans[size - 1], ans[size - 2])


class OfficialSolution:
    def rob(self, nums: List[int]) -> int:
        """动态规划。"""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

    def rob_2(self, nums: List[int]) -> int:
        """动态规划（优化空间）。"""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        return second


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_rob_2(self) -> None:
        self.assertEqual(
            self.s.rob_2([1, 2, 3, 1]),
            4,
        )
        self.assertEqual(
            self.s.rob_2([1, 1]),
            1,
        )


if __name__ == "__main__":
    unittest.main()
