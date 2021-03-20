"""
计算器

链接：https://leetcode-cn.com/problems/calculator-lcci

给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。 整数除法仅保留整数部分。

示例 1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

解法：
1. 栈。
算法：
1）遍历字符串：
1.1）遇到空格时，跳过。
1.2）遇到数字时，可能不止一位，需要向后查找，获取完整的数字 a，并入栈。
1.3）遇到运算符号时，查找下一位完整的数字 b，并根据运算符做下列计算：
1.3.1）遇到 + 号，直接将数字 b 入栈。
1.3.2）遇到 - 号，将数字 -b 入栈。
1.3.3）遇到 * 号，弹出栈顶元素 c 并乘上 b，再入栈。
1.3.4）遇到 / 号，弹出栈顶元素 c 并除以 b，只保留整数部分再入栈。
1.4）栈中剩余数字之和就是答案。


"""
import unittest
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """栈。"""
        stack: List[int] = []

        i = 0
        while i < len(s):
            # 遇到空格，跳过。
            if s[i] == " ":
                i += 1
                continue

            # 遇到数字，向后查找，获取完整数字。
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # 将数字入栈。
                stack.append(num)
                continue

            # 遇到运算符。
            if s[i] in "+-*/":
                # 记录运算符。
                sign = s[i]

                i += 1
                # 跳过空格。
                while i < len(s) and s[i] == " ":
                    i += 1

                # 获取运算符后的完整的数字。
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                # 遇到 + 号，将运算符后的数字入栈。
                if sign == "+":
                    stack.append(num)

                # 遇到 - 号，将运算符后的数字取反入栈。
                elif sign == "-":
                    stack.append(-num)

                # 遇到 * 号，将栈顶数字取出，与运算符后的数字相乘后再入栈。
                elif sign == "*":
                    stack.append(stack.pop() * num)

                # 遇到 / 号，将栈顶数字取出，与运算符后的数字相除，只保留整数部分后再入栈。
                elif sign == "/":
                    stack.append(int(stack.pop() / num))

                continue

        # 将栈内剩余数字相加即为结果。
        return sum(stack)


class Case:
    def __init__(self, s: str, want: int):
        self.s = s
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_calculate(self) -> None:
        test_cases: List[Case] = [
            Case("3+2*2", 7),
            Case(" 3/2 ", 1),
            Case(" 3+5 / 2 ", 5),
            Case("14-3/2", 13),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.calculate(tc.s))


if __name__ == "__main__":
    unittest.main()
