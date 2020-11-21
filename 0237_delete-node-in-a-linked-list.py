"""
删除链表中的节点

链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为要被删除的节点。

现有一个链表 --head = [4,5,1,9]，它可以表示为: 4 -> 5 -> 1 -> 9

示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

提示：
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

官方解法：
1. 将想要删除的节点的指换成它之后节点的值，并删除它之后的节点。

时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    unittest.main()
