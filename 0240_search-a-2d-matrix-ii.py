"""
搜索二维矩阵 II

链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。

我的解题思路：
1. . 二分搜索。
先二分搜索确定行，再二分搜索列。

2. 暴力搜索。

官方解法：
1. 二分法搜索。
在对角线上迭代，二分搜索行和列，直到对角线的迭代元素用完为止。

时间复杂度：O(lgn!)
空间复杂度：O(1)

2. 移动指针。（最优解）
初始化一个指向矩阵左下角 [row, col] 的指针 p，然后直到找到目标 target 之前，执行下列操作：
 - 若 p > target，row--；
 - 若 p < target，col++；
 - row 和 col 不能超出矩阵范围。

时间复杂度：O(m+n)。
空间复杂度：O(1)。

"""
from typing import List
import unittest


class OfficialSolution:
    def binary_search(self, matrix: List[List[int]], target: int, start: int, vertical: bool) -> bool:
        """垂直或水平二分搜索矩阵。"""
        low = start
        hig = len(matrix) - 1 if vertical else len(matrix[0]) - 1
        
        while low <= hig:
            mid = (low + hig) // 2
            # 垂直二分搜索，行坐标不变。
            if vertical:
                if matrix[start][mid] > target:
                    hig = mid - 1
                elif matrix[start][mid] < target:
                    low = mid + 1
                else:
                    return True
            
            # 水平二分搜索，纵坐标不变。
            else:
                if matrix[mid][start] > target:
                    hig = mid - 1
                elif matrix[mid][start] < target:
                    low = mid + 1
                else:
                    return True
        
        return False
    
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        """二分搜索。"""
        if not matrix:
            return False
        
        # 在对角线上搜索。
        for i in range(min(len(matrix), len(matrix[0]))):
            horizontal_found = self.binary_search(matrix, target, i, False)
            vertical_found = self.binary_search(matrix, target, i, True)
            if horizontal_found or vertical_found:
                return True
        return False
    
    def search_matrix_2(self, matrix: List[List[int]], target: int) -> bool:
        """移动指针。"""
        if not matrix:
            return False
        
        hight, width = len(matrix), len(matrix[0])
        
        # 用 row，col 指向矩阵左下角。
        row, col = hight - 1, 0
        
        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_search_matrix(self) -> None:
        self.assertTrue(
            self.s.search_matrix(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                5,
            ),
        )
        self.assertFalse(
            self.s.search_matrix(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                20,
            ),
        )


if __name__ == '__main__':
    unittest.main()
