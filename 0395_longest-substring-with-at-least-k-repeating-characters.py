"""
至少有 K 个重复字符的最长字串

链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters

找到给定字符串（由小写字符组成）中的最长子串 T ，要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:
输入:
s = "aaabb", k = 3
输出:
3
最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2:
输入:
s = "ababbc", k = 2
输出:
5
最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

官方解法：
1. 分治。
边界条件：若字符串 s 长度小于 k，直接返回 0。
递归：
1）首先找出给定字符串中出现次数最少的字符 c。
2）若 c 的出现次数大于等于 k，说明该字符串满足条件，返回该字符串长度。
3）若 c 的出现次数小于 k，则以 c 为边界点，将字符串分为多个子串。
4）对多个子串进行上述递归判断，找出各个子串中最长的并返回。


"""
import unittest


class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        """分支（递归）。"""
        # 若字符串比 k 小，说明不存在题目要求的子串。
        if len(s) < k:
            return 0
        
        # 1. 找出字符串 s 中出现次数最少的字符。
        c = min(set(s), key=s.count)
        # 2. 若 c 的次数大于等于 k，即字符串 s 中所有字符出现次数均大于 k，返回字符串 s 长度即可。
        if s.count(c) >= k:
            return len(s)
        # 3. 若 c 的次数小于 k，则以 c 为子串分割点，递归各个子串，并进行上列判断。
        return max(self.longest_substring(_, k) for _ in s.split(c))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_longest_substring(self) -> None:
        self.assertEqual(
            self.s.longest_substring('aaabb', 3),
            3,
        )
        self.assertEqual(
            self.s.longest_substring('ababbc', 2),
            5,
        )


if __name__ == '__main__':
    unittest.main()
