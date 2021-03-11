"""
N 皇后

链接：https://leetcode-cn.com/problems/n-queens

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

解法：
1. 回溯。

时间复杂度：O(N!)
空间复杂度：O(N)。
空间复杂度主要取决于递归调用层数、记录每行放置的皇后的列下标的数组以及三个集合，
递归调用层数不会超过 N，数组的长度为 N，每个集合的元素个数都不会超过 N。

"""
import unittest
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans: List[List[str]] = []

        # 初始化棋盘。
        board: List[List[str]] = [["."] * n for _ in range(n)]
        self.backtrack(board, 0, ans)
        return ans

    def backtrack(self, board: List[List[str]], row: int, ans: List[List[str]]) -> None:
        # 回溯终止条件。
        if len(board) == row:
            # 重建数组，避免引用。
            tmp: List[str] = []
            for i in range(len(board)):
                tmp.append("".join(board[i]))
            ans.append(tmp)
            return

        # 选择该行的每一列。
        for col in range(len(board[row])):
            # 排除不合法的选择。
            if not self.is_valid(board, row, col):
                continue

            # 做选择。
            board[row][col] = "Q"
            # 递归下一行。
            self.backtrack(board, row + 1, ans)
            # 撤销选择。
            board[row][col] = "."

    def is_valid(self, board: List[List[str]], row: int, col: int) -> bool:
        # 检查列，同一列不能存在皇后。
        for i in range(len(board)):
            if board[i][col] == "Q":
                return False

        # 检查右上方，不能存在皇后。
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j + 1

        # 检查左上方，不能存在皇后。
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j - 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_n_queens(self) -> None:
        self.assertListEqual(
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
            self.s.solveNQueens(4),
        )


if __name__ == "__main__":
    unittest.main()
