"""
验证二叉搜索树

链接：https://leetcode-cn.com/problems/validate-binary-search-tree

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
 - 节点的左子树只包含小于当前节点的数。
 - 节点的右子树只包含大于当前节点的数。
 - 所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5, 1, 4, null, null, 3, 6]。根节点的值为 5 ，但是其右子节点值为 4 。

官方解法：
1. 递归。
设计一个递归函数 helper(root, lower, upper) 来递归判断，函数表示考虑以 root 为根的子树，
判断子树中所有节点的值是否都在 (l,r) 的范围内（注意是开区间）。
如果 root 节点的值 val 不在 (l,r) 的范围内说明不满足条件直接返回，
否则我们要继续递归调用检查它的左右子树是否满足，如果都满足才说明这是一棵二叉搜索树。

那么根据二叉搜索树的性质，在递归调用左子树时，我们需要把上界 upper 改为 root.val，
即调用 helper(root.left, lower, root.val)，因为左子树里所有节点的值均小于它的根节点的值。
同理递归调用右子树时，我们需要把下界 lower 改为 root.val，即调用 helper(root.right, root.val, upper)。

函数递归调用的入口为 helper(root, -inf, +inf)， inf 表示一个无穷大的值。

时间复杂度 : O(n)，其中 n 为二叉树的节点个数。在递归调用的时候二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)。
空间复杂度 : O(n)，其中 n 为二叉树的节点个数。递归函数在递归过程中需要为每一层递归函数分配栈空间，
所以需要额外的空间且该空间取决于递归的深度，即二叉树的高度。
最坏情况下二叉树为一条链，树的高度为 n ，递归最深达到 n 层，故最坏情况下空间复杂度为 O(n) 。

2. 中序遍历
二叉搜索树中序遍历后得到序列一定是升序的，因此可以在中序遍历时检查当前节点的值是否大于前一节点即可。

时间复杂度 : O(n)，其中 n 为二叉树的节点个数。二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)。
空间复杂度 : O(n)，其中 n 为二叉树的节点个数。栈最多存储 n 个节点，因此需要额外的 O(n) 的空间。

"""
import unittest

from struct.tree import TreeNode


class OfficialSolution:
    def is_valid_BST(self, root: TreeNode) -> bool:
        """递归"""

        def helper(node: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
            if node is None:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False

            return True

        return helper(root)

    def is_valid_BST(self, root: TreeNode) -> bool:
        """中序遍历"""
        # stack 存放节点，inorder 存放上一次循环节点值
        stack, inorder = [], float('-inf')

        while len(stack) > 0 or root is not None:
            while root is not None:
                # 先循环移动到最左子节点，记录移动过程中的节点
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 若当前节点小于上一节点，说明当前树非搜索二叉树
            if root.val <= inorder:
                return False
            # 记录当前节点值，用于移动到下一节点时比较
            inorder = root.val
            # 移动到右子树
            root = root.right

        return True


if __name__ == '__main__':
    unittest.main()
