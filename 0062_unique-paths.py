"""
不同路径

链接：https://leetcode-cn.com/problems/unique-paths

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start”）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

问总共有多少条不同的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

官方解法：
1. 动态规划。
dp[i][j] 表示到 (i, j) 这个坐标有多少种路径，最终答案即为 dp[m-1][n-1]。
dp[i][j] = dp[i-1][j] + dp[i][j-1]
dp[i-1][j] 表示从上面走过来的路径条数。
dp[i][j-1] 表示从左边走过来的路径条数。
边界条件：
 - 第一行或第一列永远只有一条路径。

2. 动态规划 - 优化空间。
坐标的值只与左边和上面的值有关，可节省二维数组 dp 的空间占用。

时间复杂度：O(M*N)。
空间复杂度：O(N)。

"""
import unittest


class OfficialSolution:
    def unique_paths(self, m: int, n: int) -> int:
        """动态规划。"""
        # m 行，n 列。
        dp = [[0] * n for _ in range(m)]
        # 第一行路径为 1。
        for j in range(n):
            dp[0][j] = 1
        # 第一列路径为 1。
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def unique_paths_2(self, m: int, n: int) -> int:
        """动态规划 - 优化空间。"""
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_unique_paths(self) -> None:
        self.assertEqual(
            self.s.unique_paths_2(3, 7),
            28,
        )


if __name__ == '__main__':
    unittest.main()
