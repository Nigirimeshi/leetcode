"""
基本计算器 II

标签：字符串

链接：https://leetcode-cn.com/problems/basic-calculator-ii

实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。

整数除法仅保留整数部分。

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

官方解法：
1. 栈。
要考虑乘法、除法的优先级比加法、减法高，可以用栈实现。



"""
import unittest


class Solution:
    def calculate(self, s: str) -> int:
        """栈。"""
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            # 将字符串转数字。
            if c.isnumeric():
                num = num * 10 + int(c)
            
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop()) / num)  # 向下取整。
                
                op = c
                num = 0
        
        return sum(stack)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_calculate(self) -> None:
        # self.assertEqual(
        #     self.s.calculate("3+2*2*5/ 3-2"),
        #     7,
        # )
        self.assertEqual(
            self.s.calculate("3+2*2"),
            7,
        )
        # self.assertEqual(
        #     self.s.calculate(" 3/2 "),
        #     1,
        # )
        # self.assertEqual(
        #     self.s.calculate(" 3+5 / 2 "),
        #     5,
        # )


if __name__ == '__main__':
    unittest.main()
