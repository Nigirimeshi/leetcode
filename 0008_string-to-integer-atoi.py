"""
字符串转换整数 (atoi)

链接：https://leetcode-cn.com/problems/string-to-integer-atoi

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：
本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为[−2^31, 2^31 − 1]。
如果数值超过这个范围，请返回 INT_MAX (2^31− 1) 或 INT_MIN (−2^31) 。


示例 1:
输入: "42"
输出: 42

示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。

示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。因此返回 INT_MIN (−2^31) 。

我的解题方案：
1. 快慢指针。

官方解法：
1. 正则表达式。
2. 自动机。
字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。
因此，为了有条理地分析每个输入字符的处理方法，我们可以使用自动机这个概念：
我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。
这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。

            ' '     +/-         number  	other
start	    start   signed	    in_number	end
signed	    end	    end	        in_number	end
in_number	end	    end	        in_number	end
end	        end	    end	        end	        end

接下来编程部分就非常简单了：我们只需要把上面这个状态转换表抄进代码即可。
另外自动机也需要记录当前已经输入的数字，只要在 s' 为 in_number 时，更新我们输入的数字，即可最终得到输入的数字。

"""
import re
import unittest


class Solution:
    def my_atoi(self, s: str) -> int:
        negative_number = False
        left, right = 0, 0
        clear_str = s.lstrip()
        n = len(clear_str)

        if clear_str == '':
            return 0

        for i in range(n):
            char = clear_str[i]
            if char != '+' and char != '-' and not char.isnumeric():
                return 0

            if char.isnumeric():
                left = i

            if char == '+' or char == '-':
                if char == '-':
                    negative_number = True
                if i + 1 > n - 1:
                    return 0
                if clear_str[i + 1].isnumeric():
                    continue
                else:
                    return 0

            right = left + 1
            if right > n - 1:
                break

            while right <= n - 1 and clear_str[right].isnumeric():
                right += 1
            break

        num_str = clear_str[left:right]
        num = int(num_str)
        int_max = pow(2, 31) - 1
        int_min = pow(2, 31)
        spillover_value = int_min if negative_number else int_max
        if num > spillover_value:
            if negative_number:
                return -int(int_min)
            else:
                return int_max
        return num if not negative_number else -num


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    """
                ' '     +/-         number  	other
    start	    start   signed	    in_number	end
    signed	    end	    end	        in_number	end
    in_number	end	    end	        in_number	end
    end	        end	    end	        end	        end
    """

    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class OfficialSolution:
    def my_atoi(self, s: str) -> int:
        """正则表达式解法"""
        return max(
            min(
                int(*re.findall('^[\+\-]?\d+', s.lstrip())),
                2 ** 31 - 1
            ),
            -2 ** 31,
        )

    def my_atoi_2(self, s: str) -> int:
        """自动机解法"""
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_my_atoi(self) -> None:
        self.assertEqual(
            self.s.my_atoi(""),
            0,
        )
        self.assertEqual(
            self.s.my_atoi(" "),
            0,
        )
        self.assertEqual(
            self.s.my_atoi("+"),
            0,
        )
        self.assertEqual(
            self.s.my_atoi("-"),
            0,
        )
        self.assertEqual(
            self.s.my_atoi("42"),
            42,
        )
        self.assertEqual(
            self.s.my_atoi("-42"),
            -42,
        )
        self.assertEqual(
            self.s.my_atoi("  42"),
            42,
        )
        self.assertEqual(
            self.s.my_atoi("  -42"),
            -42,
        )


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_my_atoi_2(self) -> None:
        self.assertEqual(
            self.s.my_atoi_2(""),
            0,
        )
        self.assertEqual(
            self.s.my_atoi_2(" "),
            0,
        )
        self.assertEqual(
            self.s.my_atoi_2("+"),
            0,
        )
        self.assertEqual(
            self.s.my_atoi_2("-"),
            0,
        )
        self.assertEqual(
            self.s.my_atoi_2("42"),
            42,
        )
        self.assertEqual(
            self.s.my_atoi_2("-42"),
            -42,
        )
        self.assertEqual(
            self.s.my_atoi_2("  42"),
            42,
        )
        self.assertEqual(
            self.s.my_atoi_2("  -42"),
            -42,
        )


if __name__ == '__main__':
    unittest.main()
