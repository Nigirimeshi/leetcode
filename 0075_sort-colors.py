"""
颜色分类

链接：https://leetcode-cn.com/problems/sort-colors

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

我的解题思路：
1. 哈希表。（通过：√，但是写的有点怪）
先遍历一边数组，计算 0、1、2 各自出现的次数。
然后根据次数排序，覆盖原数组。

时间复杂度：O(N)。
空间复杂度：O(1)。

2. 逐位交换。

官方解法：
1. 一次遍历（交换）。
用三个指针（p0, p2 和 curr）来分别追踪 0 的最右边界，2 的最左边界和当前考虑的元素。
思路是沿着数组移动 curr，若 nums[curr] == 0，则将其与 nums[p0] 交换；若 nums[curr] == 2，则与 nums[p2] 交换。
算法：
 - 初始化 0 的最右边界：p0 = 0。整个算法执行过程中 nums[idx < p0] = 0。
 - 初始化 2 的最左边界：p2 = n - 1。整个算法执行过程中 nums[idx > p2] = 2。
 - 初始化当前元素序号：curr = 0。
 - while curr <= p2:
   - 若 nums[curr] == 0：交换 curr 和第 p0 个元素，并将 curr 和 p0 指针右移；
   - 若 nums[curr] == 2：交换 curr 和第 p2 个元素，并将 p2 指针左移；
   - 若 nums[curr] == 1：将指针 curr 右移。

时间复杂度 :由于对长度 NN的数组进行了一次遍历，时间复杂度为O(N)O(N) 。
空间复杂度 :由于只使用了常数空间，空间复杂度为O(1)O(1) 。

"""
import unittest
from typing import List


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {0: 0, 1: 0, 2: 0}
        for num in nums:
            counts[num] += 1

        for i in range(0, counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1
        for i in range(counts[0] + counts[1], len(nums)):
            nums[i] = 2


class OfficialSolution:
    def sort_colors(self, nums: List[int]) -> None:
        """一次遍历，交换元素。"""
        n = len(nums)
        p0, curr, p2 = 0, 0, n - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_sort_colors(self) -> None:
        case = [2, 0, 2, 1, 1, 0]
        self.s.sort_colors(case)
        self.assertListEqual(
            case,
            [0, 0, 1, 1, 2, 2],
        )


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_sort_colors(self) -> None:
        case = [2, 0, 2, 1, 1, 0]
        self.s.sort_colors(case)
        self.assertListEqual(
            case,
            [0, 0, 1, 1, 2, 2],
        )


if __name__ == '__main__':
    unittest.main()
