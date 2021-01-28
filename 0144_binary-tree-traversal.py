"""
二叉树的中序遍历

链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal

给你二叉树的根节点 root ，返回它节点值的前序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？

我的解法：
1. 递归。
时间复杂度：O(N) N 是节点数量。
空间复杂度：O(H) H 是树的深度。


"""
import unittest
from typing import List

from structure.tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """递归前序遍历。"""
        if not root:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代前序遍历。"""
        if not root:
            return []
        
        ans: List[int] = []
        stack: List[TreeNode] = []
        node: TreeNode = root
        while node or stack:
            # 根节点和左子树入栈。
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            # 弹出一个节点，到达右子树。
            node = stack.pop()
            node = node.right
        return ans
    
    def preorderTraversal3(self, root: TreeNode) -> List[int]:
        """迭代（栈）。"""
        if not root:
            return []
        
        ans: List[int] = []
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()
            if node:
                # 根节点先加入结果集。
                ans.append(node.val)
                # 因为栈的特性（先进后出），先把右子树入栈。
                if node.right:
                    stack.append(node.right)
                # 左子树入栈。
                if node.left:
                    stack.append(node.left)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
