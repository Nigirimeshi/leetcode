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

官方解法：
1. 基于快速排序的选择方法。
对原数组快排的分区过程中，只要某次用于划分左右区域的下标 q 为倒数第 k 个下标时，就得到了答案。

时间复杂度：O(N)，如上文所述，证明过程可以参考「《算法导论》9.2：期望为线性的选择算法」。
空间复杂度：O(logN)，递归使用栈空间的空间代价的期望为 O(logN)。

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


class OfficialSolution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """基于快速排序的选择方法。"""
        n = len(nums)
        target_index = n - k
        left, right = 0, n - 1
        while True:
            index = self.partition(nums, left, right)
            if index == target_index:
                return nums[index]
            elif index < target_index:
                # 下一轮在 [index + 1, right] 中找。
                left = index + 1
            else:
                right = index - 1

    def partition(self, nums: List[int], left, right: int) -> int:
        """快排分区。"""
        pivot = left
        i, j = left, right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        # 此时 i 等于 j。
        nums[j], nums[pivot] = nums[pivot], nums[j]
        return j


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
