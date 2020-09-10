"""
反转链表

链接：https://leetcode-cn.com/problems/reverse-linked-list

反转一个单链表。

示例:
输入: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
输出: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

我的解法：
1. 迭代

官方解法：
1. 迭代。
遍历链表时，将当前节点的 next 指向前一个节点。
由于节点没有引用上一个节点，所以必须事先存储上一节点。
在更改引用前，还需要另一个指针存储下一节点。
不要忘记最后返回新的头引用。

时间复杂度：O(n)，假设 n 是链表的长度。
空间复杂度：O(1)。

"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """迭代"""
        if head is None:
            return head

        # 缓存链表元素
        vals = list()
        while head != None:
            vals.append(head.val)
            head = head.next

        rev = ListNode(vals[-1])
        dummy = ListNode(0)
        dummy.next = rev
        for val in vals[-2::-1]:
            tmp = ListNode(val)
            rev.next = tmp
            rev = rev.next

        return dummy.next


class OfficialSolution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        return prev

    def reverse_list_2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverse_list_2(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    unittest.main()
