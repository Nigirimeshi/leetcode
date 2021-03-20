package leetcode

import (
	"testing"
)

/*
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
*/

type TrieNode struct {
	End      bool
	Children map[rune]*TrieNode
}

type Trie struct {
	root *TrieNode
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{
		root: &TrieNode{
			End:      false,
			Children: map[rune]*TrieNode{},
		},
	}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	node := this.root
	for _, r := range word {
		if _, ok := node.Children[r]; !ok {
			node.Children[r] = &TrieNode{
				End:      false,
				Children: map[rune]*TrieNode{},
			}
		}
		node = node.Children[r]
	}
	node.End = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	node := this.root
	for _, r := range word {
		if _, ok := node.Children[r]; !ok {
			return false
		}
		node = node.Children[r]
	}
	return node.End
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	node := this.root
	for _, r := range prefix {
		if _, ok := node.Children[r]; !ok {
			return false
		}
		node = node.Children[r]
	}
	return true
}

func TestTrie(t *testing.T) {
	trie := Constructor()
	trie.Insert("apple")
	if !trie.Search("apple") {
		t.Errorf("should return: true, but get: false")
	}
	if trie.Search("app") {
		t.Errorf("should return: false, but get: true")
	}
	if !trie.StartsWith("app") {
		t.Errorf("should return: true, but get: false")
	}
	trie.Insert("app")
	if !trie.Search("app") {
		t.Errorf("should return: true, but get: false")
	}
}
