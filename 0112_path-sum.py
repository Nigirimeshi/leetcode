"""
路径总和

链接：https://leetcode-cn.com/problems/path-sum

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum，

判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：false

示例 3：
输入：root = [1,2], targetSum = 0
输出：false

提示：
树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

官方解法：
1. 递归（自顶向下）。
思路：
 - 假设从根节点到当前节点的值和为 val，可以将大问题转为小问题：是否存在从当前节点的子节点到叶子节点的路径和为 sum - val。

时间复杂度：O(N) N 是节点数。
空间复杂度：O(H) H 是树的高度，最坏情况，树呈链状，O(N)；平均情况下，树的高度与节点数的对数正相关，即 O(logN)。

2. 迭代（队列，广度优先遍历）。
思路：
 - 存储从根节点到当前节点的路径和；
 - 使用 2 个队列分别存储节点，路径和。
 
时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest
from collections import deque

from structure.tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """递归（自顶向下）。"""
        if not root:
            return False
        
        # 当前节点为叶子节点时，比较目标和。
        if not root.left and not root.right:
            return targetSum == root.val
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
    def hasPathSum2(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        node_queue = deque([root])
        value_queue = deque([root.val])
        while node_queue:
            node = node_queue.popleft()
            value = value_queue.popleft()
            # 若当前节点是叶子节点，比较路径和。
            if not node.left and not node.right:
                if value == targetSum:
                    return True
                continue
            
            if node.left:
                node_queue.append(node.left)
                value_queue.append(node.left.val + value)
            if node.right:
                node_queue.append(node.right)
                value_queue.append(node.right.val + value)
        
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
