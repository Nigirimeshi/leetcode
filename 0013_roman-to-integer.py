"""
罗马数字转整数

链接：https://leetcode-cn.com/problems/roman-to-integer

标签：数学

罗马数字包含以下七种字符: I，V，X，L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如：
罗马数字 2 写做 II，即为两个并列的 1。12 写做 XII，即为 X+II。 27 写做 XXVII, 即为 XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。

这个特殊的规则只适用于以下六种情况：
I 可以放在 V(5) 和 X(10) 的左边，来表示 4 和 9。
X 可以放在 L(50) 和 C(100) 的左边，来表示 40 和 90。
C 可以放在 D(500) 和 M(1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

提示：
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。

我的解题思路：
1. 建立数字映射字典，建立条件字典。
计算规则：
1) 罗马数字中小的数字在大的数字的右边时，做加法；
2) 罗马数字中小的数字在大的数字的左边，且符合特殊规则时，做减。

时间复杂度：O(n)
空间复杂度：O(1)


官方解法：
1. 遍历。
然后从左到右遍历每个字符，如果 s[i] < s[i+1]，就将结果减去 s[i] 代表的数字；否则，将结果加上 s[i] 代表的数字。

时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest


class Solution:
    def roman_to_int(self, s: str) -> int:
        romain_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        i = 0
        sums = 0
        while i < len(s) - 1:
            _curr = romain_dict.get(s[i])
            _next = romain_dict.get(s[i + 1])
            if _curr >= _next:
                sums += _curr
                i += 1
                continue

            sums = sums + _next - _curr
            i += 2

        if i == len(s) - 1:
            sums += romain_dict.get(s[i])
        return sums


class OfficialSolution:
    def roman_to_int(self, s: str) -> int:
        romain_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sums = 0
        for idx in range(len(s) - 1):
            curr = romain_dict.get(s[idx])
            if curr >= romain_dict.get(s[idx + 1]):
                sums += curr
            else:
                sums -= curr
        return sums + romain_dict.get(s[-1])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_roman_to_int(self) -> None:
        self.assertEqual(
            self.s.roman_to_int('III'),
            3,
        )
        self.assertEqual(
            self.s.roman_to_int('IV'),
            4,
        )
        self.assertEqual(
            self.s.roman_to_int('IX'),
            9,
        )
        self.assertEqual(
            self.s.roman_to_int('LVIII'),
            58,
        )
        self.assertEqual(
            self.s.roman_to_int('MCMXCIV'),
            1994,
        )
        self.assertEqual(
            self.s.roman_to_int('XLIX'),
            49,
        )
        self.assertEqual(
            self.s.roman_to_int('CMXCIX'),
            999,
        )
        self.assertEqual(
            self.s.roman_to_int('DCXXI'),
            621,
        )


if __name__ == '__main__':
    unittest.main()
