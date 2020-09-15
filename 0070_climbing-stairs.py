"""
爬楼梯

链接：https://leetcode-cn.com/problems/climbing-stairs

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

官方解法：
1. 递归。
时间复杂度：O(n)
空间复杂度：O(n)


2. 动态规划。
时间复杂度：O(logn)
空间复杂度：O(n)


3. 动态规划（优化空间）。
时间复杂度：O(logn)
空间复杂度：O(1)


4. 斐波那契数列公式。
时间复杂度：O(logn)
空间复杂度：O(1)

"""
import unittest
import functools


class OfficialSolution:
    @functools.lru_cache(100)
    def climb_stairs(self, n: int) -> int:
        """递归。"""
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

    def climb_stairs_2(self, n: int) -> int:
        """动态规划。"""
        dp = {
            1: 1,
            2: 2,
        }
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climb_stairs_3(self, n: int) -> int:
        """动态规划（优化空间）。"""
        if n == 1 or n == 2:
            return n
        a, b, tmp = 1, 2, 0
        for i in range(3, n + 1):
            tmp = a + b
            a = b
            b = tmp
        return tmp

    def climb_stairs_4(self, n: int) -> int:
        """斐波那契数列。"""
        import math
        sqrt5 = 5 ** 0.5
        fibin = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(fibin / sqrt5)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_climb_stairs(self) -> None:
        self.s.climb_stairs(3)


if __name__ == '__main__':
    unittest.main()
