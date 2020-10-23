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

官方解法：
1. 排序。
如果将数组 nums 按单调递增或递减排序，那么下标为 n/2 的元素（下标从 0 开始）一定是众数。

时间复杂度：O(nlogn)。
空间复杂度：O(logn)。如果使用语言自带的排序算法，需要使用 O(logn) 的栈空间。如果自己编写堆排序，则只需要使用 O(1) 的额外空间。

2. 随机化。
因为超过 n/2 的数组下标被众数占据了，那么我们随机挑选一个下标对应的元素进行验证，有很大概率能找到众数。

时间复杂度：O(n)。理论上最坏情况下是 o(∞)，由于运气差一直找不到众数。
空间复杂度：O(1)。

"""
import collections
import random
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


class OfficialSolution:
    def majority_element(self, nums: List[int]) -> int:
        """排序。"""
        nums.sort()
        return nums[len(nums) // 2]

    def majority_element_2(self, nums: List[int]) -> int:
        """随机化。"""
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


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
