"""
螺旋矩阵 II

链接：https://leetcode-cn.com/problems/spiral-matrix-ii

给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

提示：
1 <= n <= 20

解法：
1. 模拟。
算法：
1）设 l, r, t, b = 0, n - 1, 0, n - 1。
2）按从左到右、从上到下、从右到左、从下到上的顺序遍历矩阵。

时间复杂度：O(N) N 为 n * n。
空间复杂度：O(N)

"""
import unittest
from typing import List


class Solution:
    def generate_matrix(self, n: int) -> List[List[int]]:
        """模拟。"""
        # 生成矩阵。
        matrix: List[List[int]] = [[0] * n for _ in range(n)]
        # 初始坐标。
        left, right, top, button = 0, n - 1, 0, n - 1
        # 从 1 生成到 n。
        num, target = 1, n * n

        while num <= target:
            # 从左到右。
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 从上到下。
            for i in range(top, button + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 从右到左。
            for i in range(right, left - 1, -1):
                matrix[button][i] = num
                num += 1
            button -= 1

            # 从下到上。
            for i in range(button, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix


class Case:
    def __init__(self, n: int, want: List[List[int]]):
        self.n = n
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_generate_matrix(self) -> None:
        test_cases: List[Case] = [
            Case(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
            Case(1, [[1]]),
        ]
        for tc in test_cases:
            self.assertListEqual(tc.want, self.s.generate_matrix(tc.n))


if __name__ == "__main__":
    unittest.main()
