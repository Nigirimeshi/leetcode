"""
合并两个有序链表

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists

将两个升序链表合并为一个新的升序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1 -> 2 -> 4, 1 -> 3 -> 4
输出：1 -> 1 -> 2 -> 3 -> 4 -> 4

官方解法：
1. 迭代法。
当两个链表都不为空时，判断哪个链表的头节点的值更小，将较小值添加到结果里，之后将链表中的节点向后移动一位。

时间复杂度：O(n+m)，n 和 m 分别是两个链表的长度，因为每次迭代循环时，只会放入一个链表元素，因此 while 循环次数不会超过两个链表之和。
空间复杂度：O(1).

"""
import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(-1)
        prev = pre_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 合并后的 l1 和 l2 最多只有还未合并完，直接将链表末尾指向未合并完的链表即可。
        prev.next = l1 if l1 is not None else l2
        return pre_head.next


class TestSolution(unittest.TestCase):
    @staticmethod
    def list_to_list_node(l: List) -> ListNode:
        dummy = ListNode(0)
        n = dummy
        for v in l:
            n.next = ListNode(v)
            n = n.next
        return dummy.next

    def setUp(self) -> None:
        self.node1 = self.list_to_list_node([1, 2, 4])
        self.node2 = self.list_to_list_node([1, 3, 4])
        self.s = Solution()

    def test_merge_two_lists(self) -> None:
        node = self.s.merge_two_lists(self.node1, self.node2)
        values = list()
        while node is not None:
            values.append(node.val)
            node = node.next
        print(values)


if __name__ == '__main__':
    unittest.main()
