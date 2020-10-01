"""
括号生成

链接：https://leetcode-cn.com/problems/generate-parentheses

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

官方解法：
1. 暴力法。
生成所有 2^2n 个 ( 和 ) 字符构成的序列，然后检查每一个是否有效即可。
算法：
 - 生成所有序列，可以使用递归，长度为 n 的序列就是在长度为 n - 1 的序列前加一个 ( 或 )。
 - 通过遍历序列，检查序列是否有效，使用一个遍历 balance 表示左括号减去右括号的数量，
   在遍历过程中，balance 小于 0 时，或遍历结束后，balance 值不为 0，说明序列无效。

2. 回溯。
方法一的改进版，只在序列仍有效时才添加 ( or )，通过跟踪目前为止放置的左括号和右括号数量来做到。
如果左括号不大于 n，说明可以放一个左括号；如果右括号小于左括号数量，说明可以放一个右括号。

时间复杂度：O((4^n)/根号n)。在回溯过程中，每个答案需要 O(n) 的事件复制到答案数组中。
空间复杂度：O(n)。除了答案数组外，所需要的空间取决于栈的深度，每一层递归需要 O(1) 的空间，最多递归 2n 层，所以空间复杂度为 O(n)。

"""
import unittest
from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        """暴力。"""

        def generate(sequence: List[str]) -> None:
            """递归生成所有序列，并将有效序列加入结果。"""
            # 递归终止条件。
            if len(sequence) == 2 * n:
                if valid(sequence):
                    ans.append(''.join(sequence))
            else:
                sequence.append('(')
                generate(sequence)
                sequence.pop()
                sequence.append(')')
                generate(sequence)
                sequence.pop()

        def valid(sequence: List[str]) -> bool:
            """检查序列是否有效。"""
            balance = 0
            for char in sequence:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1

                # 遍历途中，若 balance 小于 0，说明序列不合法。
                if balance < 0:
                    return False
            # 遍历结束后，左右括号数量相等，序列才合法。
            return balance == 0

        ans = []
        generate([])
        return ans

    def generate_parenthesis_2(self, n: int) -> List[str]:
        """回溯法。"""

        def generate(sequence: List[str], left, right: int) -> None:
            if len(sequence) == 2 * n:
                ans.append(''.join(sequence))
                return

            if left < n:
                # 左括号数量小于 n，说明继续加左括号后，序列仍有效。
                sequence.append('(')
                generate(sequence, left + 1, right)
                sequence.pop()
            if right < left:
                # 右括号数量小于左括号数量，说明继续加右括号后，序列仍有效。
                sequence.append(')')
                generate(sequence, left, right + 1)
                sequence.pop()

        ans = []
        generate([], 0, 0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_generate_parenthesis(self) -> None:
        ans = self.s.generate_parenthesis(3)
        print(ans)


if __name__ == '__main__':
    unittest.main()
