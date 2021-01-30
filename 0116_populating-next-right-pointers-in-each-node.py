"""
填充每个节点的下一个右侧节点指针

链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node

给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。

二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

示例：
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

提示：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

我的解题思路：
1. BFS。（通过：√）
使用一次遍历的广度优先遍历，用分隔符 None 分割树的每一层。
每层从左向右遍历，用 pre_node 指向每层遍历过程中的左边一个节点，遍历到右边下一个节点时，用 pre_node 指向当前节点；
换到下一层时，将 pre_node 指向 null。

时间复杂度：O(N)。N 为树中所有节点个数。

空间复杂度：O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2 个节点，外加树的层数（None 的个数）。
 - 广度优先遍历的复杂度取决于一个层级上的最大元素数量。这种情况下空间复杂度为 O(N)。

官方解法：
1. BFS。（嵌套循环遍历）

时间复杂度：O(N)。N 为树中所有节点个数。
空间复杂度：O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2 个节点。
 - 广度优先遍历的复杂度取决于一个层级上的最大元素数量。这种情况下空间复杂度为 O(N)。

2. 使用已建立的 next 指针。

时间复杂度：O(N)
空间复杂度：O(1)

"""
import unittest
from collections import deque

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """BFS（一次遍历）。"""
        if not root:
            return root

        # FIFO 节点队列，用 None 分割树的每一层。
        queue = deque([root, None])
        # 每层当前元素的左边节点。
        pre_node = None

        while len(queue) > 0:
            node = queue.popleft()
            # 向队列尾部添加下一层的节点。
            if node:
                if not pre_node:
                    # 开始遍历新的一层时，将 pre_node 指向每层第一个节点
                    pre_node = node
                else:
                    # 从每层第二个节点开始，将前一个节点的 next 指向自己，并用 pre_node 指向自己。
                    pre_node.next = node
                    pre_node = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 遍历树的下一层。
            else:
                # 该层所有节点遍历过了，且下一层的节点已经加入队列了，用 None 分割下一层。
                if len(queue) != 0:
                    queue.append(None)
    
                pre_node.next = None
                pre_node = None

        return root

    def connect2(self, root: Node) -> Node:
        """层序遍历（迭代）。"""
        if not root:
            return root
    
        queue = deque([root])
        while queue:
            # 缓存该层上一个节点。
            # 刚进入该层时忽略。
            prev_node: Optional[Node] = None
        
            # 该层节点数量。
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
            
                # 用该层上一个节点指向当前节点。
                if prev_node:
                    prev_node.next = node
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
                # 记录当前节点，下次循环时再赋值 next。
                prev_node = node
        return root


class OfficialSolution:
    def connect(self, root: Node) -> Node:
        """BFS（嵌套循环，外循环遍历层，内循环遍历该层所有节点）。"""
        if not root:
            return root

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # 将左节点的 next 指向右节点。
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect2(self, root: Node) -> Node:
        """使用已建立的 next 指针。"""
        if not root:
            return root
    
        leftmost = root
        while leftmost.left:
            # 遍历该层节点组成的链表，为下一层的节点更新 next 指针。
            head = leftmost
            while head:
                # 1. 连接相同父节点的左右子树。
                head.left.next = head.right
            
                # 2. 连接不同父节点的右子树和左子树。
                # 若上一层的 next 指针已连接，可以通过 head.next 访问同层右侧的父节点。
                if head.next:
                    head.right.next = head.next.left
            
                # 继续向右移动指针。
                head = head.next
        
            # 去下一层的最左节点。
            leftmost = leftmost.left
        return root


if __name__ == '__main__':
    unittest.main()
