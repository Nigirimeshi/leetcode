"""
最长公共前缀

链接：https://leetcode-cn.com/problems/longest-common-prefix

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower", "flow", "flight"]
输出: "fl"

示例 2:
输入: ["dog", "racecar", "car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z。

官方解题方案：
1. 横向扫描。
用 LCP(S1...Sn) 表示字符串 S1...Sn 的最长公共前缀。
可以得到以下结论：LCP(S1...Sn) = LCP(LCP(LCP(S1, S2), S3), ...Sn)
基于该结论，可以得到一种查找字符串数组中的最长公共前缀的简单方法。
依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
如果在尚未遍历完所有的字符串时，最长公共前缀已经是空串，则最长公共前缀一定是空串，因此不需要继续遍历剩下的字符串，直接返回空串即可。

时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
空间复杂度：O(1)。使用的额外空间复杂度为常数。

"""
import unittest
from typing import List


class OfficialSolution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        prefix, length = strs[0], len(strs)
        for i in range(1, length):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1: str, str2: str) -> str:
        length, idx = min(len(str1), len(str2)), 0
        while idx < length and str1[idx] == str2[idx]:
            idx += 1
        return str1[:idx]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_longest_common_prefix(self) -> None:
        self.assertEqual(
            self.s.longest_common_prefix(["flower", "flow", "flight"]),
            'fl',
        )
        self.assertEqual(
            self.s.longest_common_prefix(["dog", "racecar", "car"]),
            '',
        )


if __name__ == '__main__':
    unittest.main()
