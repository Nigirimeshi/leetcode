"""
打家劫舍 III

链接：https://leetcode-cn.com/problems/house-robber-iii

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。

这个地区只有一个入口，我们称之为 “根”。

除了“根”之外，每栋房子有且只有一个“父“房子与之相连。

一番侦察之后，聪明的小偷意识到 “这个地方的所有房屋的排列类似于一棵二叉树”。

如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1
     
输出: 7
解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

解法：
1. 动态规划。
状态：
 - 偷当前节点，则不能偷左右子节点。
 - 不偷当前节点，则可以偷，也可以不偷左右子节点，取决于左右子节点各自偷与不偷所能得到的最高金额。
状态转移：
 - 偷当前节点：dp[node][1] = 当前节点的钱 + 不偷左子节点的最高金额 + 不偷右子节点的最高金额
                         = node.val + dp[node.left][0] + dp[node.right][0]
 - 不偷当前节点：dp[node][0] = max(偷左节点的最高金额, 不偷左节点的最高金额) + max(偷右节点的最高金额, 不偷右节点的最高金额)
                           = max(dp[node.left][1], dp[node.left][0])
                           + max(dp[node.right][1], dp[node.right][0])
                           
时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest
from typing import List

from structure.tree import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        """动态规划。"""
        dp = self.dfs(root)
        return max(dp[0], dp[1])

    def dfs(self, node: TreeNode) -> List[int]:
        if not node:
            return [0, 0]

        left_dp = self.dfs(node.left)
        right_dp = self.dfs(node.right)

        dp: List[int] = [0, 0]
        dp[0] = max(left_dp[0], left_dp[1]) + max(right_dp[0], right_dp[1])
        dp[1] = node.val + left_dp[0] + right_dp[0]
        return dp


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == "__main__":
    unittest.main()
