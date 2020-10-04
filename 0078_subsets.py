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

官方解法：
1. 位运算。
记原序列中元素的总数为 n。原序列中的每个数字 a(i) 的状态可能有两种，即「在子集中」和「不在子集中」。
我们用 1 表示「在子集中」，0 表示不在子集中，那么每一个子集可以对应一个长度为 n 的 0/1 序列，第 i 位表示 a(i) 是否在子集中。

例如：n = 3, a = {5, 2, 9} 时：
0/1 序列              子集              0/1 序列对应的二进制数
000                  {}                0
001                  {9}               1
010                  {2}               2
011                  {2,9}             3
100                  {5}               4
101                  {5,9}             5
110                  {5,2}             6
111                  {5,2,9}           7

可以发现 0/1 序列对应的二进制数正好从 0 到 2^n - 1。
我们可以枚举 mask 属于 [0, 2^n - 1]，mask 的二进制表示是一个 0/1 序列，我们可以按照这个 0/1 序列在原集合中取数。
当枚举完所有 2^n 个 mask，就构造出了所有的子集。

时间复杂度：O(n * 2^n)。一共 2^n 个状态，每种状态需要 O(n) 的时间来构造子集。
空间复杂度：O(n)。即构造子集使用的临时数组 t 的空间代价。


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


class OfficialSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """位运算。"""
        ans = []
        n = len(nums)
        for mask in range(1 << n):
            sets = []
            for j in range(n):
                if (mask >> j) & 1 == 1:
                    sets.append(nums[j])
            ans.append(sets)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_subsets(self) -> None:
        ans = self.s.subsets([1, 2, 3])
        print(ans)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_subsets(self) -> None:
        ans = self.s.subsets([1, 2, 3])
        print(ans)


if __name__ == '__main__':
    unittest.main()
