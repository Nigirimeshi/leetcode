"""
递增的三元子序列

链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k, 且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true；否则返回 false。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:
输入: [1,2,3,4,5]
输出: true

示例 2:
输入: [5,4,3,2,1]
输出: false

我的解题思路：
1. 双指针。
用 small，mid 分别表示最小值和中间值，遍历数组。
若数字小于 small，则替换 small；
若大于 small 小于 mid，则替换 mid，
若大于 mid，说明满足题目条件（长度为 3 的递增序列）。

"""
import unittest
import math
from typing import List


class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        small, mid = math.inf, math.inf
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_increasing_triplet(self) -> None:
        self.assertTrue(self.s.increasing_triplet([1, 2, 3, 4, 5]))
        self.assertFalse(self.s.increasing_triplet([5, 4, 3, 2, 1]))
        self.assertTrue(self.s.increasing_triplet([5, 1, 5, 5, 2, 5, 4]))
        self.assertFalse(self.s.increasing_triplet([0, 4, 2, 1, 0, -1, -3]))
        self.assertFalse(self.s.increasing_triplet(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
