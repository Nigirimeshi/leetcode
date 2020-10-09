"""
跳跃游戏

链接：https://leetcode-cn.com/problems/jump-game

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0，所以你永远不可能到达最后一个位置。

官方解法：
1. 贪心。
依次遍历数组中的每一个位置，并实时维护最远可以到达的位置。
对于当前遍历到的位置 x，如果它在最远可以到达的位置的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，
因此我们可以用 xx+nums[x] 更新 最远可以到达的位置。

"""
import unittest
from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        """贪心。"""
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_can_jump(self) -> None:
        self.assertTrue(self.s.can_jump([2, 3, 1, 1, 4]))
        self.assertFalse(self.s.can_jump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
