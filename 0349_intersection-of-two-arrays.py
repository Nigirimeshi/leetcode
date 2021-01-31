"""
两个数组的交集

链接：https://leetcode-cn.com/problems/intersection-of-two-arrays

给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

我的解题思路：
1. 两个集合。

时间复杂度：O(M+N)
空间复杂度：O(M+N)

"""
import unittest
from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """两个集合。"""
        set1, set2 = set(nums1), set(nums2)
        return self.set_intersection(set1, set2)
    
    def set_intersection(self, set1, set2: Set[int]) -> List[int]:
        # 遍历元素较少的列表，降低时间复杂度。
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]
    
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
