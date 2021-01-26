"""
二叉树中的最大路径和。

链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum

路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径 至少包含一个 节点，且不一定经过根节点。

路径和是路径中各节点值的总和。

给你一个二叉树的根节点 root，返回其 最大路径和。

示例 1：
    1
  ↙   ↘
2       3

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
    -10
  ↙     ↘
9         20
        ↙    ↘
      15       7
      
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
 树中节点数目范围是 [1, 3 * 104]
 -1000 <= Node.val <= 1000

官方解法：
1. 递归。
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/shou-hui-tu-jie-hen-you-ya-de-yi-dao-dfsti-by-hyj8/
思路：
 - 每个节点有 3 种选择：1. 停在当前节点；2. 走左节点；3. 走右节点。
 - 走到子节点，又面临 3 种选择，需要递归处理。
 - 不能走回头路，即走进一个子节点又返回父节点走进另一个子节点，路径重叠。
 
定义递归函数：
 - 只关心路径走进一个子树，能够获取的最大收益，不管具体怎么走。
 - 定义 dfs 函数，返回当前子树能向父节点提供的最大路径和，即一条从父节点延伸下来的路径，能在当前子树中获得的最大收益。分 3 种情况：
    - 1. 路径停在当前子树的根节点，最大收益：root.val
    - 2. 走进左子树，最大收益：root.val + dfs(root.left)
    - 3. 走进右子树，最大收益：root.val + dfs(root.right)
 - 遍历到 null 节点时，返回 0。
 - 若子树 dfs 结果为负数，则应忽略它，返回 0。
 
最大路径可能产生于局部子树中：
 - 定义一个最大路径和，用于记录整个树中的最大路径和。
 - 每递归一个子树，都要求出当前子树内部的最大路径和，并和最大路径和比较。
 - 一个子树内部的最大路径和 = root.val + dfs(root.left) + def(root.right)

时间复杂度：O(N) N 为二叉树节点数量。
空间复杂度：O(H) H 为树的深度。

"""
import unittest

from structure.tree import TreeNode


class Solution:
    def max_path_sum(self, root: TreeNode) -> int:
        """递归。"""
        # 记录整个树的最大路径和。
        max_sum = float('-inf')
        
        def dfs(subtree_root: TreeNode) -> int:
            # 遍历到 null 节点，返回 0。
            if not subtree_root:
                return 0
            
            # 分别获取左右子树的最大路径和。
            left = dfs(subtree_root.left)
            right = dfs(subtree_root.right)
            
            # 计算当前子树内部的最大路径和。
            inner_max_sum = subtree_root.val + left + right
            # 和整个树的最大路径和比较。
            nonlocal max_sum
            max_sum = max(max_sum, inner_max_sum)
            
            # 返回对父节点提供的左、右子树各自的最大路径和。
            output_max_sum = subtree_root.val + max(left, right)
            # 若对父节点提供的最大路径和小于 0，则不选择该路径，返回 0。
            if output_max_sum < 0:
                return 0
            return output_max_sum
        
        dfs(root)
        return max_sum


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
