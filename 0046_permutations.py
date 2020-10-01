"""
全排列

链接：https://leetcode-cn.com/problems/permutations

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

我的解题思路：
1. 回溯。（通过：√）
回溯过程中，跳过已存在的数字。

官方解法：
1. 搜索回溯。
将题目给定的 n 个数的数组 nums[] 划分成左右两个部分，左边的表示已经填过的数，右边表示待填的数，
我们在递归搜索的时候只要动态维护这个数组即可。


"""
import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯法。"""

        def backtrack(sequence: List[int]) -> None:
            if len(sequence) == n:
                ans.append(sequence.copy())
                return
            else:
                for num in nums:
                    if num in sequence:
                        continue
                    sequence.append(num)
                    backtrack(sequence)
                    sequence.pop()

        n = len(nums)
        ans = []
        backtrack([])
        return ans


class OfficialSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """探索回溯。"""

        def backtrack(first) -> None:
            if first == n:
                ans.append(nums[:])
                return

            for i in range(first, n):
                # 动态维护数组。
                nums[first], nums[i] = nums[i], nums[first]
                # 递归下一个数。
                backtrack(first + 1)
                # 撤销操作。
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        ans = []
        backtrack(0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_permute(self) -> None:
        ans = self.s.permute([1, 2, 3])
        print(ans)


if __name__ == '__main__':
    unittest.main()
