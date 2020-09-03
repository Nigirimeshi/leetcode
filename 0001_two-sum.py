"""
两数之和

链接：https://leetcode-cn.com/problems/two-sum

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

我的解题思路：
1. 暴力：遍历数组每个元素 x，并查找是否存在一个值与 target - x 相等。
时间复杂度：O(n^2)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            differential = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == differential:
                    return [i, j]


def main():
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    if result == [0, 1]:
        print('ok')
    else:
        print('wrong')


if __name__ == '__main__':
    main()
