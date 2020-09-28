"""
从前序与中序遍历序列中构造二叉树

链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出：

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

官方解法：
1. 递归。
先序遍历：根节点 -> 左子树 -> 右子树
中序遍历：左子树 -> 根节点 -> 右子树

不难发现，先序遍历的第一个元素为根节点，在中序遍历中，该节点左侧为左子树，右侧为右子树。

构建二叉树问题的本质：
1) 找到各个子树的根节点；
2) 构建该根节点的左子树；
3) 构建该根节点的右子树。

例如：
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
preorder 的第一个元素 3 为根节点；inorder 中 3 左侧的 [9] 是树的左子树，右侧 [15,20,7] 构成了右子树。
由此可知 preorder 中 3 右边第 1 个元素 [9] 是左子树，[20,15,7] 是右子树。
preorder [3, [9], [20, 15, 7]]
inorder  [[9], 3, [15, 20, 7]]

目前为止，已经知道了根节点为 3，左子树为 [9]，右子树前序遍历为 [20,15,7]，右子树中序遍历为 [15,20,7]。
依次类推，preorder 中 20 为右子树的根节点，inorder 里 20 左边的 [15] 为左子树，[20,7] 为右子树；
最终推导出完整的树。


"""
import unittest
from typing import List

from structure.tree import TreeNode


class OfficialSolution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归。"""
        # 构造中序遍历元素对应的位置索引。
        idx = {element: i for i, element in enumerate(inorder)}

        def build(preorder_left, preorder_right, inorder_left, inorder_right: int) -> TreeNode:
            """递归构造树。"""
            if preorder_left > preorder_right:
                return None

            # 先序遍历的第一个元素即为根节点。
            root = TreeNode(preorder[preorder_left])
            # 找到中序遍历序列中根节点的索引位置。
            inorder_root = idx[root.val]
            # 获取左子树元素个数，即中序遍历中根节点左侧元素个数。
            size_left_subtree = inorder_root - inorder_left
            # 递归构建左子树。
            root.left = build(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归构建右子树。
            root.right = build(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    unittest.main()
