"""
Pow(x, n)

链接：https://leetcode-cn.com/problems/powx-n

实现 pow(x, n)，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2^(-2) = (1/2)^2 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。

我的解题思路：
1. 内置运算符。
x ** n 计算 x 的 n 次幂，
要保留小数点后 5 位，只需将结果乘以 100000 后取证，再除以 100000 即可。

官方解法：
1. 快速幂 + 递归。
假设要计算 x^64，可以按照：x -> x^2 -> x^4 -> x^8 -> x^16 -> x^32 -> x^64 的顺序，每次把上次结果进行平方。
再举个例子 x^77，可以按照：x -> x^2 -> x^4 -> x^9 -> x^19 -> x^38 -> x^77，

如果 n 是负数，相当于求 (1/x)^(-n)。

时间复杂度：O(logN)。
空间复杂度：O(logN)。

2. 快速幂 + 迭代。
x^77，可以按照：x -> x^2 -> x^4 -> x^9 -> x^19 -> x^38 -> x^77，
x * x^4 * x^8 * x^64 恰好等于 x^77，
它们都是 2 的幂次，因为每个额外乘的 x 在之后都会被平方若干次。
而这些指数 1，4，8 和 64，恰好就对应了 77 的二进制表示 1001101 中的每个 1！

时间复杂度：O(logN)。
空间复杂度：O(1)。

"""
import unittest


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        return int(x ** n * 100000) / 100000


class OfficialSolution:
    def my_pow(self, x: float, n: int) -> float:
        """快速幂 + 递归。"""

        def quick_mul(N: int) -> float:
            if N == 0:
                return 1
            y = quick_mul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_my_pow(self) -> None:
        self.assertEqual(
            self.s.my_pow(2.00000, 10),
            1024.00000,
        )
        self.assertEqual(
            self.s.my_pow(2.10000, 3),
            9.26100,
        )
        self.assertEqual(
            self.s.my_pow(2.00000, -2),
            0.25000,
        )


if __name__ == '__main__':
    unittest.main()
