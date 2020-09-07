"""
字符串中的第一个唯一字符

链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

我的解题方案：
1. 双层遍历
时间复杂度：O(n^2)
2. 遍历字符串，用哈希表记录各字符次数；再次遍历，返回哈希表中字符次数为 1 的。
"""
import unittest
import collections


class Solution:
    def first_uniq_char(self, s: str) -> int:
        counter = collections.Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_first_uniq_char(self) -> None:
        self.assertEqual(
            self.s.first_uniq_char('leetcode'),
            0,
        )


if __name__ == '__main__':
    unittest.main()
