"""
整数反转

链接：https://leetcode-cn.com/problems/reverse-integer

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−2^31, 2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

我的解题方案：
1. 数字转成字符串，反转后还原为数字。若数字小于零，单独标记为负数；若数字溢出，返回 0。

官方解法：
1. 每次构建反转整数的一位数字。在每次构建时，预先检查向上一次的构建结果加新构建的数字是否会导致溢出。
重复 “弹出” x 的最后一位数字，并将它 “追加” 到 res 的尾部，最后得到的 res 将与 x 相反。
时间复杂度：O(log(x))，x 中大约有 log10(x) 位数字。
空间复杂度：O(1)

"""
import unittest


class Solution:
    def reverse(self, x: int) -> int:
        negative_number = False
        if x < 0:
            negative_number = True
            x = 0 - x

        s = str(x)
        s = s[::-1]
        y = int(s)
        if negative_number:
            y = 0 - y
        if y < pow(-2, 31) or y > pow(2, 31) - 1:
            return 0
        return y


class OfficialSolution:
    def reverse(self, x: int) -> int:
        # 取 x 的绝对值，用于简化判断数字是否溢出。
        y, res = abs(x), 0

        # 溢出值大小，x > 0 时，该值为 2^31 - 1；x < 0 时，值为 2^31。
        overflow_value = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            # 重复 “弹出” y 的最后一位数字，并将它 “追加” 到 res 的尾部。
            res = res * 10 + y % 10

            # 判断结果是否溢出
            if res > overflow_value:
                return 0
            y //= 10

        # 当 x 大于 0 时，返回正数，小于 0 时，返回负数。
        return res if x > 0 else -res


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_reverse(self) -> None:
        self.assertEqual(self.s.reverse(123), 321)


if __name__ == '__main__':
    unittest.main()
