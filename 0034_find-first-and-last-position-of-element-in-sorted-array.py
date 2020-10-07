"""
在排序数组中查找元素的第一个和最后一个位置

链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

我的解题思路：
1. 二分查找。
先用二分查找找到目标元素，再从目标元素位置向后遍历，直到遍历的元素不等于目标元素。

官方解法：
1. 线性扫描。
从左向右遍历，找到目标元素下标；再从右向左遍历，找到目标元素下标。

时间复杂度：O(N)。
空间复杂度：O(1)。

2. 二分查找。
分别用二分查找最左边的 target 和最右边的 target。
利用 left 的真假来指示遇到 nums[i] 等于 target 的时候做什么，当 left 等于 true，就递归左区间，否则递归右区间。
如果在下标 i 时遇到了 target，那么最左边的 target 一定不会出现在下标大于 i 的位置，所以永远不需要考虑右子区间；
同理在求最右下标时，在下标 i 遇到了 target，那么最右边的 target 一定不会出现在下标小于 i 的位置，所以不考虑左子区间。

时间复杂度：O(logN)。
空间复杂度：O(1)。

"""
import unittest
from typing import List


class OfficialSolution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """线性扫描。"""
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] == target:
                ans.append(i)
                break

        for i in range(n - 1, -1, -1):
            if nums[i] == target:
                ans.append(i)
                break

        if not ans:
            ans.extend([-1, -1])
        return ans

    def search_range_2(self, nums: List[int], target: int) -> List[int]:
        """二分查找。"""
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]

        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums: List[int], size, target: int) -> int:
        """找做左边 target 的下标。"""
        left, right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                # 向左子区间继续搜索。
                right = mid - 1
            elif nums[mid] == target:
                # 向左子区间继续搜索。
                right = mid
            else:
                # nums[mid] < target
                # 向右子区间继续搜索。
                left = mid + 1

        if nums[left] != target:
            return -1
        return left

    def __find_last_position(self, nums: List[int], size, target: int) -> int:
        """找最右边 target 的下标。"""
        left, right = 0, size - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                # 向右子区间继续搜索。
                left = mid + 1
            elif nums[mid] == target:
                # 向右子区间继续搜索。
                left = mid
            else:
                # nums[mid] > target
                # 向左子区间继续搜索。
                right = mid - 1

        if nums[left] != target:
            return -1
        return left


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_search_range(self) -> None:
        self.assertListEqual(
            self.s.search_range(
                [5, 7, 7, 8, 8, 10],
                6
            ),
            [-1, -1]
        )


if __name__ == '__main__':
    unittest.main()
