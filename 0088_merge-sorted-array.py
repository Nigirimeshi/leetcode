"""
合并两个有序数组

链接：https://leetcode-cn.com/problems/merge-sorted-array

给你两个“有序整数数组” nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

我的解题思路：
1. 先将 nums2 合并到 nums1 上，填满原本多余的 0，然后排序。

2. 双指针（插入排序思想）。

官方解法：
1. 先合并，后排序。(这种方法没有利用两个数组本身已经有序这一点。)
时间复杂度 : O((n+m)log(n+m))
空间复杂度 : O(1)

2. 双指针法（从前往后）。
用 p1 指向 nums1 的开头，p2 指向 nums2 的开头，比较指向元素大小，每次将最小值放入 nums1；
由于 nums1 是用于输出的数组，因此需要先将 nums1 中前 m 个元素暂存在其他地方，需要 O(m) 的空间复杂度。
时间复杂度：O(m+n)
空间复杂度：O(m)

3. 双（三）指针法（从后往前）
由于两数组有序递增 且 nums1 尾部元素为 0 ，可以从尾部开始改写 nums1，无需占用额外空间，用 p 表示改写的下标位置（索引）。
时间复杂度：O(m+n)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
    
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """双指针（插入排序思想）。

        首先选择 nums2 第 1 个元素，将其插入到 nums1 中正确的位置；
        然后再从 nums2 选择第 2 位元素，沿着 nums1 中上次插入的位置，向右寻找合适位置并插入，依此类推。
        """
        if n == 0:
            return None
        
        for i in range(n):
            nums1[m + i] = nums2[i]
            for j in range(m + i, 0, -1):
                if nums1[j] < nums1[j - 1]:
                    nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]
                else:
                    break


class OfficialSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """先合并，后排序。"""
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """双指针法（从前往后）"""
        # 由于结果需要放在 nums1 中，暂存 nums1 原本的前 m 个元素，并清空 nums1。
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            # 比较双指针指向元素大小，并移动指针。
            if nums1_copy[p1] <= nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # p1 和 p2 其中一方会先移动到数组尾部，这里另一方剩余的元素加上。
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    def merge_3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        双指针 - 从后向前。
        因为 nums1 尾部是 0，因此从尾部改写 nums1，不需要额外的空间。
        设置指针 p1，p2 分别指向 m-1，n-1，循环左移，且 p1 >= 0 and p2 >= 0；
        每次将 nums1[p1] 和 nums2[p2] 中较大值放入 nums1 的尾部；
        最后再将 nums2 中剩余元素放入 nums1。
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
    
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
    
        # 将 nums2 中剩余的值放入 nums1。
        nums1[:p2 + 1] = nums2[:p2 + 1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_merge(self) -> None:
        # nums1 = [1, 2, 3, 0, 0, 0]
        # self.s.merge(nums1, 3, [2, 5, 6], 3)
        # self.assertListEqual(
        #     nums1,
        #     [1, 2, 2, 3, 5, 6],
        # )
    
        nums1 = [1, 2, 3, 4, 0, 0, 0]
        self.s.merge(nums1, 4, [2, 5, 6], 3)
        self.assertListEqual(
            nums1,
            [1, 2, 2, 3, 4, 5, 6],
        )


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_merge_3(self) -> None:
        nums1 = [1, 2, 3, 0, 0, 0]
        self.s.merge_3(nums1, 3, [2, 5, 6], 3)
        self.assertListEqual(
            nums1,
            [1, 2, 2, 3, 5, 6],
        )


if __name__ == '__main__':
    unittest.main()
