"""
给定一个整数数组，判断是否存在重复元素。

链接：https://leetcode-cn.com/problems/contains-duplicate

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

我的解题思路：
1. 集合。
去除重复元素，判断集合和原数组大小。

2. 排序。
若存在重复元素，排序后它们应相邻。

时间复杂度：O(nlogn)
空间复杂度：O(1)

3. 哈希表。
存储各数字次数，若当前数字次数大于等于 2，直接返回 True。

时间复杂度：O(n)
空间复杂度：O(n)

"""
from collections import defaultdict
from typing import List
import unittest


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """集合。"""
        return len(set(nums)) != len(nums)
    
    def contains_duplicate_2(self, nums: List[int]) -> bool:
        """排序。"""
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    
    def contains_duplicate_3(self, nums: List[int]) -> bool:
        """哈希表。"""
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] >= 2:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_contains_duplicate(self) -> None:
        self.assertTrue(
            self.s.contains_duplicate_3([1, 2, 3, 1])
        )
        self.assertFalse(
            self.s.contains_duplicate_3([1, 2, 3, 4])
        )
        self.assertTrue(
            self.s.contains_duplicate_3([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        )


if __name__ == '__main__':
    unittest.main()
