"""
二叉树的最大深度

链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3, 9, 20, null, null, 15, 7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

我的解题思路：
1. 递归（自顶向下）。


官方解题方案：
1. 递归（深度优先搜索）
假设左右子树最大深度分别为 l 忽然 r，那么最大深度即为 max(l, r) + 1，而左子树和右子树的最大深度又可以用同样方式进行计算。
因此可以先递归计算出左子树和右子树的最大深度，然后在 O(1) 的时间内计算出当前二叉树的最大深度。访问到空节点时退出。

时间复杂度：O(n)，其中 n 为二叉树节点个数。每个节点在递归中只遍历一次。
空间复杂度：O(height)，其中 height 为二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

2. 广度优先搜索

"""
import unittest
from collections import deque

from structure.tree import TreeNode


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """递归（自底向上）。"""
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
    
    def BFS(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = list()
        queue.append(root)
        ans = 0
        while len(queue) > 0:
            sz = len(queue)
            while sz > 0:
                node = queue[0]
                queue = queue[1:]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                sz -= 1
            ans += 1
        return ans

    def max_depth_2(self, root: TreeNode) -> int:
        """递归（自顶向下）。"""
        max_depth = 0
    
        def dfs(node: TreeNode, depth: int) -> None:
            if not node:
                nonlocal max_depth
                max_depth = max(max_depth, depth)
                return
        
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
    
        dfs(root, 0)
        return max_depth

    def max_depth_3(self, root: TreeNode) -> int:
        """层序遍历。

        每遍历完一层，层数 + 1。
        """
        if not root:
            return 0
    
        ans: int = 0
        queue = deque([root])
        while queue:
            # 获取该层的节点数量。
            size = len(queue)
            # 依序遍历该层节点。
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 遍历完一层，层数 + 1。
            ans += 1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_max_depth(self) -> None:
        self.assertEqual(
            self.s.max_depth(),
            3,
        )


if __name__ == '__main__':
    unittest.main()
