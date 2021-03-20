"""
基本计算器

链接：https://leetcode-cn.com/problems/basic-calculator

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：
1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

解法：
1. 栈。

"""
import unittest
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """栈。"""
        num, sign, ans = 0, 1, 0

        # 暂存括号前的数字和运算符。
        stack: List[int] = []

        for c in s:
            # 遇到数字，累加。
            if c.isdigit():
                num = num * 10 + int(c)

            # 遇到运算符。
            elif c in "+-":
                # 累加之前的数字。
                ans += sign * num
                # 重置数字。
                num = 0
                # 更新运算符。
                sign = 1 if c == "+" else -1

            # 遇到左括号。
            elif c == "(":
                # 暂存左括号前的数字的和与运算符。
                stack.append(ans)
                stack.append(sign)
                # 重置累加和与运算符，用于计算括号内的表达式。
                ans = 0
                sign = 1

            # 遇到右括号。
            elif c == ")":
                # 累加括号内最后的数字。
                ans += sign * num
                # 重置数字。
                num = 0
                # 在括号内数字和的前加上之前暂存的运算符。
                ans *= stack.pop()
                # 加上左括号前表达式的和。
                ans += stack.pop()

        # 因为上述循环遇到运算符时，才会累加之前的结果，所以最后会可能会剩余一个运算符和数字。
        ans += sign * num
        return ans


class Case:
    def __init__(self, s: str, want: int):
        self.s = s
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_calculate(self) -> None:
        test_cases: List[Case] = [
            Case("1 + 1", 2),
            Case(" 2-1 + 2 ", 3),
            Case("(1+(4+5+2)-3)+(6+8)", 23),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.calculate(tc.s))


if __name__ == "__main__":
    unittest.main()
