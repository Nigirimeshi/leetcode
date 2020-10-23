"""
多数元素

链接：https://leetcode-cn.com/problems/majority-element

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 n/2 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

我的解题思路：
1. 哈希表。
遍历数组，哈希表记录数字即出现的次数，同时记录出现次数最多的数字。

时间复杂度：O(n)。
空间复杂度：O(n)。

"""
import collections
import unittest
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        """哈希表。"""
        counts = collections.defaultdict(int)
        ans = nums[0]
        for num in nums:
            counts[num] += 1
            ans = ans if counts[ans] >= counts[num] else num
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_majority_element(self) -> None:
        self.assertEqual(
            self.s.majority_element([3, 2, 3]),
            3,
        )
        self.assertEqual(
            self.s.majority_element([2, 2, 1, 1, 1, 2, 2]),
            2,
        )


if __name__ == '__main__':
    unittest.main()
