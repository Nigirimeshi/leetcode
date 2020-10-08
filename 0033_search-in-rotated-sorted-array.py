"""
搜索旋转排序数组

链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2])。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1


我的解题思路：
1. 二分查找。

官方解法：
1. 二分搜索。
将数组分为两部分，一定有一部分是有序的。
因此可以在二分搜索的时候查看当前 mid 分割出来的 [left, mid] 和 [mid+1, right] 哪个部分是有序的，
并根据有序部分判断 target 在不在该部分：
 - 如果 [left, mid - 1] 是有序数组，且 target 满足 [nums[left], nums[mid] - 1]，
   那么应该将搜索范围减小至 [left, mid - 1]，否则在 [mid + 1, right] 中查找。
 - 如果 [mid + 1, right] 是有序数组，且 target 满足 [nums[mid] + 1, nums[right]]，
   那么应该将搜索范围减小至 [mid + 1, right]，否则在 [left, mid - 1] 中查找。

时间复杂度：O(logN)。
空间复杂度：O(1)。

"""
import unittest
from typing import List


class OfficialSolution:
    def search(self, nums: List[int], target: int) -> int:
        """二分搜索。"""
        if not nums:
            return -1

        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # 如果左子区间有序。
            if nums[0] <= nums[mid]:
                # target 在 [0, mid - 1] 范围内。
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                # target 在 [mid + 1, right] 范围内。
                else:
                    left = mid + 1
            # 如果右子区间有序。
            else:
                # target 在 [mid + 1, n - 1] 范围内。
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_search(self) -> None:
        self.s.search([4, 5, 6, 7, 0, 1, 2], 0)


if __name__ == '__main__':
    unittest.main()
