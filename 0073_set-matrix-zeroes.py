"""
矩阵置零

链接：https://leetcode-cn.com/problems/set-matrix-zeroes

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
 [1,1,1],
 [1,0,1],
 [1,1,1]
]
输出:
[
 [1,0,1],
 [0,0,0],
 [1,0,1]
]

示例 2:
输入:
[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
]
输出:
[
 [0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]
]

进阶:
一个直接的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

我的解题思路：
1. 迭代。
先遍历一遍矩阵，记录元素为 0 的行和列；
将记录的行和列变为 0。

时间复杂度：O(m*n)。
空间复杂度：O(m+n)。

官方解法：
1. O(1) 空间 - 在第一行第一列上设置标志位。
遍历矩阵，在第一行和第一列设置 0 标记位，用来表示该行该列是否为 0；
单独标记第一行和第一列是否为 0。

时间复杂度：O(n^2)。
空间复杂度：O(1)。

"""
import unittest
from typing import List


class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        rows, columns = [], []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # 记录元素为 0 的行和列位置。
                    rows.append(i)
                    columns.append(j)

        # 将记录的行置为 0。
        for row in rows:
            matrix[row] = [0] * m

        # 将记录的列置为 0。
        for i in range(n):
            for column in columns:
                matrix[i][column] = 0


class OfficialSolution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """在首行首列设置 0 标记位。"""
        n, m = len(matrix), len(matrix[0])

        # 检查第一行是否有 0。
        row_zero = True if 0 in matrix[0] else False

        # 检查第一列是否有 0。
        column_zero = False
        for i in range(n):
            if matrix[i][0] == 0:
                column_zero = True

        # 遍历矩阵，设置标记位。
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 矩阵置零。
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 判断首行首列是否需要置零。
        if row_zero:
            matrix[0] = [0] * m
        if column_zero:
            for i in range(n):
                matrix[i][0] = 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_set_zeroes(self) -> None:
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.s.set_zeroes(matrix)
        self.assertListEqual(
            matrix,
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]
        )


if __name__ == '__main__':
    unittest.main()
