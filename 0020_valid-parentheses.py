"""
有效的括号

链接：https://leetcode-cn.com/problems/valid-parentheses

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true

我的解题思路：
1. 用栈的先进后出特性解决。
若字符串长度不为偶数，说明一定存在无法匹配的括号，直接返回 False。
迭代字符串的每个字符，若是左括号，则入栈，若是右括号，则弹出栈顶元素并判断是否与右括号配对。

时间复杂度：O(n)，其中 nn 是字符串 s 的长度。
空间复杂度：O(n+∣Σ∣)，其中 Σ 表示字符集，本题中字符串只包含 6 种括号，∣Σ∣=6。
栈中的字符数量为 O(n)，而哈希映射使用的空间为 O(∣Σ∣)，相加即可得到总空间复杂度。


"""
import unittest


class Solution:
    def is_valid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        right_parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for char in s:
            if char not in right_parenthesis:
                # 左括号入栈。
                stack.append(char)
                continue

            if not stack or right_parenthesis[char] != stack.pop():
                # 栈为空，表示右括号出现在左括号之前；栈顶的左括号与当前右括号不匹配。
                return False

        # 栈未空的话，表示存在未配对的括号。
        return not stack


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_valid(self) -> None:
        self.assertTrue(self.s.is_valid(''))
        self.assertTrue(self.s.is_valid('['))
        self.assertTrue(self.s.is_valid('()'))
        self.assertTrue(self.s.is_valid('()[]{}'))
        self.assertTrue(self.s.is_valid('{[]}'))
        self.assertFalse(self.s.is_valid('(['))
        self.assertFalse(self.s.is_valid('([)]'))


if __name__ == '__main__':
    unittest.main()
