"""
甲板上的战舰

链接：https://leetcode-cn.com/problems/battleships-in-a-board

给定一个二维的甲板， 请计算其中有多少艘战舰。

战舰用 'X' 表示，空位用 '.' 表示。

你需要遵守以下规则：
给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列) 组成，其中 N 可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。

示例 :
X . . X
. . . X
. . . X
在上面的甲板中有 2 艘战舰。

无效样例 :
. . . X
X X X X
. . . X

你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。

进阶:
你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？

解法：
1. 遍历。
遍历矩阵，
 - 跳过 .
 - 当前元素的上边和左边是 x 时，说明当前元素是战舰的一部分，直接跳过
 - 当前元素是 x，且上边和左边不是 x，说明是战舰的头部，结果 + 1。
 
时间复杂度：O(N)
空间复杂度：O(1)
"""
import unittest
from typing import List


class Solution:
    def count_battleships(self, board: List[List[str]]) -> int:
        """遍历。"""
        n, m = len(board), len(board[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == ".":
                    continue
                # 上面是 X，说明当前元素是战舰的一部分。
                if i > 0 and board[i - 1][j] == "X":
                    continue
                # 左边是 X，说明当前元素是战舰的一部分。
                if j > 0 and board[i][j - 1] == "X":
                    continue

                # 当前节点是战舰头部。
                ans += 1
        return ans


class Case:
    def __init__(self, board: List[List[str]], want: int):
        self.board = board
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_count_battleships(self) -> None:
        test_cases: List[Case] = [
            Case([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]], 2),
            Case([["X", ".", "."], [".", ".", "."]], 1),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.count_battleships(tc.board))


if __name__ == "__main__":
    unittest.main()
