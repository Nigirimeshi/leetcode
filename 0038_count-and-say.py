"""
外观数列

链接：https://leetcode-cn.com/problems/count-and-say

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221

第一项是数字 1
描述前一项，这个数是 1 即 “一个 1 ”，记作 11
描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

示例 1:
输入: 1
输出: "1"
解释：这是一个基本样例。

示例 2:
输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而值 = 2；类似 "1" 可以读作 "11"。
所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

我的解题方案：
1. 递归 + 双指针。
递归边界条件明显是 n 为 1 时，返回 '1'；
利用数组记录字符依次出现的次数；
拼接结果字符串。

"""
import unittest
import collections


class Solution:
    def count_and_say(self, n: int) -> str:
        # 递归终止条件。
        if n == 1:
            return '1'

        s = self.count_and_say(n - 1)

        # 记录字符顺序及连续出现次数。
        counter = []
        length = len(s)
        i = 0
        while i <= length - 1:
            j, count = i + 1, 1
            while j <= length - 1:
                if s[i] == s[j]:
                    count += 1
                else:
                    break
                j += 1
            counter.append((s[i], count))
            i += count

        ans = ''
        for k, v in counter:
            ans += str(v) + k
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_count_and_say(self) -> None:
        self.assertEqual(
            self.s.count_and_say(1),
            '1',
        )
        self.assertEqual(
            self.s.count_and_say(2),
            '11',
        )
        self.assertEqual(
            self.s.count_and_say(3),
            '21',
        )
        self.assertEqual(
            self.s.count_and_say(4),
            '1211',
        )
        self.assertEqual(
            self.s.count_and_say(5),
            '111221',
        )
        self.assertEqual(
            self.s.count_and_say(6),
            '312211',
        )


if __name__ == '__main__':
    unittest.main()
