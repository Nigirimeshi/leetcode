"""
二叉树的后序遍历

链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal

给定一个二叉树，返回它的 后序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

解法：
1. 递归。

2. 迭代（栈）。

"""
import unittest
from typing import List, Optional

from structure.tree import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归。"""
        if not root:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代（栈）。
        
        修改前序遍历的代码，修改左右子树入栈的顺序，并将结果集取反即可。
        """
        if not root:
            return []
        
        ans: List[int] = []
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]
    
    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        """迭代（栈）。"""
        if not root:
            return []
        
        ans: List[int] = []
        stack: List[TreeNode] = []
        node: Optional[TreeNode] = root
        while node or stack:
            while node:
                # 根节点先入栈。
                stack.append(node)
                # 若左子树存在，就移动到左子树；否则，移动到右子树。
                node = node.left if node.left else node.right
            # 退出内循环说明走到了叶子节点，没有左右子树了，该叶子节点即为栈顶元素。
            node = stack.pop()
            ans.append(node.val)
            # 若栈非空，且当前节点是栈顶元素的左子树，则转向遍历右子树。
            if stack and stack[-1].left == node:
                node = stack[-1].right
            # 没有左右子树，强制退栈。
            else:
                node = None
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
