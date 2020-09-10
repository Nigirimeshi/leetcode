"""
删除链表的倒数第 N 个节点

链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1 -> 2 -> 3 -> 4 -> 5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

我的解题思路：
1. 先获取链表长度 L，删除第 L - n + 1 个元素。
2. 假如 n = 2，遍历链表，当节点 next 的 next 是 None 时，说明当前节点是倒数第 2 个。
以此类推，当节点的 n * next 时 None 时，当前节点刚好是倒数第 n 个。

我的解题方案：
1. 两次遍历
第一次遍历获取链表长度 L；第二次遍历再删除第 L - n + 1 个元素。

时间复杂度：O(L)，该算法对列表进行了两次遍历，首先计算了列表的长度 L 其次找到第 L−n 个结点。 操作执行了 2L-n 步，时间复杂度为 O(L)。
空间复杂度：O(1)，我们只用了常量级的额外空间。

官方解题方案：
1. 一次遍历（双指针）
第一个指针从链表开头移动 n + 1 步，第二个指针从链表的开头出发，此时两个相差 n 个节点。
通过同时移动指针保持这个 n 个间隔，直到第一个指针到达最后一个节点，此时第二个指针刚好指向倒数第 n 个节点；
之后将第二个指针的 next 指向 next.next 即可。

"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """两次遍历"""
        # 用于最后返回原始头节点
        first = ListNode(0)
        first.next = head

        # 获取链表总长度
        length = 1
        node = head
        while node != None:
            length += 1
            node = node.next

        # 遍历到目标节点位置
        node = first
        for i in range(length - n - 1):
            node = node.next

        # 删除第 length -n + 1  个元素
        node.next = node.next.next
        return first.next


class OfficialSolution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """一次遍历"""
        dummy = ListNode(0)
        dummy.next = head

        first, second = dummy, dummy
        for i in range(n + 1):
            first = first.next

        while first != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    unittest.main()
