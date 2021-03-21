"""
缺失的第一个正数

链接：https://leetcode-cn.com/problems/first-missing-positive

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1

提示：
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1

解法：
1. 哈希表（用数组下标标记数字）。
算法：
1）遍历数组，将所有小于 0 的数字变成 n + 1，因为负数不在 [1,n] 范围内，需要忽略。
2）遍历数组，当 abs(num) <= n 时，将 nums[num-1] 处的数字变成负数（已经是负数则不处理）。
3）遍历数组，遇到的第一个正数的下标 + 1 即为缺失的最小正数；若数组全是负数，则 n + 1 为最小正数。

时间复杂度：O(N)
空间复杂度：O(1)
"""
import unittest
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        """哈希表（用数组下标标记数字）。"""
        n = len(nums)

        # 将所有负数变为 n + 1。
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 将 nums[abs(nums[i]) - 1] 对应的数变成负数，作为已存在数字的标记。
        for i in range(n):
            # 可能已被标记了。
            num = abs(nums[i])
            # 排除之前标记的负数。
            if num <= n:
                # 相当于标记数字 num 已存在。
                nums[num - 1] = -abs(nums[num - 1])

        # 遇到的第一个正数的下标 + 1 即为缺失的第一个正数。
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 数组都为负数，说明 1 到 n 都存在，那么缺失的第一个正数就是 n + 1。
        return n + 1


class Case:
    def __init__(self, nums: List[int], want: int):
        self.nums = nums
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_first_missing_positive(self):
        test_cases: List[Case] = [
            Case([1, 2, 0], 3),
            Case([3, 4, -1, 1], 2),
            Case([7, 8, 9, 11, 12], 1),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.first_missing_positive(tc.nums))


if __name__ == "__main__":
    unittest.main()
