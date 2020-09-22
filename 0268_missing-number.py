"""
缺失数字

链接：https://leetcode-cn.com/problems/missing-number

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

我的解题思路：
1. 用数字总和减去已存在的数字，结果即缺失的数字。

[0, 1] = 1
[0, 1, 2] = 3 = (1+2) * 2//2
[0, 1, 2, 3] = 6 = (1+3) * 3//2 + 2
[0, 1, 2, 3, 4] = 10 = (1+4) * 4//2
[0, 1, 2, 3, 4, 5] = 15 = (1+5) * 5//2 + 3

若 n 为数组长度，那么：
最大数字 max = n，数字总和 sums = (min+max) * (max//2)，
如果 max 为奇数，sums 还需加上 (min+max)//2。

接着迭代数组，用 sums 减去每个数字，剩余值即为缺失的数字。

时间复杂度：O(n)。
空间复杂度：O(1)。

官方解法：
1. 数学（高斯求和公式）。
sum = n*(n+1)/2

时间复杂度：O(n)。求出数组中所有数的和的时间复杂度为 O(n)，高斯求和公式的时间复杂度为 O(1)，因此总的时间复杂度为 O(n)。
空间复杂度：O(1)。算法中只用到了 O(1) 的额外空间，用来存储答案。

"""
import unittest
from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        _max, _min, _sum = len(nums), 1, 0
        if _max == _min:
            _sum = 1
        else:
            _sum = (_max + _min) * (_max // 2)
            if _max % 2 != 0:
                _sum += (_max + _min) // 2

        for num in nums:
            # 迭代数组，用 sum 减去每个数字，剩余值即为缺失的数字。
            _sum -= num
        return _sum


class OfficialSolution:
    def missing_number(self, nums: List[int]) -> int:
        """高斯公式计算。"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_missing_number(self) -> None:
        self.assertEqual(
            self.s.missing_number([3, 0, 1]),
            2,
        )
        self.assertEqual(
            self.s.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]),
            8,
        )


if __name__ == '__main__':
    unittest.main()
