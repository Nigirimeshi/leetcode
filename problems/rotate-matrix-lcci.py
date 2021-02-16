"""
面试题 01.07 旋转矩阵

链接：https://leetcode-cn.com/problems/rotate-matrix-lcci

给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。

请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

解法：
1. 辅助数组。
矩阵中第 i 行的第 j 个元素，经过旋转，将出现在倒数第 i 列的第 j 个元素。
即 matrix[row][col] = matrix_new[col][n - row - 1]

时间复杂度：O(N^2)
空间复杂度：O(N)

2. 原度旋转。

时间复杂度：O(N^2)
空间复杂度：O(1)

3. 用翻转代替旋转。
先将矩阵水平翻转，再沿着主对角线翻转。

时间复杂度：O(N^2)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """辅助矩阵。"""
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                matrix_new[col][n - row - 1] = matrix[row][col]
        matrix[:] = matrix_new

    def rotate2(self, matrix: List[List[int]]) -> None:
        """原地旋转。"""
        pass

    def rotate3(self, matrix: List[List[int]]) -> None:
        """用翻转代替旋转。"""
        n = len(matrix)
        # 水平翻转。
        for row in range(n // 2):
            for col in range(n):
                matrix[row][col], matrix[n - row - 1][col] = matrix[n - row - 1][col], matrix[row][col]

        # 沿主对角线翻转。
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_rotate(self) -> None:
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        self.s.rotate(matrix)
        self.assertListEqual(
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ],
            matrix,
        )

    def test_rotate3(self) -> None:
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        self.s.rotate3(matrix)
        self.assertListEqual(
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ],
            matrix,
        )


if __name__ == '__main__':
    unittest.main()
