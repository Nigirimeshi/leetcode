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
1. 双指针。
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
        """
        双指针。
        设指针 pre 指向 None，指针 cur 指向 head，
        然后遍历 cur，每次将 cur.next 指向 pre，
        然后将 pre 和 cur 沿着链表移动一位。
        直到 cur 遍历完链表，此时 pre 指向链表最后一个元素。
        """
        pre, cur = None, head
        # 用 cur 遍历链表。
        while cur:
            # 记录当前节点的下一个节点。
            tmp = cur.next
            # 将当前节点的下一个节点指向 pre。
            cur.next = pre
            # pre 和 cur 都前进一位。
            pre = cur
            cur = tmp
        # cur 遍历完链表，pre 刚好指向链表尾部，此时链表已完成反转。
        return pre
    
    def reverse_list_2(self, head: ListNode) -> ListNode:
        """
        递归。
        """
        if not head or not head.next:
            return head
        
        # cur 在递归回溯过程中一直链表尾节点，即反转后的头节点。
        cur = self.reverse_list_2(head.next)
        # 将 A -> B 变成 A <- B
        head.next.next = head
        # 断开 A -> B，放置死循环。
        head.next = None
        return cur


if __name__ == '__main__':
    unittest.main()
