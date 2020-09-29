"""
二叉搜索树中第 K 小的元素

链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1

   3
  / \
 1   4
  \
   2

输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3

       5
      / \
     3   6
    / \
   2   4
  /
 1

输出: 3

进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

我的解题思路：
1. DFS，递归，中序遍历。
中序遍历树，用数组依次记录各节点值，此时数组是从小到大排序的。

时间复杂度：O(N)
空间复杂度：O(N)

官方解法：
1. 递归。
通过构造 BST 的中序遍历序列，则第 k-1 个元素就是第 k 小的元素。

时间复杂度：O(N)，遍历了整个树。
空间复杂度：O(N)，用了一个数组存储中序序列。

2. 迭代。
在栈的帮助下，可以将方法一的递归转换为迭代，这样可以加快速度，因为这样可以不用遍历整个树，可以在找到答案后停止。

时间复杂度：O(H+k)。其中 H 指的是树的高度，由于我们开始遍历之前，要先向下达到叶，
 - 当树是一个平衡树时：复杂度为 O(logN+k)。
 - 当树是一个不平衡树时：复杂度为O(N+k)，此时所有的节点都在左子树。

空间复杂度：O(H+k)。
 - 当树是一个平衡树时：O(logN+k)。
 - 当树是一个非平衡树时：O(N+k)。

"""
import unittest
from typing import List

from structure.tree import TreeNode


class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """DFS。"""
        tmp = []

        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            tmp.append(node.val)
            dfs(node.right)

        dfs(root)
        return tmp[k - 1]


class OfficialSolution:
    def ktn_smallest(self, root: TreeNode, k: int) -> int:
        """递归（中序遍历）。"""

        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

    def ktn_smallest_2(self, root: TreeNode, k: int) -> int:
        """迭代。"""
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_kth_smallest(self) -> None:
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        val = self.s.kth_smallest(root, 3)
        print(val)


if __name__ == '__main__':
    unittest.main()
