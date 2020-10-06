"""
数组中的第 k 个最大元素

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

我的解题思路：
1. 最小堆。
时间复杂度：O(N*logK)。
空间复杂度：O(K)。

2. 先排序。


"""
import unittest
import heapq
from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """最小堆。"""
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_find_kth_largest(self) -> None:
        self.s.find_kth_largest(
            [3, 2, 1, 5, 6, 4],
            2,
        )


if __name__ == '__main__':
    unittest.main()
