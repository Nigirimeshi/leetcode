"""
奇偶链表

链接：https://leetcode-cn.com/problems/odd-even-linked-list

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

我的解题思路：
1. 遍历链表，每次找出下一个相对位置的奇数节点，
然后将该奇数节点放到当前节点的 next 位置。


官方解法：
1. 将奇节点放在一个链表里，偶节点放在另一个链表里，然后把偶链表接在奇链表尾部。

时间复杂度： O(n)。总共有 n 个节点，我们每个遍历一次。
空间复杂度： O(1)。我们只需要 4 个指针。

"""
import unittest

from structure.linked_list import (ListNode,
                                   list_node_to_list,
                                   list_to_list_node)


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        cur = head
        offset = 1
        while cur:
            # 记录当前节点的下一节点。
            cur_next = cur.next
            # 获取下一个相对位置为奇数的节点。
            i = 0
            even_node = cur
            while i < offset:
                even_node = even_node.next
                # 遍历到尾结点了，已完成奇偶排列。
                if not even_node:
                    return head
                i += 1
            # 遍历到尾结点了，完成排列。
            if not even_node.next:
                return head
            
            # 记录目标奇数节点。
            odd_node = even_node.next
            # 断开目标奇数节点。
            even_node.next = even_node.next.next
            
            # 连接当前节点与下一个奇数节点。
            cur.next = odd_node
            odd_node.next = cur_next
            
            # 遍历下一个节点。
            cur = odd_node
            
            # 每遍历一次，下一个奇数节点的相对位置偏移值就得加 1。
            offset += 1


class OfficialSolution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        """
        分离奇偶节点再合并。
        若链表为空，直接返回。
        记录 head 为奇数链表头，even_head = head.next 为偶数链表头，用于最后合并奇偶链表。
        分别设指针 odd 指向 head，even 指向 head.next
        遍历原链表，构造奇偶链表，先更新奇数节点，再更新偶数节点。
        - 更新奇数节点时，odd.next = even.next，然后 odd = odd.next
        - 更新偶数节点时，even.next = odd.next，然后 even = even.next
        最后合并链表 odd.next = even_head。

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not head:
            return head
        
        even_head = head.next
        odd, even = head, even_head
        while even and even.next:
            # 更新奇数节点，并移动到下一个奇数节点。
            odd.next = even.next
            odd = odd.next
            # 更新偶数节点，并移动到下一个偶数节点。
            even.next = odd.next
            even = even.next
        
        # 合并奇数偶数链表。
        odd.next = even_head
        return head


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_odd_even_list(self) -> None:
        self.assertListEqual(
            list_node_to_list(
                self.s.odd_even_list(
                    list_to_list_node([1, 2, 3, 4, 5])
                )
            ),
            [1, 3, 5, 2, 4],
        )
        self.assertListEqual(
            list_node_to_list(
                self.s.odd_even_list(
                    list_to_list_node([2, 1, 3, 5, 6, 4, 7])
                )
            ),
            [2, 3, 6, 7, 1, 5, 4],
        )
        self.assertListEqual(
            list_node_to_list(
                self.s.odd_even_list(
                    list_to_list_node([1, 2, 3, 4, 5, 6, 7, 8])
                )
            ),
            [1, 3, 5, 7, 2, 4, 6, 8],
        )


if __name__ == '__main__':
    unittest.main()
