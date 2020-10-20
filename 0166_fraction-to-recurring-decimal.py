"""
分数到小数

链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:
输入: numerator = 1, denominator = 2
输出: "0.5"

示例 2:
输入: numerator = 2, denominator = 1
输出: "2"

示例 3:
输入: numerator = 2, denominator = 3
输出: "0.(6)"

官方解法：
1.
除法运算过程，难点在于替换循环数以及特殊情况的考虑。

特殊情况：
 - 正负号
 - 是否有小数点，也就是是否能被整除
 - 溢出：−2147483648/-1
 - 有小数点的话，是否存在循环

"""
import unittest


class OfficialSolution:
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        # 特殊情况。
        if numerator == 0:
            return '0'

        # 存储正负号、整数部分、小数点、小数部分，用于最后返回拼接后的字符串。
        res = []

        # 若为 fasle，说明结果是负数；否则，结果为正数。
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')

        # 取正数。
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 添加整数部分。
        res.append(str(numerator // denominator))
        # 若余数为 0，说明没有小数点和小数，直接返回结果。
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)

        # 添加小数点。
        res.append('.')
        # 记录余数及位置，用于遇到循环时插入括号。
        d = {}
        # 余数不为零，说明可以继续除。
        while remainder != 0:
            # 存在已经出现过的余数，说明存在循环。
            if remainder in d:
                # 在之前出现的位置插入括号。
                res.insert(d[remainder], '(')
                res.append(')')
                break

            # 记录余数及位置。
            d[remainder] = len(res)
            # 余数加 0，继续除。
            remainder *= 10
            # 添加小数。
            res.append(str(remainder // denominator))
            # 更新余数。
            remainder = remainder % denominator

        return ''.join(res)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_fraction_to_decimal(self) -> None:
        self.assertEqual(
            self.s.fraction_to_decimal(1, 2),
            '0.5',
        )
        self.assertEqual(
            self.s.fraction_to_decimal(2, 1),
            '2',
        )
        self.assertEqual(
            self.s.fraction_to_decimal(2, 3),
            '0.(6)',
        )
        self.assertEqual(
            self.s.fraction_to_decimal(-2147483648, -1),
            '2147483648',
        )
        self.assertEqual(
            self.s.fraction_to_decimal(-50, 8),
            '-6.25',
        )


if __name__ == '__main__':
    unittest.main()
