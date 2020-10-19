"""
两数相除

链接：https://leetcode-cn.com/problems/divide-two-integers

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

提示：
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

参考解法：


"""
import unittest

MAX_INT = 2 ** 31 - 1
MIN_INT = -(2 ** 31)


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > MIN_INT:
                return -dividend
            return MAX_INT

        # sign 为 true，表示结果是负数，sign 为 false，表示结果是正数。
        sign = (dividend > 0) ^ (divisor > 0)
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else - divisor
        ans = self.div(a, b)
        if not sign:
            return MAX_INT if ans > MAX_INT else ans
        return -ans

    def div(self, a, b: int) -> int:
        if a < b:
            return 0
        count = 1
        tmp_b = b
        while (tmp_b + tmp_b) <= a:
            count = count + count  # 最小解翻倍。
            tmp_b = tmp_b + tmp_b  # 当前测试值也翻倍。
        return count + self.div(a - tmp_b, b)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_divide(self) -> None:
        self.assertEqual(
            self.s.divide(10, 3),
            3,
        )
        self.assertEqual(
            self.s.divide(7, -3),
            -2,
        )
        self.assertEqual(
            self.s.divide(-2147483648, -1),
            2147483647,
        )
        self.assertEqual(
            self.s.divide(1, -1),
            -1,
        )


if __name__ == '__main__':
    unittest.main()
