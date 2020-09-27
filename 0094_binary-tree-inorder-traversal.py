"""
二叉树的中序遍历

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal

给定一个二叉树，返回它的中序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""
import unittest
from typing import List

from structure.tree import TreeNode


class Solution:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        """递归。"""
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root: TreeNode, output: List[int]):
        if not root:
            return None

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

    def inorder_traversal_2(self, root: TreeNode) -> List[int]:
        """用栈迭代。"""
        ans = []
        stack = []
        while root or stack:
            # 先依次将 “中”，“左” 节点入栈。
            while root:
                stack.append(root)
                root = root.left

            # 取出栈顶节点。
            root = stack.pop()
            ans.append(root.val)

            # 检查右节点。
            root = root.right

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_inorder_traversal(self) -> None:
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(
            self.s.inorder_traversal_2(root),
            [1, 3, 2],
        )


if __name__ == '__main__':
    unittest.main()
