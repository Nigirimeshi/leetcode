"""
二叉树的锯齿形层次遍历

链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal

给定一个二叉树，返回其节点值的锯齿形层次遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

我的解题思路：
1.
设置交替标志位，用于每一层控制是左 -> 右，还是右 -> 左。
逐层遍历。

官方解法：
1. BFS + 双端队列。
使用一层循环逐层遍历树，将要访问的节点添加到队列中，使用分隔符（例如：空节点）分割树的每一层。
用双端队列实现锯齿形顺序。
在每一层，使用一个空的双端队列保存该层所有节点，根据每一层的访问顺序（即从左到右或从右到左），决定从双端队列的哪一端插入节点。
 - 从左向右遍历（FIFO）：将元素添加到双端队列队尾，确保后添加的节点后被访问。
 - 从右向左遍历（FILO）：将元素添加到双端队列头部，确保后添加的节点先被访问。

时间复杂度：O(N)。N 是树中节点的数量。
 - 每个节点仅访问一次。
 - 双端队列的插入为常数时间。如果用数组，头部插入需要 O(K) 的时间，其中 K 是数组的长度。

空间复杂度：O(N)。N 是树中节点的数量。

2. DFS。
在 DFS 遍历期间，将结果保存在按层数索引的全局数组中，即 array[level] 存储同一层的所有节点，然后在 DFS 的每一步更新该数组。
使用双端队列保存同一层的所有节点，并交替插入方向。

定义一个递归方法 DFS(node, level)，node 表示当前节点，level 表示当前层数，该方法执行 3 个步骤：
1) 如果是第一次访问该层的节点，即该层的双端队列不存在。那么创建一个双端队列，并添加当前节点到队列中。
2) 如果当前节点的双端队列已存在，那么根据层数，将当前节点插入头部或尾部即可。
3) 递归左右节点。

时间复杂度：O(N)。N 为树中节点的数量，所有节点只访问一次。
空间复杂度：O(H)。H 是树的高度。例如：包含 N 个节点的树，高度大约为 log2^N。
 - 与 BFS 不同，DFS 不需要维护双端队列。
 - 方法递归调用会产生额外的内层消耗。方法 DFS(node, level) 的调用栈大小刚好等于节点所在层数，因此复杂度为 O(log2^N)。比 BFS 好。

"""
import unittest
from typing import List
from collections import deque

from structure.tree import TreeNode


class OfficialSolution:
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        """BFS + 双端队列。"""
        if not root:
            return []

        ans = []
        # 是否从左向右排序。
        is_order_left = True
        # 每一层的队列。
        level_queue = deque()
        # 将树的节点按分隔符（None）分割后的队列。
        node_queue = deque([root, None])
        while len(node_queue) > 0:
            curr_node = node_queue.popleft()
            if curr_node:
                # 实现锯齿形顺序。
                if is_order_left:
                    level_queue.append(curr_node.val)
                else:
                    level_queue.appendleft(curr_node.val)

                # 将下一层节点加入队列。
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            # 分割并准备向树的下一层遍历。
            else:
                ans.append(list(level_queue))
                # 如果节点队列空了，说明已经遍历完了，不用再分割了，即退出循环的条件。
                if len(node_queue) != 0:
                    node_queue.append(None)

                level_queue = deque()
                is_order_left = not is_order_left

        return ans

    def zigzag_level_order_2(self, root: TreeNode) -> List[List[int]]:
        """DFS + 全局数组 + 双端队列。"""
        if root is None:
            return []

        ans = []

        def dfs(node: TreeNode, level: int) -> None:
            # 若是第一次访问该层的节点，则创建双端队列，并添加元素。
            if level >= len(ans):
                ans.append(deque([node.val]))
            else:
                # 根据层数，决定插入双端队列头或尾。
                # 若层数为偶数，插入头；若层数为奇数，插入尾。
                if level % 2 == 0:
                    ans[level].append(node.val)
                else:
                    ans[level].appendleft(node.val)

            # 递归节点。
            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level + 1)

        dfs(root, 0)

        for i in range(len(ans)):
            ans[i] = list(ans[i])

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_zigzag_level_order(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
