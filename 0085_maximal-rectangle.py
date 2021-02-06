"""
最大矩形

链接：https://leetcode-cn.com/problems/maximal-rectangle

给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。

示例 2：
输入：matrix = []
输出：0

示例 3：
输入：matrix = [["0"]]
输出：0

示例 4：
输入：matrix = [["1"]]
输出：1

示例 5：
输入：matrix = [["0","0"]]
输出：0

提示：
rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

官方解法：
1. 将问题转变为求柱形图中最大的矩形。
计算矩阵每一层的高度（列上连续 1 的数量），得到 heights，然后带入 largest_rectangle_area(heights)。

时间复杂度：O(MN)
空间复杂度：O(N)

"""
import unittest
from typing import List


class OfficialSolution:
    def maximal_rectangle(self, matrix: List[List[str]]) -> int:
        """计算每层高度，求柱形图中最大的矩形面积。"""
        row = len(matrix)
        if row == 0:
            return 0
        
        area = 0
        
        # 计算矩形每层的高度（连续 1 个数量）。
        col = len(matrix[0])
        # 初始化高度。
        heights: List[int] = [0] * col
        for i in range(row):
            for j in range(col):
                # 更新高度。
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            area = max(area, self.largest_rectangle_area(heights))
        return area
    
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """单调栈。"""
        # 简化代码，先给 height 头部和尾部插入高度为 0 的柱体。
        heights = heights.copy()
        heights.insert(0, 0)
        heights.append(0)
        
        area = 0
        # 存放柱体下标，单调递增。
        stack: List[int] = []
        for i in range(len(heights)):
            # 若当前柱体高度小于栈顶柱体高度，则计算面积。
            while stack and heights[i] < heights[stack[-1]]:
                # 弹出栈顶柱体下标，并得到其高度。
                h = heights[stack.pop()]
                # 面积 = 弹出栈顶柱体的高度 * (右边界（当前遍历到的柱体下标） - 左边界（当前栈顶柱体下标） - 1)
                area = max(area, h * (i - stack[-1] - 1))
            
            # 若当前柱体高度大于等于栈顶柱体高度，则将当前柱体下标入栈。
            stack.append(i)
        
        return area


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_maximal_rectangle(self) -> None:
        self.assertEqual(
            0,
            self.s.maximal_rectangle([])
        )
        self.assertEqual(
            0,
            self.s.maximal_rectangle([["0"]])
        )
        self.assertEqual(
            1,
            self.s.maximal_rectangle([["1"]])
        )
        self.assertEqual(
            0,
            self.s.maximal_rectangle([["0", "0"]])
        )
        self.assertEqual(
            6,
            self.s.maximal_rectangle([
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ])
        )


if __name__ == '__main__':
    unittest.main()
