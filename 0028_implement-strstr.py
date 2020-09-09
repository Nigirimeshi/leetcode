"""
实现 strStr()

链接：https://leetcode-cn.com/problems/implement-strstr

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。
如果不存在，则返回 -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

我的解题方案：
1. 内置字符串函数 index()，加一个 ValueError 异常捕获。

官方解题方案：
1. 子串逐一比较（滑动窗口）- 线性时间复杂度
时间复杂度：O((N - L)L)，其中 N 为 haystack 字符串的长度，L 为 needle 字符串的长度。
          内循环中比较字符串的复杂度为 L，总共需要比较 (N - L) 次。
空间复杂度：O(1)。

"""
import unittest


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
        except ValueError:
            return -1
        return index


class OfficialSolution:
    def str_str(self, haystack: str, needle: str) -> int:
        """子串逐一比较（滑动窗口）- 线性时间复杂度"""
        n, l = len(haystack), len(needle)
        for start in range(n - l + 1):
            if haystack[start:start + l] == needle:
                return start
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_strStr(self):
        self.assertEqual(
            self.s.str_str('hello', 'll'),
            2,
        )
        self.assertEqual(
            self.s.str_str('aaaaa', 'bba'),
            -1,
        )


if __name__ == '__main__':
    unittest.main()
