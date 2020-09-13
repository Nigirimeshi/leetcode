"""
二叉树的层序遍历

链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3, 9, 20, null, null, 15, 7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

我的解法：
1. BFS。
遍历完每一层的所有节点，再进入下一层。

时间复杂度：O(n)
空间复杂度：O(n)
"""
import unittest
from typing import List

from struct.tree import TreeNode


class OfficialSolution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = []
        queue = [root]
        while queue:
            # 获取该层节点数。
            n = len(queue)
            level = []
            # 遍历完该层的节点（循环 n 次），再进入下一层。
            for i in range(n):
                node = queue[0]
                queue = queue[1:]
                # 记录该层的所有节点值。
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes.append(level)
        return nodes


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_level_order(self) -> None:
        # 二叉树：[3, 9, 20, null, null, 15, 7],
        #
        #     3
        #    / \
        #   9  20
        #     /  \
        #    15   7
        case = TreeNode(3)
        case.left = TreeNode(9)
        case.right = TreeNode(20)
        case.right.left = TreeNode(15)
        case.right.right = TreeNode(7)
        self.assertListEqual(
            self.s.level_order(case),
            [[3], [9, 20], [15, 7]],
        )


if __name__ == '__main__':
    unittest.main()
