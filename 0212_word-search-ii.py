"""
单词搜索 II

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。

同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。
什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题：实现 Trie（前缀树）。

官方解法：
1. 前缀树 + DFS。
算法：
1) 根据 words 中的单词构建一个前缀树 trie，稍后用于匹配。
2) 从 board 每一个单元格 (i, j) 开始，如果 trie 中存在单元格中字母开头的单词，就进入递归搜索：
   - 检测该单词是否结束。
   - 探索该字母周围的相邻单元格，并在找到的位置上递归探索。

"""
from typing import Dict, List, Set, Tuple
import unittest


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        """前缀树 + DFS。"""
        trie = {}  # 构造字典树
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True
        
        def search(i, j: int, cur_node: Dict[str, str], pre: str, visited: Set[Tuple]) -> None:
            """
            :param i: board 横坐标
            :param j: board 纵坐标
            :param cur_node: 当前 trie 树结点
            :param pre: 随着递归拼接的目标字符串
            :param visited: 已经访问过的坐标
            :return: 无返回值
            """
            if '#' in cur_node:  # 已有字典树结束。
                res.add(pre)  # 添加答案。
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w:
                    char = board[_i][_j]
                    if char in cur_node and (_i, _j) not in visited:  # 可继续搜索
                        search(_i, _j, cur_node[char], pre + char, visited | {(_i, _j)})  # dfs搜索
        
        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索
        return list(res)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_find_words(self):
        self.assertListEqual(
            self.s.find_words(
                [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                ["oath", "pea", "eat", "rain"],
            ),
            ["eat", "oath"],
        )


if __name__ == '__main__':
    unittest.main()
