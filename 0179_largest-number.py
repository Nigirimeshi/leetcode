"""
最大数

链接：https://leetcode-cn.com/problems/largest-number

给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：

输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 109


官方解法：
1. 自定义排序。
先将每个数字变成字符串，然后比较字符串排序。
比较的关键在于 x + y 和 y + x。

时间复杂度：O(NlogN)
空间复杂度：O(N)

"""
from typing import List
import unittest


class LargestNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largest_number(self, nums: List[int]) -> str:
        largest_num = ''.join(
            sorted(
                map(str, nums),
                key=LargestNumKey,
            )
        )
        return '0' if largest_num[0] == 0 else largest_num


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_largest_number(self) -> None:
        self.assertEqual(
            self.s.largest_number([10, 2]),
            '210',
        )


if __name__ == '__main__':
    unittest.main()
