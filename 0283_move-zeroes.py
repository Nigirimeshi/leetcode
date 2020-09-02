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
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = list()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        for i in range(len(zeros)):
            del nums[zeros[i] - i]
            nums.append(0)


def main():
    cases = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(cases)
    if cases == [1, 3, 12, 0, 0]:
        print("ok")
    else:
        print("wrong")


if __name__ == '__main__':
    main()
