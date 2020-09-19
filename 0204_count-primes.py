"""
计算质数

标签：数学

链接：https://leetcode-cn.com/problems/count-primes/

统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

我的解题思路：
1. 遍历 0 到 n，检查每个数是否为质数。
时间复杂度：O(n^2)
空间复杂度：O(1)

官方解法：
1. 厄拉多塞筛法。
循环时排除当前数字的所有倍数。

"""
import unittest
import math


class Solution:
    def count_primes(self, n: int) -> int:
        """暴力（优化时间）。（提交超时）"""
        count = 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, math.isqrt(i) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count


class OfficialSolution:
    def count_primes(self, n: int) -> int:
        # 先设所有数为质数。
        signs = [True] * n
        count = 0
        for i in range(2, n):
            if signs[i]:
                count += 1
            # 排除 i 的所有倍数，将其设为非质数。
            j = i + i
            while j < n:
                signs[j] = False
                j += i
        return count


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_count_primes(self) -> None:
        self.assertEqual(
            self.s.count_primes(10),
            4,
        )
        self.assertEqual(
            self.s.count_primes(3),
            1,
        )
        self.assertEqual(
            self.s.count_primes(2),
            0,
        )
        self.assertEqual(
            self.s.count_primes(499979),
            41537,
        )
        self.assertEqual(
            self.s.count_primes(1500000),
            114155,
        )


if __name__ == '__main__':
    unittest.main()
