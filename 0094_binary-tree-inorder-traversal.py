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

官方解法：
1. 递归。
递归的调用过程是不断往左边走，当左边走不下去了，就打印节点，并转向右边，然后右边继续这个过程。

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
        """迭代（栈）。"""
        ans: List[int] = []
        stack: List[TreeNode] = []
        node: TreeNode = root
        while node or stack:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中，模拟递归的调用。
            while node:
                stack.append(node)
                node = node.left
        
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程。
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    
        return ans

    def inorder_traversal_3(self, root: TreeNode) -> List[int]:
        """递归。"""
        if not root:
            return []
    
        return self.inorder_traversal_3(root.left) + [root.val] + self.inorder_traversal_3(root.right)


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
