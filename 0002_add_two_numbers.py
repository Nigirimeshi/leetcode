"""
两数相加

链接：https://leetcode-cn.com/problems/add-two-numbers

给出两个非空的链表用来表示两个非负的整数。
其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

我的解题思路：
1. 将两个链表还原成数字，用数字之和构建新链表。

2. 按位相加，记录 “进位” 标志。
需要注意两个链表最后一位和大于 10 时，额外进位一次。

"""
import unittest

from structure.linked_list import ListNode, list_to_list_node, list_node_to_list


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """按位相加，标记进位"""
        head = ListNode(0)
        node = head

        # 标识下一节点是否需要进位。
        plus = False
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            if plus:
                val += 1
            if val >= 10:
                plus = True
                val %= 10
            else:
                plus = False

            node.next = ListNode(val)
            node = node.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        # 末尾进位。
        if plus:
            node.next = ListNode(1)

        return head.next


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_add_two_numbers(self) -> None:
        self.assertListEqual(
            list_node_to_list(
                self.s.add_two_numbers(
                    list_to_list_node([2, 4, 3]),
                    list_to_list_node([5, 6, 4]),
                )
            ),
            [7, 0, 8],
        )
        self.assertListEqual(
            list_node_to_list(
                self.s.add_two_numbers(
                    list_to_list_node([2, 4, 3]),
                    list_to_list_node([0]),
                )
            ),
            [2, 4, 3],
        )
        self.assertListEqual(
            list_node_to_list(
                self.s.add_two_numbers(
                    list_to_list_node([5]),
                    list_to_list_node([5]),
                )
            ),
            [0, 1],
        )


if __name__ == '__main__':
    unittest.main()
