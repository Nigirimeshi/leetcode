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

官方解法：
1. DFS。
从坐标 (i, j) 的上下左右 (i-1, j), (i+1, j), (i, j-1), (i, j+1) 做深度优先搜索。
终止条件：
 - (i, j) 越过矩阵边界。
 - grid[i][j] == '0'，表示已经越过岛屿边界。
将遍历过的岛屿标为 0，即将岛屿删除，避免之后重复搜索。

主循环：遍历矩阵，遇到 grid[i][j] == '1' 时，开始做 dfs，并使岛屿数加 1。

时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。
空间复杂度：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN。

2. BFS。
使用队列 queue，判断队首节点 (i, j) 是否为 '1'：
 - 若是则将该节点置零，并将上下左右节点加入队列。
 - 若不是，跳过。
循环从队列取，直到队列空。

时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。
空间复杂度：O(min(M,N))，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min(M,N)。

"""
import unittest
from typing import List


class OfficialSolution:
    def num_islands(self, grid: List[List[str]]) -> int:
        """DFS。"""

        def dfs(g: List[List[str]], i, j: int) -> None:
            if not 0 <= i < len(g) or not 0 <= j < len(g[0]) or g[i][j] == '0':
                return

            g[i][j] = '0'
            dfs(g, i - 1, j)
            dfs(g, i + 1, j)
            dfs(g, i, j - 1)
            dfs(g, i, j + 1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    count += 1
        return count

    def num_islands_2(self, grid: List[List[str]]) -> int:
        """BFS。"""

        def bfs(g: List[List[str]], i, j) -> None:
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0)
                if 0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] == '1':
                    g[i][j] = '0'
                    queue += [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != '1':
                    continue
                bfs(grid, r, c)
                count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_num_islands(self) -> None:
        self.assertEqual(
            self.s.num_islands_2(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )
        self.assertEqual(
            self.s.num_islands(
                [
                    ['1', '1', '0', '0', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '1', '0', '0'],
                    ['0', '0', '0', '1', '1'],
                ]
            ),
            3,
        )
        self.assertEqual(
            self.s.num_islands(
                [
                    ["1", "1", "1"],
                    ["0", "1", "0"],
                    ["1", "1", "1"],
                ]
            ),
            1,
        )


if __name__ == '__main__':
    unittest.main()
