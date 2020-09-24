"""
字母异位词分组

链接：https://leetcode-cn.com/problems/group-anagrams

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

我的解题思路：
1. 排序数组分类。
边界条件：输入 []，返回 []。
关键：字母顺序不同的字符串排序后是相同的。

时间复杂度：O(N*KlogK)。N 为数组长度，L 是 strs 中字符串的最大长度。
空间复杂度：O(NK)。

官方解法：
1. 排序数组分类。
当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
维护一个映射 ans : {String -> List}，其中每个键 K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 K。
在 Java 中，我们将键存储为字符串，例如，code。 在 Python 中，我们将键存储为散列化元组，例如，('c', 'o', 'd', 'e')。

时间复杂度：O(NKlogK)，其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。
遍历每个字符串时，外部循环复杂度为 O(N)。在 O(KlogK) 的时间内对每个字符串排序。

空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。

2. 按计数分类。
当且仅当字符串的字符出现出现相同时，两个字符串是字符异位词。
可以将每个字符串 s 转化为字符数 count，由 26 个非负数组成，表示各字符串的数量。

时间复杂度：O(NK)，其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。计算每个字符串的字符串大小是线性的，我们统计每个字符串。
空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。

"""
import unittest
import collections
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        groups = {}
        for string in strs:
            # 将字符串排序，字母顺序不同的字符串，排序后是相同的。
            order_str = ''.join(sorted(string))
            # 按排序后的字符串分组。
            if not groups.__contains__(order_str):
                groups[order_str] = []
            groups[order_str].append(string)

        ans = []
        for v in groups.values():
            ans.append(v)

        return ans


class OfficialSolution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """排序数组分类。"""
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def group_anagrams_2(self, strs: List[str]) -> List[List[str]]:
        """按计数分类。"""
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_group_anagrams(self) -> None:
        print(self.s.group_anagrams(test_cases[0]))
        print(self.s.group_anagrams(test_cases[1]))


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_group_anagrams(self) -> None:
        print(self.s.group_anagrams(test_cases[0]))
        print(self.s.group_anagrams(test_cases[1]))


if __name__ == '__main__':
    unittest.main()
