"""
分割回文串

链接：https://leetcode-cn.com/problems/palindrome-partitioning

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

官方解法：
1. 回溯。
回溯法思考步骤：
1) 画递归树；
2) 根据画的树编码。



"""
from typing import List
import unittest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """回溯。"""
        ans = []
        length = len(s)
        if length == 0:
            return ans
        
        stack = []
        self.backtracking(s, 0, length, stack, ans)
        return ans
    
    def backtracking(self, s: str, start, length: int, path: List[str], ans: List[List[str]]) -> None:
        # 当叶子节点是空字符串时结算，此时 path 记录了从根节点到叶子节点的路径，即一种分割方式。
        if start == length:
            # 注意，这里拷贝 path，不然回溯完是空数组。
            ans.append(path.copy())
            return
        
        for i in range(start, length):
            # 子串非回文，剪枝。
            if not self.is_palindrome(s, start, i):
                continue
            
            # 子串是回文，记录路径。
            path.append(s[start:i + 1])
            # 深度优先遍历。
            self.backtracking(s, i + 1, length, path, ans)
            # 回溯。
            path.pop()
    
    def is_palindrome(self, s: str, left, right: int) -> bool:
        """判断是否为回文串。"""
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_partition(self):
        ans = self.s.partition("aab")
        self.assertIn(["aa", "b"], ans)
        self.assertIn(["a", "a", "b"], ans)


if __name__ == '__main__':
    unittest.main()
