"""
二叉树的最近公共祖先

链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：

“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

官方解法：
1. 递归（深度优先遍历）。
节点 p、q 分为 2 种情况：
- p、q 在相同子树中；
- p、q 在不同子树中。

从根节点递归左右子树。
递归终止条件：当前节点节点为空，或等于 p、q 节点，则返回当前节点。
递归左右子树：
- 若返回的左右子树节点均不为空，则说明 p、q 分别在左右子树中，即当前节点为最近公共节点。
- 若左右子树中有一个为空，则返回非空的节点。

"""
import unittest

from structure.tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """递归。"""
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 左右子树都有返回值，说明 p、q 在相同子树中，它们的根节点相同，即为最近公共节点。
        if left and right:
            return root
        # 当前节点的左右子树中只找到 p、q 中的一个，说明 p、q 在不同的子树，
        # 深度优先遍历，先遍历到的节点深度低，即为最近公共节点。
        return left if left else right


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
