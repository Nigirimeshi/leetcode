"""
岛屿数量

链接：https://leetcode-cn.com/problems/number-of-islands

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
[
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]
输出: 1

示例 2:
输入:
[
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

我的解题思路：
1. 哈希表。
双层遍历二维网格，用哈希表存储坐标和分组值。
设行为 i，列为 j，当 i > 0，j > 0 时，检查元素为 1 的相邻左边和上边元素在哈希表中是否存在分组值，存在则记录该元素坐标，分组值相等；
不存在则记录坐标，并使分组值加 1。

"""
import unittest
from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        maps = {}
        num_groups = 0
        rows, columns = len(grid), len(grid[0])

        if grid[0][0] == '1':
            num_groups += 1
            maps[(0, 0)] = num_groups

        # 遍历第一行。
        for j in range(1, columns):
            if grid[0][j] != '1':
                continue
            if (0, j - 1) in maps:
                maps[(0, j)] = maps[(0, j - 1)]
            else:
                num_groups += 1
                maps[(0, j)] = num_groups

        # 遍历第一列。
        for i in range(1, rows):
            if grid[i][0] != '1':
                continue
            if (i - 1, 0) in maps:
                maps[(i, 0)] = maps[(i - 1, 0)]
            else:
                num_groups += 1
                maps[(i, 0)] = num_groups

        for i in range(1, rows):
            for j in range(1, columns):
                if grid[i][j] != '1':
                    continue

                if not maps.__contains__((i, j - 1)) and not maps.__contains__((i - 1, j)):
                    num_groups += 1
                    maps[(i, j)] = num_groups
                    continue

                if (i, j - 1) in maps:
                    maps[(i, j)] = maps[(i, j - 1)]
                    continue

                if (i - 1, j) in maps:
                    maps[(i, j)] = maps[(i - 1, j)]
                    continue

        print(num_groups)
        return num_groups


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_num_islands(self) -> None:
        self.s.num_islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        self.s.num_islands(
            [
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1'],
            ]
        )
        self.s.num_islands(
            [
                ["1", "1", "1"],
                ["0", "1", "0"],
                ["1", "1", "1"],
            ]
        )


if __name__ == '__main__':
    unittest.main()
