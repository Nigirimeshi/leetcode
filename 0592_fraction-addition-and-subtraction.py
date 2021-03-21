"""
分数加减运算

链接：https://leetcode-cn.com/problems/fraction-addition-and-subtraction

给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。

这个结果应该是不可约分的分数，即最简分数。

如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。

示例 1:
输入:"-1/2+1/2"
输出: "0/1"

示例 2:
输入:"-1/2+1/2+1/3"
输出: "1/3"

示例 3:
输入:"1/3-1/2"
输出: "-1/6"

示例 4:
输入:"5/3+1/3"
输出: "2/1"

说明:
输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是 [1,10]。如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。

解法：
1. 全部通分。（提交通过）
算法：
1. 将表达式中所有的 - 替换成 +-。
2. 按 + 分割表达式。
3. 分别存储分子和分母。
4. 计算分母的最小公倍数。
5. 将所有分子乘上最小公倍数后再相加。
6. 分子和分母进行约分，返回其字符串格式。

"""
import unittest
from typing import List


class Solution:
    def fraction_addition(self, expression: str) -> str:
        """通分。"""
        # 将所有的 - 替换成 +-。
        expression = expression.replace("-", "+-")

        # 按 + 分割。
        fractions = [_ for _ in expression.split("+") if _ != ""]

        # 存储分子和分母。
        numerator: List[int] = []
        denominator: List[int] = []
        for s in fractions:
            n, d = s.split("/")
            numerator.append(int(n))
            denominator.append(int(d))

        # 计算分母的最小公倍数。
        # 例如：1/2 和 1/4 的最小公倍数是 4。
        lcm = 1
        for num in denominator:
            lcm = self.__lowest_common_multiple(lcm, num)

        # 计算分子的和。
        numerator_sum = 0
        for i in range(len(numerator)):
            # 例如：1/2 和 1/4 分子的和为 1 * 2 + 1
            numerator_sum += numerator[i] * (lcm // denominator[i])

        # 分子和分母约分。
        gcm = self.__greatest_common_divisor(numerator_sum, lcm)
        ans = f"{numerator_sum // gcm}/{lcm // gcm}"
        return ans

    def __lowest_common_multiple(self, a: int, b: int) -> int:
        """LCM - 最小公倍数。"""
        return a * b // self.__greatest_common_divisor(a, b)

    @staticmethod
    def __greatest_common_divisor(a: int, b: int) -> int:
        """GCD - 最大公约数。"""
        while b:
            a, b = b, a % b
        return a


class Case:
    def __init__(self, expression: str, want: str):
        self.expression = expression
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_fraction_addition(self):
        test_cases: List[Case] = [
            Case("-1/2+1/2", "0/1"),
            Case("-1/2+1/2+1/3", "1/3"),
            Case("1/3-1/2", "-1/6"),
            Case("5/3+1/3", "2/1"),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.fraction_addition(tc.expression))


if __name__ == "__main__":
    unittest.main()
