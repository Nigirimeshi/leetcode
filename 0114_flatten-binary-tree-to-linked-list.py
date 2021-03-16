"""
二叉树展开为链表

链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list

给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [0]
输出：[0]

提示：
树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100

解法：
1. 前序遍历。
二叉树展开为单链表后，单链表中节点的顺序与前序遍历相同。
因此先前序遍历，再更新每个节点的左右子节点即可。

时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest
from typing import List, Union

from structure.tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 存放前序遍历后的各节点。
        preorder_list: List[TreeNode] = []
        # 前序遍历。
        self.preorder(root, preorder_list)

        n = len(preorder_list)
        for i in range(1, n):
            prev, curr = preorder_list[i - 1], preorder_list[i]
            prev.left = None
            prev.right = curr

    def preorder(self, root: TreeNode, preorder_list: List[TreeNode]) -> None:
        if not root:
            return
        preorder_list.append(root)
        self.preorder(root.left, preorder_list)
        self.preorder(root.right, preorder_list)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == "__main__":
    unittest.main()
