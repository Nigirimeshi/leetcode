"""
摆动排序 II

链接：https://leetcode-cn.com/problems/wiggle-sort-ii

给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:
输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]

示例 2:
输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

官方解法：
1. 排序。
先排序数组，然后将数组一分为二并反转，最后将分割后的数组交替遍历，组合成新数组。
时间复杂度：O(NlogN)
空间复杂度：O(N)


"""
import unittest
from typing import List


class Solution:
    def wiggle_sort(self, nums: List[int]) -> None:
        """
        排序。
        """
        nums.sort()
        s = len(nums) - (len(nums) // 2)
        a = nums[:s][::-1]
        b = nums[s:][::-1]
        nums.clear()
        for i in range(s):
            nums.append(a[i])
            if i < len(b):
                nums.append(b[i])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_wiggle_sort(self) -> None:
        nums = [1, 5, 1, 1, 6, 4]
        self.s.wiggle_sort(nums)
        self.assertListEqual(
            nums,
            [1, 6, 1, 5, 1, 4],
        )


if __name__ == '__main__':
    unittest.main()
