"""
移动零

链接：https://leetcode-cn.com/problems/move-zeroes

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

我的解题思路：
1. 遍历数组，记录 0 的下标，删除所有 0，最后在数组尾部追加对应数量的 0。

官方解法：
1. 两次遍历（双指针）。
创建两个指针 i，j，第一次遍历时用 j 记录非 0 元素的数量。
遍历到非 0 元素时向左挪，并使 j + 1，遍历完后，j - 1 就等于最后一个非 0 元素的下标。
第二次遍历从 j 开始，将剩下的元素全部赋值 0。

时间复杂度：O(n)
空间复杂度：O(1)

2. 一次遍历（交换元素）。
参考快排思想，快排首先要确定一个待分割元素做中间点 x，然后把小于 x 的放左边，大于 x 的放右边。
该题可以把 0 做为中间点，把不等于 0 的放左边，等于 0 的放右边。
可以设置快指针 i，慢指针 j，只要 nums[i] != 0，就交换 nums[i] 和 nums[j]。

时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """遍历。"""
        # 记录 0 元素的下标。
        zero_idx = list()
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx.append(i)
        
        # 根据下标删除 0 元素，并在末尾追加 0。
        for i in range(len(zero_idx)):
            # 每删除一个 0 元素，其他 0 元素的下标就得 - 1，因此各 0 元素的真正下标为 zero_idx[i] - i。
            del nums[zero_idx[i] - i]
            nums.append(0)


class OfficialSolution:
    def move_zeroes(self, nums: List[int]) -> None:
        """两次遍历（双指针）。"""
        n = len(nums)
        
        # 用 j 计算非 0 元素个数，遍历完，j - 1 就指向了最后一个非 0 元素的下标。
        j = 0
        for i in range(n):
            # 将非 0 元素移到左边。
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # 此时 j - 1 指向了最后一个非 0 元素，剩下的全是 0，依次赋值为 0。
        for i in range(j, n):
            nums[i] = 0
    
    def move_zeroes_2(self, nums: List[int]) -> None:
        """一次遍历（快排思想，交换元素）。"""
        n = len(nums)

        # j 指向 0 元素。
        j = 0
        # i 持续向右移动。
        for i in range(n):
            # 遇到非 0 元素，j 向右移动。
            if nums[i] != 0:
                # 不等于 0 的放左边，等于 0 的放右边。
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

    def move_zeroes_3(self, nums: List[int]) -> None:
        """双指针。"""
        n = len(nums)
        left, right = 0, 0
        while right < n:
            # right 从左向右移动，直到指向非 0 元素。
            if nums[right] != 0:
                # 交换 left，right 指向的元素。
                nums[left], nums[right] = nums[right], nums[left]
                # 右移 left。
                left += 1
            right += 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_move_zeroes(self) -> None:
        nums = [0, 1, 0, 3, 12]
        self.s.move_zeroes(nums)
        self.assertListEqual(
            nums,
            [1, 3, 12, 0, 0],
        )


if __name__ == '__main__':
    unittest.main()
