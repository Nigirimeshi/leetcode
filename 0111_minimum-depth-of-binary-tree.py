"""
二叉树的最小深度

链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：
树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000

解法：
1. BFS。
初始层数为 0，遍历树的每一层，当某个节点非根节点，且同时没有左、右子树时，返回层数 + 1。
每遍历完一层，层数加 1。

时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest
from collections import deque

from structure.tree import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """BFS。"""
        if not root:
            return 0

        ans: int = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                    # 当节点是叶子节点时，立即返回。
                    if node != root and not node.left and not node.right:
                        return ans + 1
            ans += 1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == "__main__":
    unittest.main()
