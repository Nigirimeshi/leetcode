"""
跳跃游戏 V

给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：

链接：https://leetcode-cn.com/problems/jump-game-v

i + x，其中 i + x < arr.length 且 0 < x <= d。
i - x，其中 i - x >= 0 且 0 < x <= d。
除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k]，
其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。

你可以选择数组的任意下标开始跳跃。请你返回你 最多可以访问多少个下标。

请注意，任何时刻你都不能跳到数组的外面。

示例 1：
输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
输出：4
解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。
注意，如果你从下标 6 开始，你只能跳到下标 7 处。你不能跳到下标 5 处因为 13 > 9 。
你也不能跳到下标 4 处，因为下标 5 在下标 4 和 6 之间且 13 > 9 。
类似的，你不能从下标 3 处跳到下标 2 或者下标 1 处。

示例 2：
输入：arr = [3,3,3,3,3], d = 3
输出：1
解释：你可以从任意下标处开始且你永远无法跳到任何其他坐标。

示例 3：
输入：arr = [7,6,5,4,3,2,1], d = 1
输出：7
解释：从下标 0 处开始，你可以按照数值从大到小，访问所有的下标。

示例 4：
输入：arr = [7,1,7,1,7,1], d = 2
输出：2

示例 5：
输入：arr = [66], d = 1
输出：1

提示：
1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length

解法：
1. DFS + 动态规划。

时间复杂度：O(ND)
空间复杂度：O(N)

"""
import unittest
from typing import List


class Solution:
    def max_jumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1 for _ in range(n)]
        
        def dfs(idx: int) -> None:
            # 对应位置的可跳跃最大值已知。
            if dp[idx] != -1:
                return
            dp[idx] = 1
            
            # 向左递归，找出左边 d 个可跳跃位置中的跳跃最大值。
            i = idx - 1
            while 0 <= i and idx - i <= d and arr[idx] > arr[i]:
                dfs(i)
                dp[idx] = max(dp[idx], dp[i] + 1)
                i -= 1
            
            # 向右递归，找出右边 d 个可跳跃位置中的跳跃最大值。
            j = idx + 1
            while j < n and j - idx <= d and arr[idx] > arr[j]:
                dfs(j)
                dp[idx] = max(dp[idx], dp[j] + 1)
                j += 1
        
        for idx in range(n):
            dfs(idx)
        
        return max(dp)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_max_jumps(self) -> None:
        self.assertEqual(
            4,
            self.s.max_jumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2)
        )


if __name__ == '__main__':
    unittest.main()
