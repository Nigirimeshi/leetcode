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
from collections import deque
from typing import List
import unittest


class OfficialSolution:
    def DFS(self, grid: List[List[str]], i: int, j: int):
        row, col = len(grid), len(grid[0])
        
        # 搜索过的节点置为 0。
        grid[i][j] = '0'
        # 构造水平和垂直方向上的相邻节点坐标。
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            # 继续搜索坐标有效且值为 1 的节点。
            if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                self.DFS(grid, x, y)
    
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        DFS。
        遍历二维数组，如果一个位置为 1，则以该位置为起始节点进行深度优先搜索，
        并将搜索过程中每个搜索到的 1 置为 0。
        """
        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != '1':
                    continue
                self.DFS(grid, i, j)
                count += 1
        return count
    
    def num_islands_2(self, grid: List[List[str]]) -> int:
        """
        BFS。
        遍历二维数组，如果找到一个位置为 1，就将其加入搜索队列，开始广度优先搜索，
        并将搜索过程中的 1 置为 0。
        """
        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != '1':
                    continue
                
                # 搜索到的 1 置为 0。
                grid[i][j] = '0'
                # 岛屿数量加 1。
                count += 1
                
                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    # 构造水平，垂直方向的相邻节点坐标。
                    for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        # 将坐标合法且值为 1 的坐标加入队列。
                        if 0 <= r < row and 0 <= c < col and grid[r][c] == '1':
                            # 将访问过的坐标置为 0。
                            grid[r][c] = '0'
                            queue.append((r, c))
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
