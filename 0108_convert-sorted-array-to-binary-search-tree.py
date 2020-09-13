"""
将有序数组转换为二叉搜索树

链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

我的解题思路：
1. 高度平衡的二叉搜索树需满足以下条件：
1) 二叉树每个节点的左右两个子树的高度差的绝对值不超过 1；
2) 二叉搜索树需满足：
2.1) 若任意节点的左子树不为空，则左子树上所有节点的值均小于它根节点的值；
2.2) 若任意节点的右子树不为空，则右子树上所有节点的值均大于它根节点的值；
2.3) 任意节点的左、右子树均为二叉搜索树。

官方解法：
1. 递归。
实现二叉树的平衡，其实很简单，只要每次把一组数最中间的位置，作为树的头拎起来，剩下部分平均分两份就行，要是出多来一个数就分配给左脚 or 右脚。
具体实现这个平衡条件，我们可以定义一个函数 “做一棵树”，而且这个函数只和数组的长度有关，和具体数字等等通通无关：

def 做一棵树（数组的哪个段落要做成树）：#这个段落用索引表示即可，与具体数字无关
    #假设这个段落叫A吧
    树的根部 = 这个段落A最中间的数字
    树的左边 = 做一棵树（这个段落A的左边部分）
    树的右边 = 做一棵树（这个段落A的右边部分）
    return 这棵树

时间复杂度：O(n)，其中 n 是数组的长度。每个数字只访问一次。
空间复杂度：O(logn)，其中 n 是数组的长度。空间复杂度不考虑返回值，因此空间复杂度主要取决于递归栈的深度，递归栈的深度是 O(logn)。


"""
import unittest
from typing import List

from struct.tree import TreeNode


class OfficialSolution:
    def sorted_array_to_BST(self, nums: List[int]) -> TreeNode:
        """递归。"""
        return self.build_BST(nums, 0, len(nums) - 1)

    def build_BST(self, nums: List, left: int, right: int) -> TreeNode:
        # 判断区间是否合理，
        if left > right:
            return None

        mid = (left + right) // 2
        tree = TreeNode(nums[mid])
        tree.left = self.build_BST(nums, left, mid - 1)
        tree.right = self.build_BST(nums, mid + 1, right)
        return tree


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_sorted_array_to_BST(self) -> None:
        # [-10, -3, 0, 5, 9]
        pass


if __name__ == '__main__':
    unittest.main()
