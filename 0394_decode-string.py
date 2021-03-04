"""
字符串解码

链接：https://leetcode-cn.com/problems/decode-string

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。


示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

解法：
1. 栈。
mult 表示乘数，初始值为 0，sub_str 表示已解码的 [] 内的子串。
算法：
1）遍历给定字符串 s 中每个字符 c。
2）若字符 c 是数字，则使 mult = mult * 10 + int(c)。
3）若字符 c 是字母，则使 res += c
4）若字符 c 是 [，则将 mult 和 res 放入栈中；并重置 mult 为 0，res 为空字符串。
5）若字符 c 是 ]，则取出栈顶元素 [curr_mult, last_res]，使 res = last_res + curr_mult * res
"""
import unittest


class Solution:
    def decode_string(self, s: str) -> str:
        mult, res = 0, ''
        stack = []
        for c in s:
            if c.isnumeric():
                mult = mult * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                stack.append([mult, res])
                mult, res = 0, ''
            elif c == ']':
                # last_res 是一个 [] 内，左边的字符串。
                # 例如：3[a2[c]] 中，last_res = a
                curr_mult, last_res = stack.pop()
                res = last_res + curr_mult * res
        return res


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_decode_string(self) -> None:
        self.assertEqual(
            '',
            self.s.decode_string('')
        )
        self.assertEqual(
            'aaabcbc',
            self.s.decode_string('3[a]2[bc]')
        )
        self.assertEqual(
            'accaccacc',
            self.s.decode_string('3[a2[c]]')
        )


if __name__ == '__main__':
    unittest.main()
