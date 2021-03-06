"""
有效的数独

链接：https://leetcode-cn.com/problems/valid-sudoku

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

示例 2:
输入:
[
 ["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例 1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符'.'。
给定数独永远是 9x9 形式的。

我的解题思路：
1. 哈希表分别记录行、列元素次数，大于一则返回 False；
将 9x9 的表格划分成 9 块，用哈希表记录每块的元素次数，每个块的索引值计算公式为：box_index = (row / 3) * 3 + column / 3

"""
import unittest

from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        boxes = [{} for i in range(9)]
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]

        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == '.':
                    continue

                rows[row][num] = rows[row].get(num, 0) + 1
                columns[column][num] = columns[column].get(num, 0) + 1

                box_index: float = (row // 3) * 3 + column // 3
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                if rows[row][num] > 1 or columns[column][num] > 1 or boxes[box_index][num] > 1:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_valid_sudoku(self) -> None:
        cases = [
            {
                'input': [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ],
                'output': True,
            },
            {
                'input': [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ],
                'output': False,
            },
        ]
        for case in cases:
            self.assertEqual(self.s.is_valid_sudoku(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
