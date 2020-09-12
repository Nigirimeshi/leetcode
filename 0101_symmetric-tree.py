"""
对称二叉树

链接：https://leetcode-cn.com/problems/symmetric-tree

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1, 2, 2, 3, 4, 4, 3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1, 2, 2, null, 3, null, 3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

我的解题思路：
1. 中序遍历二叉树，如示例 1 中的二叉树，结果应为 [3, 2, 4, 1, 4, 2, 3]。
得到的数组应为回文数组，之后判断数组是否回文数组即可。

"""
import unittest
from typing import List

from struct.tree import TreeNode


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        """中序遍历。"""
        stack, values = [], []
        while len(stack) > 0 or root is not None:
            while root is not None:
                # 移动到最左子节点，并记录移动过程中的节点。
                stack.append(root)
                print(f'stack: {stack}')
                root = root.left
            root = stack.pop()
            values.append(root.val)
            print(f'values: {values}')
            if (root.left is not None and root.right is None) or (root.right is not None and root.left is None):
                values.append(None)
            root = root.right
        print(values)

        return self.is_reverse_list(values)

    def is_reverse_list(self, arr: List) -> bool:
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left, right = left + 1, right - 1
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_symmetric(self) -> None:
        # [1, 2, 3, 4, null, 5]
        """
            1
           / \
          2   3
         / \ / \
        4    5
        """
        # [4, 2, None, 1, 5, 3, None]
        case = TreeNode(1)
        case.left = TreeNode(2)
        case.right = TreeNode(3)
        case.left.left = TreeNode(4)
        case.right.left = TreeNode(5)
        self.s.is_symmetric(case)


if __name__ == '__main__':
    unittest.main()
