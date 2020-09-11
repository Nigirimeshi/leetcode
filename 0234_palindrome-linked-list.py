"""
回文链表

https://leetcode-cn.com/problems/palindrome-linked-list/

请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

我的解题方案：
1. 将链表转成数组，再用双指针判断回文。
时间复杂度：O(n)
空间复杂度：O(n)

官方解题方案：
1. 将链表的后半部分反转，然后比较前半部分和后半部分，比较完后将链表恢复原样。
可分为以下步骤：
1) 找到链表前半部分的尾节点；
2) 反转后半部分的链表；
3) 迭代前半、后半部分链表，判断是否为回文;
4) 恢复链表；
5) 返回结果。

步骤一：我们可以计算链表节点的数量，然后遍历链表找到前半部分的尾节点。
或者可以使用快慢指针在一次遍历中找到：慢指针一次走一步，快指针一次走两步，快慢指针同时出发。
当快指针移动到链表的末尾时，慢指针到链表的中间。通过慢指针将链表分为两部分。
（若链表有奇数个节点，则中间的节点应该看作是前半部分。）
步骤二：可以使用在反向链表问题中找到解决方法来反转链表的后半部分。
步骤三：比较两个部分的值，当后半部分到达末尾则比较完成，可以忽略计数情况中的中间节点。
步骤四：与步骤二使用的函数相同，再反转一次恢复链表本身。

时间复杂度：O(n)，其中 n 指的是链表的大小。
空间复杂度：O(1)，我们是一个接着一个的改变指针，我们在堆栈上的堆栈帧不超过 O(1)。
该方法的缺点是，在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执执行过程中链表暂时断开。

"""
import unittest

from struct.linked_list import ListNode, list_to_list_node


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        """链表转数组，再用双指针判断回文。"""
        arr = list()
        while head is not None:
            arr.append(head.val)
            head = head.next

        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left, right = left + 1, right - 1
        return True


class OfficialSolution:
    def is_palindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点。
        first_half_end = self.end_of_first_half(head)

        # 反转后半部分的链表。
        second_half_start = self.reverse_list(first_half_end)

        # 比较前后两部分的链表。
        result = True
        first = head
        second = second_half_start
        while result and second is not None:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next

        # 恢复链表。
        first_half_end.next = self.reverse_list(second_half_start)
        return result

        # 返回。

    def end_of_first_half(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while slow.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_palindrome(self) -> None:
        case = list_to_list_node([1, 2])
        self.assertFalse(self.s.is_palindrome(case))

        case = list_to_list_node([1, 2, 2, 1])
        self.assertTrue(self.s.is_palindrome(case))


if __name__ == '__main__':
    unittest.main()
