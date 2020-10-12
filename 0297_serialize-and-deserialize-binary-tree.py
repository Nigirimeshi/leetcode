"""
二叉树的序列化与反序列化

链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree

序列化是将一个数据结构或者对象转换为连续的比特位的操作，
进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员/全局/静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

官方解法：
1. DFS。


"""
import unittest
from collections import deque
from typing import List

from structure.tree import TreeNode


class Codec:
    """BFS。"""

    def serialize(self, root: TreeNode) -> str:
        """将树编码为单个字符串。"""
        if not root:
            return []

        q = deque()
        q.append(root)
        res = ''
        while q:
            node = q.popleft()
            if node:
                res += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
            else:
                res += 'X,'
        return res

    def deserialize(self, data: str) -> TreeNode:
        """将您的编码数据解码为树。"""
        if not data:
            return None

        data = data.split(',')
        root = TreeNode(data.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.left = TreeNode(val)
                    q.append(node.left)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.right = TreeNode(val)
                    q.append(node.right)
        return root


class Codec2:
    """DFS。"""

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return 'X,'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right

    def deserialize(self, data: str) -> TreeNode:
        data = data.split(',')
        root = self.build_tree(data)
        return root

    def build_tree(self, data: List[str]):
        val = data.pop(0)
        if val == 'X':
            return None

        node = TreeNode(val)
        node.left = self.build_tree(data)
        node.right = self.build_tree(data)
        return node


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Codec()

    def test_serialize(self) -> None:
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left.left = TreeNode(4)
        print(self.c.serialize(tree))

    def test_deserialize(self) -> None:
        s = '1,2,4,None,None,None,3,None,None,'
        print(self.c.deserialize(s))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    unittest.main()
