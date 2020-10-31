"""
实现 Trie（前缀树）

标签：字符串，树

链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。


"""
from collections import defaultdict
import unittest


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end = True
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()
    
    def test_tire(self):
        self.trie.insert('apple')
        self.assertTrue(self.trie.search('apple'))
        self.assertFalse(self.trie.search('app'))
        self.assertTrue(self.trie.startsWith('app'))
        self.trie.insert('app')
        self.assertTrue(self.trie.search('app'))


if __name__ == '__main__':
    unittest.main()
