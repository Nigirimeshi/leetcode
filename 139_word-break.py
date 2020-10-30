"""
单词拆分

链接：https://leetcode-cn.com/problems/word-break

给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
    注意你可以重复使用字典中的单词。
    
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false


官方解法：
1. 动态规划。
dp[i] 表示字符串 s 的前 i 个字符组成的子串是否在单词表中。
dp[0] = True，即空字符串算在单词表中，设字符串 s 长度为 n，则dp 长度为 n + 1。
结果即 dp[n+1] 的值。

设指针为 i，从左向右扫描字符串 s：
- 如果指针 i 左侧部分是单词表中的单词（即 dp[i] 为 True），
  且右侧 s[i:j] (j 属于 [i+1, n]) 组成的单词在单词表中，
  则表示字符串 s 下标 j 的左侧部分是单词表中的单词（即 dp[j] 为 True）。
  
时间复杂度：O(n^2)
空间复杂度：O(n)

"""
from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """动态规划。"""
        # 初始化 dp，长度为 len(s) + 1。
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_wordBreak(self):
        self.assertTrue(
            self.s.wordBreak("leetcode", ["leet", "code"]),
        )
        self.assertTrue(
            self.s.wordBreak("applepenapple", ["apple", "pen"]),
        )
        self.assertFalse(
            self.s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        )


if __name__ == '__main__':
    unittest.main()
