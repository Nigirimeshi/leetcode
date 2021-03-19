"""
找到所有数组中消失的数字

链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array

给定一个范围在 1 ≤ a[i] ≤ n (n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

解法：
1. 集合。
时间复杂度：O(N)
空间复杂度：O(N)

2. 原地修改。
由于 nums 的数字范围均在 [1,n] 中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。

时间复杂度：O(N)
空间复杂度：O(1)
"""
import unittest
from typing import List, Set


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        memo: Set[int] = set()
        for num in nums:
            memo.add(num)

        ans: List[int] = []
        for i in range(1, len(nums) + 1):
            if i not in memo:
                ans.append(i)
        return ans

    def find_disappeared_numbers_2(self, nums: List[int]) -> List[int]:
        """原地修改。"""
        n = len(nums)
        for num in nums:
            idx = (num - 1) % n
            nums[idx] += n

        return [i + 1 for i in range(n) if nums[i] <= n]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_find_disappeared_numbers(self):
        self.assertListEqual(
            [5, 6], self.s.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
        )


if __name__ == "__main__":
    unittest.main()
