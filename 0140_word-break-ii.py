"""
单词拆分 II

链接：https://leetcode-cn.com/problems/word-break-ii

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
 "cats and dog",
 "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
 "pine apple pen apple",
 "pineapple pen apple",
 "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

官方解法：
1. 动态规划。

"""
from collections import deque
from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """动态规划。"""
        n = len(s)
        dp = [False] * n
        dp[0] = s[0] in wordDict
        
        for right in range(1, n):
            # 如果整个单词在 wordDict 中，直接返回；
            # 否则将单词分割，挨个判断。
            if s[:right + 1] in wordDict:
                dp[right] = True
                continue
            
            for left in range(right):
                if dp[left] and s[left + 1: right + 1] in wordDict:
                    dp[right] = True
                    break  # 一旦得到 dp[r] = True，就不再循环。
        
        ans = []
        if dp[-1]:
            queue = deque()
            self.__dfs(s, n - 1, wordDict, ans, queue, dp)
        return ans
    
    def __dfs(self, s: str, end: int, words: List[str], ans: List[str], path, dp):
        if s[:end + 1] in words:
            path.appendleft(s[:end + 1])
            ans.append(' '.join(path))
            path.popleft()
        
        for i in range(end):
            if dp[i]:
                suffix = s[i + 1:end + 1]
                if suffix in words:
                    path.appendleft(suffix)
                    self.__dfs(s, i, words, ans, path, dp)
                    path.popleft()


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_wordBreak(self):
        self.assertEqual(
            self.s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
            [
                "cat sand dog",
                "cats and dog",
            ],
        )
        self.assertEqual(
            self.s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
            [
                "pine applepen apple",
                "pineapple pen apple",
                "pine apple pen apple",
            ],
        )


if __name__ == '__main__':
    unittest.main()
