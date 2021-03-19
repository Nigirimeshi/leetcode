"""
删除无效的括号

链接：https://leetcode-cn.com/problems/remove-invalid-parentheses

给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

示例 1:
输入: "()())()"
输出: ["()()()", "(())()"]

示例 2:
输入: "(a)())()"
输出: ["(a)()()", "(a())()"]

示例 3:
输入: ")("
输出: [""]

示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]

示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

示例 3：
输入：s = ")("
输出：[""]

提示：
1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

解法：
1. BFS。
1）广度优先遍历，根节点是 s，穷举去除任一 ( 或 ) 后的子串，并用集合存储，避免重复子串，该集合将作为根节点的下一层。
2）遍历子串集合，检查是否各子串是否合法，若合法，则加入结果集。
3）结果集数量大于 0，说明存在删除了最小括号，且合法的子串，返回结果集。

2. 回溯。


"""
import unittest
from typing import List, Set


class Solution:
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        """BFS。"""
        # 存放有效子串。
        ans: List[str] = []

        # 存储当前遍历层的子串集合。
        level: Set[str] = {s}
        while True:
            # 遍历当前层中的子串。
            for sub_str in level:
                # 检查是否有效。
                if self.is_valid(sub_str):
                    ans.append(sub_str)

            # 已找到了删除最小数量括号后，有效的子串。
            if len(ans) > 0:
                return ans

            # 存储下一层的所有子串集合。
            next_level: Set[str] = set()
            # 遍历当前层，生成下一层的子串。
            for sub_str in level:
                for i in range(len(sub_str)):
                    if sub_str[i] in "()":
                        next_level.add(sub_str[:i] + sub_str[i + 1 :])

            # 遍历下一层。
            level = next_level

    def is_valid(self, s: str) -> bool:
        """
        判断字符串括号是否有效。
        """
        left = 0
        for c in s:
            if c == "(":
                left += 1

            elif c == ")":
                if left == 0:
                    return False
                left -= 1

        return left == 0


class Case:
    def __init__(self, s: str, want: List[str]):
        self.s = s
        self.want = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_remove_invalid_parentheses(self) -> None:
        test_case: List[Case] = [
            Case("()())()", ["()()()", "(())()"]),
            Case("(a)())()", ["(a)()()", "(a())()"]),
            Case(")(", [""]),
        ]
        for tc in test_case:
            self.assertSetEqual(
                set(tc.want), set(self.s.remove_invalid_parentheses(tc.s))
            )


if __name__ == "__main__":
    unittest.main()
