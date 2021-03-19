"""
有效的括号字符串

链接：https://leetcode-cn.com/problems/valid-parenthesis-string

给定一个只包含三种字符的字符串：（ ，）和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 (。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。

示例 1:
输入: "()"
输出: True

示例 2:
输入: "(*)"
输出: True

示例 3:
输入: "(*))"
输出: True

注意:
字符串大小将在 [1，100] 范围内。

解法：
1. 贪心法。
算法：
1）用 lo，hi 表示 “可能多余的左括号”，一个表示下界，一个表示上界。
2）遍历字符串：
2.1）遇到左括号：lo++, hi++
2.2）遇到星号：lo--（保证 lo 不小于 0）, hi++
2.3）遇到右括号：lo--（保证 lo 不小于 0）, hi--
2.4）若 hi 小于 0，说明就算把所有星号变成左括号也不够了，直接返回 false
3）如果 lo 不等于 0，说明有多的左括号，返回 false

时间复杂度：O(N)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def check_valid_string(self, s: str) -> bool:
        """贪心法。"""
        if not s:
            return True

        lo, hi = 0, 0
        for c in s:
            if c == "*":
                if lo > 0:
                    lo -= 1
                hi += 1

            elif c == "(":
                lo += 1
                hi += 1

            elif c == ")":
                if lo > 0:
                    lo -= 1
                hi -= 1

            # 就算把所有的星号当作左括号也不够了。
            if hi < 0:
                return False

        # 存在多余的左括号。
        return lo == 0


class Case:
    def __init__(self, s: str, want: bool):
        self.s = s
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_check_valid_string(self) -> None:
        test_cases: List[Case] = [
            Case("", True),
            Case("()", True),
            Case("(*)", True),
            Case("(*))", True),
            Case("(()())", True),
            Case("(**))", True),
            Case("(*)))", False),
            Case("(", False),
            Case(")", False),
            Case(")(", False),
            Case(")()", False),
            Case(")*(", False),
            Case(")()(", False),
            Case(
                "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
                True,
            ),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.check_valid_string(tc.s), f"s: {tc.s}")


if __name__ == "__main__":
    unittest.main()
