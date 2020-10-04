"""
子集

链接：https://leetcode-cn.com/problems/subsets

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

我的解题思路：
1. 回溯。（通过：√）


"""
import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯。"""
        if not nums:
            return []

        def backtrack(sequence: List[int], index: int) -> None:
            if index == n:
                return
            else:
                for i in range(index, n):
                    sequence.append(nums[i])
                    ans.append(sequence.copy())
                    backtrack(sequence, i + 1)
                    sequence.pop()

        n = len(nums)
        ans = [[]]
        backtrack([], 0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_subsets(self) -> None:
        ans = self.s.subsets([1, 2, 3])
        print(ans)


if __name__ == '__main__':
    unittest.main()
