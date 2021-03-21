"""
监控二叉树

链接：https://leetcode-cn.com/problems/binary-tree-cameras

给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

示例 1：
输入：[0,0,null,0,0]
    0
    x
0       0

输出：1
解释：如图所示，一台摄像头足以监控所有节点。

示例 2：
输入：[0,0,null,0,null,0,null,null,0]
            0
        x
    0
x
    0

输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：
给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。

解法：
1. 动态规划 + DFS。（提交通过）

状态：
 - 有 2 个：有没有摄像头，是否被监控。
 - dp[node] = (False, False) 表示节点有没有摄像头，是否被监控。

状态转移：
 - node 是叶子节点：dp[node] = (False, False)。
 - node 非叶子节点：
    - 根据左右子节点是否被监控，来决定当前节点装不装摄像头：
       - dp[node][0] = !(dp[node.left][1] and dp[node.right][1])
         解释：
          - 若左右子节点都被监控覆盖了，则当前节点不用装摄像头。
          - 若左右子节点中存在没被监控覆盖的，则当前节点要装摄像头。

    - 检查下当前节点有没有被自己或子节点的摄像头的监控到：
       - dp[node][0] = False 时，即当前节点没装摄像头，需要检查子节点有没有摄像头：
          - dp[node.left][0] 或 dp[node.right][0] = True 时，dp[node][1] = True。
       - dp[node][0] = True 时，即当前节点装了摄像头，那肯定监控覆盖了，直接 dp[node] = True。
      
base case：
 - 叶子节点：dp[node] = (False, False)
 - 空节点：返回 (False, True)，假装没有摄像头，但是被监控覆盖了。
"""
import unittest

from structure.tree import TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def min_camera_cover(self, root: TreeNode) -> int:
        """动态规划 + DFS。"""
        camera, cover = self.__dfs(root)
        # 根节点没被监控覆盖到，需要装个摄像头。
        if not cover:
            self.ans += 1
        return self.ans

    def __dfs(self, root: TreeNode):
        # 叶子节点没有子节点，但可以假装存在虚拟子节点且已被监控覆盖。
        if not root:
            return [False, True]

        left = self.__dfs(root.left)
        right = self.__dfs(root.right)

        # 当前节点要不要装摄像头，有没有被监控覆盖。
        camera, cover = False, False

        # 若左右子节点都被监控覆盖了，则当前节点不用装摄像头。
        # 若左右子节点中存在没被监控覆盖的，则当前节点要装摄像头。
        camera = not all((left[1], right[1]))

        # 该节点没装摄像头。
        if not camera:
            # 左右子节点装了摄像头，则当前节点会被监控覆盖。
            if left[0] or right[0]:
                cover = True

        # 该节点装了摄像头。
        else:
            cover = True
            # 记录摄像头数量。
            self.ans += 1
        return camera, cover


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_min_camera_cover(self):
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.left.left = TreeNode(0)
        root.left.left.left = TreeNode(0)
        root.left.left.left.right = TreeNode(0)

        self.assertEqual(2, self.s.min_camera_cover(root))


if __name__ == "__main__":
    unittest.main()
