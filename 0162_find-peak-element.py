"""
寻找峰值

链接：https://leetcode-cn.com/problems/find-peak-element

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:
输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

示例 2:
输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；或者返回索引 5， 其峰值元素为 6。

说明:
你的解法应该是 O(logN) 时间复杂度的。

我的解题思路：
1. 一次遍历。
从下标 1 遍历到 N - 1，比较左右元素。

时间复杂度：O(N)。不符合题目要求。

官方解法：
1. 线性扫描。
本方法利用了题目给出的两个元素 nums[j] 和 nums[j+1] 不会相等这一事实。
每当我们遇到数字 nums[j]，只需要检查它是否大于下一个元素，即可判断 nums[j] 是否是峰值，可通过下列 3 种情况证明：
1) 情况 1：所有数字以降序排列。这种情况下，第一个元素即为峰值，不需要继续向下判断，也就不用判断 nums[j-1] 的大小。
2) 情况 2：所有数字以升序排列。这种情况下，会一直比较 nums[j] 和 nums[j+1]，没有元素符合，说明处于上坡而非峰值。
   因此，只需返回末尾元素作为峰值。同样不需要比较 nums[j-1] 的大小。
3) 情况 3：峰值在中间某处。这种情况下，类似情况 2，当满足条件 nums[j] > nums[j+1] 即为峰值，同样不需要判断 nums[j-1]。

时间复杂度：O(N)。
空间复杂度：O(1)。

2. 递归二分查找。

时间复杂度：O(logN)。每一次都将搜索空间减半。
空间复杂度：O(logN)。每一次都将搜索空间减半。递归树的深度为 O(logN)。

3. 迭代二分查找。

时间复杂度：O(logN)。
空间复杂度：O(1)。
"""
import unittest
from typing import List


class OfficialSolution:
    def find_peak_element(self, nums: List[int]) -> int:
        """线性扫描。"""
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
        return n - 1

    def find_peak_element_2(self, nums: List[int]) -> int:
        """递归二分查找。"""
        return self.binary_search(nums, 0, len(nums) - 1)

    def binary_search(self, nums: List[int], left, right: int) -> int:
        """二分查找。"""
        if left == right:
            return left

        mid = (left + right) // 2
        # 大于下一位元素，说明处于下坡，则去 [left, mid] 区间搜索。
        if nums[mid] > nums[mid + 1]:
            return self.binary_search(nums, left, mid)

        # 小于下一位元素，说明处于上坡，则去 [mid+1, right] 区间搜索。
        return self.binary_search(nums, mid + 1, right)

    def find_peak_element_3(self, nums: List[int]) -> int:
        """迭代二分查找。"""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_find_peak_element(self) -> None:
        self.assertEqual(
            self.s.find_peak_element([1, 2, 3, 1]),
            2,
        )
        self.assertEqual(
            self.s.find_peak_element([1]),
            0,
        )


if __name__ == '__main__':
    unittest.main()
