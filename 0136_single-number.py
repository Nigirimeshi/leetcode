"""
只出现一次的数字

链接：https://leetcode-cn.com/problems/single-number

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4

我的解题思路：
1. 如果不用考虑时间和空间复杂度的化，就先排序，然后找出左右相邻两个元素均不同的那个元素。

官方解法：
方法 1：使用位运算。
对于这道题，可使用异或运算。异或运算有以下三个性质：
1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
2. 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
3. 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]


class OfficialSolution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


def main():
    s = Solution()
    s.singleNumber([2, 2, 1])


if __name__ == '__main__':
    main()
