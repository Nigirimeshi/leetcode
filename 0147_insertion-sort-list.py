"""
对链表进行插入排序

链接：https://leetcode-cn.com/problems/insertion-sort-list

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4

示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""
import unittest

from structure.linked_list import ListNode


class Solution:
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        # 有序链表。
        sorted_list = ListNode(0)
        sorted_list.next = head
        
        last = head
        curr = head.next
        # 从第二个节点开始，到尾节点结束。
        while curr:
            # 当前遍历到的节点值大于等于上次遍历到的节点值，不用调整位置。
            if curr.val >= last.val:
                last = last.next
            # 当前遍历到的节点值小于上次遍历到的节点值，需要调整位置。
            else:
                # 取出当前节点。
                last.next = curr.next
                # 从有序链表中找到当前节点应插入的位置。
                prev = sorted_list
                while prev.next.val <= curr.val:
                    prev = prev.next
                # 将当前节点插入 prev 后面。
                curr.next = prev.next
                prev.next = curr
            
            curr = last.next
        return sorted_list.next


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_insertion_sort_list(self) -> None:
        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(3)
        h = self.s.insertion_sort_list(head)
        ans = []
        while h:
            ans.append(h.val)
            h = h.next
        self.assertListEqual(
            [1, 2, 3, 4],
            ans,
        )


if __name__ == '__main__':
    unittest.main()
