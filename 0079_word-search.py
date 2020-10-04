"""
单词搜索

链接：https://leetcode-cn.com/problems/word-search

给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

官方解法：
1. DFS、回溯。
首先找到单词的起始字母，然后四周扩散搜索下个字母。


"""
import unittest
from typing import List


class OfficialSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS + 回溯。"""
        m, n = len(board), len(board[0])

        visited = [[False] * n for _ in range(m)]

        rows = [-1, 0, 1, 0]
        cols = [0, -1, 0, 1]

        def dfs(x, y, idx: int):
            """
            :param x: 行索引
            :param y: 列索引
            :param idx: 单词对应字母的索引
            :return:
            """
            # 字母不匹配。
            if board[x][y] != word[idx]:
                return False

            # 单词最后一个字母匹配，说明找到了 word 字符串。
            if idx == len(word) - 1:
                return True

            # 编辑检查过的字段。
            visited[x][y] = True

            # 向上下左右四个方向扩散搜索字母。
            for i in range(4):
                row = x + rows[i]
                column = y + cols[i]
                if 0 <= row < m and 0 <= column < n and not visited[row][column] and dfs(row, column, idx + 1):
                    return True

            # 扩散未能搜索到对应字母，释放标记。
            visited[x][y] = False
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_exist(self) -> None:
        self.assertTrue(
            self.s.exist(
                [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "ABCCED"),
        )


if __name__ == '__main__':
    unittest.main()
