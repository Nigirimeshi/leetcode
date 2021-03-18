"""
环形数组的最大和

链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray

给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。

（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）

此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。

（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

示例 1：
输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

示例 2：
输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

示例 3：
输入：[3,-1,2,-1]
输出：4
解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4

示例 4：
输入：[3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3

示例 5：
输入：[-2,-3,-1]
输出：-1
解释：从子数组 [-1] 得到最大和 -1

提示：
-30000 <= A[i] <= 30000
1 <= A.length <= 30000

解法：
1. 分类讨论。

存在 2 种情况：
1）子数组的最大和在 A 内，不包括环形，那么问题就变为求 A 内的子数组的最大和，用 dp 即可：
   dp[i] = max(dp[i-1] + A[i], A[i])
2）子数组的最大和包括环形区域，也就是说：子数组一定包括 A[0] 和 A[-1]，
   那么只需求出 A[1:-1] 内子数组的最大和即可，
   问题可以进一步转化为找出 A[1:-1] 内子数组的最小和 min_sum，并用 sum(A) - min_sum 即可。
"""
import unittest
from typing import List


class Solution:
    def max_subarray_sum_circular(self, A: List[int]) -> int:
        """动态规划 - 分类讨论。"""
        # 找 A 中子数组的最大和。
        max_sum = curr = float("-inf")
        for num in A:
            curr = max(curr + num, num)
            max_sum = max(max_sum, curr)

        # 找 A[1:-1] 中子数组的最小和。
        min_sum = curr = float("inf")
        for num in A[1:-1]:
            curr = min(curr + num, num)
            min_sum = min(min_sum, curr)

        # 返回 2 种情况中的较大值。
        return max(max_sum, sum(A) - min_sum)


class Case:
    def __init__(self, A: List[int], want: int):
        self.A = A
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_max_subarray_sum_circular(self) -> None:
        test_cases: List[Case] = [
            Case(A=[1, -2, 3, -2], want=3),
            Case(A=[5, -3, 5], want=10),
            Case(A=[3, -1, 2, -1], want=4),
            Case(A=[3, -2, 2, -3], want=3),
            Case(A=[-2, -3, -1], want=-1),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.max_subarray_sum_circular(tc.A))


if __name__ == "__main__":
    unittest.main()
