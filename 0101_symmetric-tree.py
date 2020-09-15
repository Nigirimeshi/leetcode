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

官方解法：
1. 递归。
比较 left 和 right，再比较 left.left 和 right.right，以及 left.right 和 right.left，依此递归。
递归终止条件：
1) 当 left 和 right 都为 None 时，返回 True；
2) 当 left 或 right 为 None 时，返回 False；
3) 当 left 不等于 right 时，返回 False。

时间复杂度是 O(n)，因为要遍历 n 个节点
空间复杂度是 O(n)，空间复杂度是递归的深度，也就是跟树高度有关，最坏情况下树变成一个链表结构，高度是 n。

2. 迭代。
维护一个队列，每次从队列中拿两个节点（left 和 right）比较，
再将 left.left 和 right.right 以及 left.right 和 right.left 放入队列。
两节点都为空时进入下一次循环，仅一个为空时，返回 False。

时间复杂度：O(n)。
空间复杂度：O(n)。

"""
import unittest

from structure.tree import TreeNode


class OfficialSolution:
    def is_symmetric(self, root: TreeNode) -> bool:
        """递归。"""
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right) -> bool:
        # 左右节点都为空。
        if not (left or right):
            return True

        # 两个节点有一个为空。
        if not (left and right):
            return False

        # 两个节点不等。
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)

    def is_symmetric_2(self, root: TreeNode) -> bool:
        """迭代。"""
        if not root or not (root.left or root.right):
            return True

        queue = [root.left, root.right]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            # 两节点都为空，继续循环。
            if not (left or right):
                continue
            # 两节点有一个为空，即不对称，返回 False。
            if not (left and right):
                return False
            # 两节点值不等，返回 False。
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

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
