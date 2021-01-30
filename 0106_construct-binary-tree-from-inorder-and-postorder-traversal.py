"""
从中序与后序遍历序列构造二叉树

链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]

返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

官方解法：
1. 递归。
已知：
 - 中序遍历顺序：左节点，根节点，右节点。
 - 后续遍历顺序：左节点，右节点，根节点。
易知：
 - 后序遍历列表中尾元素是整个树的根节点。
 - 利用根节点可以在中序遍历列表中找到根节点的下标，进而将中序遍历数组分为左、右两部分，对应左、右子树。
 - 针对左、右两部分使用上述方法递归下去构造子树。
算法：
 1. 为了高效查找后续遍历数组中根节点元素在中序遍历数组中的下标，首先创建哈希表来存储中序序列，即（元素、下标）键值对的哈希表。
 2. 定义递归函数 helper(start, end)，表示当前递归到中序序列中当前子树的左右边界，递归入口为 helper(0, n - 1)。
    - 若 start > end，说明当前节点是叶子节点，子树为空，返回 None。
    - 选择后续序列中最后一个元素作为根节点。
    - 利用哈希表查找当前根节点在中序序列中的下标为 index，
      那么中序序列中 [start, index - 1] 属于左子树，[index + 1, end] 属于右子树。
    - 根据后续遍历逻辑，递归创建右子树 helper(index + 1, end) 和左子树 helper(start, index - 1)。
      注意这里要先创建右子树，因为后续遍历创建数组的顺序是：左、右、根，所以反过来构造树要按顺序：根、右、左。

时间复杂度：O(N)
空间复杂度：O(N)
 
"""
import unittest
from typing import List, Optional

from structure.tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """递归。"""
        # 根据 inorder 构造索引，键是 val，值是对应下标。
        idx = {v: i for i, v in enumerate(inorder)}
        
        def helper(start, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            
            # 根据 postorder 创建父节点。
            val = postorder.pop()
            root = TreeNode(val)
            
            # 获取 inorder 中 root 对应的下标，进而分割、递归构造左右子树。
            index = idx[val]
            root.right = helper(index + 1, end)
            root.left = helper(start, index - 1)
            return root
        
        return helper(0, len(inorder) - 1)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
