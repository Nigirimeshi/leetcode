"""
有效的字母异位词

链接：https://leetcode-cn.com/problems/valid-anagram

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

我的解题方案：
1. 用哈希表分别记录两个字符串的元素及数量，哈希表相同即为 True。
时间复杂度：O(n)。时间复杂度为 O(n) 因为访问计数器表是一个固定的时间操作。
空间复杂度：O(1)。尽管我们使用了额外的空间，但是空间的复杂性是 O(1)，因为无论 N 有多大，表的大小都保持不变。

"""
import unittest
import collections


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_anagram(self) -> None:
        self.assertTrue(
            self.s.is_anagram('anagram', 'nagaram')
        )


if __name__ == '__main__':
    unittest.main()
