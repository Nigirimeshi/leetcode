"""
基本计算器 III

链接：https://leetcode-cn.com/problems/basic-calculator-iii

实现一个基本的计算器来计算简单的表达式字符串。

表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。

你可以假定给定的表达式总是有效的。所有的中间结果的范围为 [-231, 231 - 1] 。

示例 1：
输入：s = "1+1"
输出：2

示例 2：
输入：s = "6-4/2"
输出：4

示例 3：
输入：s = "2*(5+5*2)/3+(6/2+8)"
输出：21

示例 4：
输入：s = "(2+6*3+5-(3*14/7+2)*5)+3"
输出：-12

示例 5：
输入：s = "0"
输出：0

提示：
1 <= s <= 104
s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
s 是一个 有效的 表达式

解法：
1. 栈 + 递归。（提交通过）
算法：
1）跳过空格。

2）遇到数字，向后获取完整数字，并入栈。

3）遇到运算符（+-*/）：
3.1）运算符后面是空格，跳过。
3.2）获取运算符后面的数字 next_num，分 2 种情况：
3.2.1）运算符后面是左括号：
3.2.1.1）递归计算括号内表达式的值（包含左右括号）。
3.2.1.2）弹出栈顶（括号内表达式的值），并将其作为 next_num。
3.2.2）运算符后面是数字：向后获取完整数字，并将其作为 next_num。
3.3）根据运算符四则运算：
3.3.1）+ 号：直接将 next_num 入栈。
3.3.2）- 号：将 —next_num 入栈。
3.3.3）* 号：弹出栈顶，将其乘上 next_num 后入栈。
3.3.4）/ 号：弹出栈顶，将其除以 next_num 并向下取整后入栈。

4）遇到左括号：
4.1）获取对应右括号的下标。
4.2）递归计算括号内表达式的值（不包含左右括号），递归过程中会向栈增加数字。
4.3）递归后栈中新增的数字就是括号内表达式的值，将其逐个弹出累加，并将累加结果入栈。

5）栈中剩余元素的和即为表达式结果。

"""
import unittest
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """栈 + 递归。"""
        stack: List[int] = []

        self.__calculate(stack, s, 0, len(s) - 1)

        return sum(stack)

    def __calculate(self, stack: List[int], s: str, left: int, right: int) -> None:
        i = left
        while i <= right:
            # 遇到空格时，跳过。
            if s[i] == " ":
                i += 1
                continue

            # 遇到数字时，向右获取完整数字，并入栈。
            if s[i].isdigit():
                num = 0
                while i <= right and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                stack.append(num)
                continue

            # 遇到运算符。
            if s[i] in "+-*/":
                # 记录运算符。
                sign = s[i]

                # 跳过空格。
                i += 1
                while i <= right and s[i] == " ":
                    i += 1

                next_num = 0
                # 遇到括号时，递归处理括号内的。
                if s[i] == "(":
                    # 找到对应右括号的下标。
                    j = self.__find_index_of_right_parenthesis(s, i, right)

                    # 递归计算带括号的表达式的值。
                    self.__calculate(stack, s, i, j)
                    # 将括号内的表达式的计算结果作为运算符右边的值。
                    next_num = stack.pop()

                    # 下次循环时，从右括号后的字符开始。
                    i = j + 1

                elif s[i].isdigit():
                    # 获取运算符后的完整数字。
                    while i <= right and s[i].isdigit():
                        next_num = next_num * 10 + int(s[i])
                        i += 1

                # 遇到 + 号，直接将运算符后的数字入栈。
                if sign == "+":
                    stack.append(next_num)

                # 遇到 - 号，将运算符后的数字取反后入栈。
                elif sign == "-":
                    stack.append(-next_num)

                # 遇到 * 号，将栈顶数字取出后乘以 next_num 再入栈。
                elif sign == "*":
                    stack.append(stack.pop() * next_num)

                # 遇到 / 号，将栈顶数字取出后除以 next_num 再入栈。
                elif sign == "/":
                    stack.append(int(stack.pop() / next_num))

                continue

            # 遇到左括号时，计算出对应右括号的边界，然后递归计算括号内表达式的值。
            if s[i] == "(":
                # 找到对应右括号的下标。
                j = self.__find_index_of_right_parenthesis(s, i, right)

                # 记录当前栈的大小。
                stack_size = len(stack)

                # 递归计算括号内的字符串。
                # 注意：s[i] 此时对应 '('，s[j] 此时对应 ')' 的后一位字符，只要括号内的字符串，不要括号。
                self.__calculate(stack, s, i + 1, j - 1)

                # 计算括号内的表达式的值。
                value = 0
                for _ in range(len(stack) - stack_size):
                    value += stack.pop()
                stack.append(value)

                # 下次循环时，从右括号后的字符开始。
                i = j + 1
                continue

    def __find_index_of_right_parenthesis(self, s: str, start: int, end: int):
        """根据左括号的起始位置，找到对应右括号的下标。"""
        # 左括号的数量。
        left_count = 1
        # 从 i + 1 开始向右查找。
        i = start + 1
        # 遍历，直到找到对应右括号的下标。
        while i <= end and left_count != 0:
            if s[i] == "(":
                left_count += 1
            elif s[i] == ")":
                left_count -= 1
            i += 1
        return i - 1


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
            Case("1 + 1", 2),
            Case(" 2-1 + 2 ", 3),
            Case("(1+(4+5+2)-3)+(6+8)", 23),
            Case("1+(3+4)*2", 15),
            Case("2*(5+5*2)/3+(6/2+8)", 21),
            Case("(2+6*3+5-(3*14/7+2)*5)+3", -12),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.calculate(tc.s))


if __name__ == "__main__":
    unittest.main()
