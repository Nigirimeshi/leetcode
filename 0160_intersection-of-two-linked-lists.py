"""
相交链表

编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：
A：      a1 -> a2 ↘
                    c1 -> c2 -> c3
B：b1 -> b2 -> b3 ↗

在 c1 开始相交。

示例 1：
A：     4 -> 1 ↘
                 8 -> 4 -> 5
B：5 -> 0 -> 1 ↗

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
        从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
        在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
A：0 -> 9 -> 1 ↘
                 2 -> 4
B：          5 ↗

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
        从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
        在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
A：2 -> 6 -> 4

B：     1 -> 5

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
        由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。


注意：
 - 如果两个链表没有交点，返回 null.
 - 在返回结果后，两个链表仍须保持原有的结构。
 - 可假定整个链表结构中没有循环。
 - 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

我的解题思路：
1. 暴力。
遍历两个链表，找出相同的节点。（提交超时）

时间复杂度：O(m*n)
空间复杂度：O(1)

官方解法：
1. 哈希表。
遍历链表 A，用哈希表记录每个节点地址/引用，然后遍历链表 B，检查每个节点是否在 A 的哈希表中。

时间复杂度：O(m+n)
空间复杂度：O(m) 或 O(n)

2. 双指针。
指针 a 指向链表 A 头节点，指针 b 指向链表 B 头节点，让它们向后逐结点遍历。
当指针 a 移动到了链表 A 的尾部，将它重定向到链表 B 的头节点；
当指针 b 移动到了链表 B 的尾部，将它重定向到链表 A 的头节点；
若某一时刻指针 a 与 b 相遇了，则该节点为相交节点。
若直到最后结点仍不相同，则两链表不相交。

时间复杂度：O(m+n)
空间复杂度：O(1)

"""
import unittest

from structure.linked_list import (ListNode)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """遍历两个链表，找出相同的节点。"""
        if not headA or not headB:
            return None

        a = headA
        while a:
            b = headB
            while b:
                if a == b:
                    return a
                b = b.next
            a = a.next
        return None


class OfficialSolution:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        """哈希表法。"""
        idx = {}
        a = headA
        while a:
            idx[a] = None
            a = a.next

        b = headB
        while b:
            if b in idx:
                return b
            b = b.next
        return None

    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针。
        设指针 a，b 分别指向链表 A，B 的头部，
        然后分别遍历链表，当遍历完当前链表，便将指针指向另一个链表的头部，继续遍历，直至 2 个指针相遇。
        即：
        - 指针 a 遍历完链表 A 时，把指针 a 指向链表 B；
        - 指针 b 遍历完链表 B 时，把指针 b 指向链表 A。
        最终两个指针走过的路径为（C 为相交部分的路径长度）：
        指针 a：A + C + B
        指针 b：B + C + A
        路径明显相等，可知若 2 个链表相交，则指针 a，b 必在相交节点相遇。

        时间复杂度：O(m+n)
        空间复杂度：O(1)
        """
        # 任意一个链表不存在，肯定不相交。
        if not headA or not headB:
            return None
    
        # 分别指向 2 个链表头。
        a, b = headA, headB
        # 遍历 2 个链表，直至两指针相等。
        # 指针相等有 2 种情况：
        # 1. 存在相交节点，a，b 指向相交节点。
        # 2. 不存在相交节点，a，b 遍历到链表尾部，指向 None。
        while a != b:
            # 当前链表遍历完，就指向另一个链表头部，接着遍历。
            a = a.next if a else headB
            b = b.next if b else headA
    
        # a 可能指向相交节点或 None。
        return a


if __name__ == '__main__':
    unittest.main()
