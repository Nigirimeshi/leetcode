"""
移出无效的括号

链接：https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses

给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')'（可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下任意一条要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」

示例 1：
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。

示例 2：
输入：s = "a)b(c)d"
输出："ab(c)d"

示例 3：
输入：s = "))(("
输出：""
解释：空字符串也是有效的

示例 4：
输入：s = "(a(b(c)d)"
输出："a(b(c)d)"

提示：
1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母

解法：
1. 栈。

"""
import unittest
from collections import defaultdict
from typing import List, Tuple, Union


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        """
        栈。
        """
        stack: List[Tuple[str, int]] = []
        ans: List[str] = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))

            if c == ")":
                # 栈为空，说明 ")" 是多余的，用空字符代替 ")"。
                if len(stack) == 0:
                    ans.append("")
                    continue
                stack.pop()

            ans.append(c)

        # 栈不为空，说明存在多于的 "("，依次出栈，并替换为空字符。
        while stack:
            c, i = stack.pop()
            ans[i] = ""

        return "".join(ans)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_min_remove_to_make_valid(self) -> None:
        self.assertEqual(
            "lee(t(c)o)de",
            self.s.min_remove_to_make_valid("lee(t(c)o)de)"),
        )

        self.assertEqual(
            "",
            self.s.min_remove_to_make_valid("))(("),
        )

        self.assertEqual(
            "abc",
            self.s.min_remove_to_make_valid("))a(b(c"),
        )

        self.assertEqual(
            "a(b(c)d)",
            self.s.min_remove_to_make_valid("(a(b(c)d)"),
        )


if __name__ == "__main__":
    unittest.main()
