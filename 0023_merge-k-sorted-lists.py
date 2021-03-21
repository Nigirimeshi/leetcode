"""
合并 K 个升序链表

链接：https://leetcode-cn.com/problems/merge-k-sorted-lists

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

解法：
1. 顺序合并。

时间复杂度：O(k^2n)
空间复杂度：O(1)

2. 分治合并。

时间复杂度：O(kn * logk)
空间复杂度：O(logn)

"""
import unittest
from typing import List, Optional

from structure.linked_list import ListNode, list_to_list_node


class Solution:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """顺序合并。"""
        ans: Optional[ListNode] = None
        for node in lists:
            ans = self.__merge(ans, node)
        return ans

    def __merge(self, left: ListNode, right: ListNode) -> Optional[ListNode]:
        if not any((left, right)):
            return left if not right else right

        root: ListNode = ListNode()
        head: ListNode = root

        # 交替归并排序，从小到大。
        while left and right:
            if left.val <= right.val:
                root.next = left
                left = left.next
            else:
                root.next = right
                right = right.next

            root = root.next

        # 若剩余 left，说明剩下的都比 right 大。
        while left:
            root.next = left
            root = root.next
            left = left.next

        # 若剩余 right，说明剩下的都比 left 大。
        while right:
            root.next = right
            root = root.next
            right = right.next

        return head.next


class Solution2:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """分治合并。"""
        return self.__merge(lists, 0, len(lists) - 1)

    def __merge(
        self, lists: List[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        if left > right:
            return None

        mid = left + (right - left) // 2
        a = self.__merge(lists, left, mid)
        b = self.__merge(lists, mid + 1, right)
        return self.__merge_to_list_node(a, b)

    def __merge_to_list_node(
        self, a: Optional[ListNode], b: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not a or not b:
            return a if a else b

        head = root = ListNode()
        while a and b:
            if a.val <= b.val:
                root.next = a
                a = a.next
            else:
                root.next = b
                b = b.next

            root = root.next

        root.next = a if a else b
        return head.next


class Case:
    def __init__(self, lists: List[Optional[ListNode]], want: Optional[ListNode]):
        self.lists = lists
        self.want = want

    def compare(self, output: ListNode) -> bool:
        if not self.want and not output:
            return True
        if self.want and not output:
            return False
        if not self.want and output:
            return False

        want = self.want
        while output:
            if output.val != want.val:
                return False
            want = want.next
            output = output.next
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution2()

    def test_mergeKLists(self):
        c1 = [None, ListNode(1)]

        c2_1 = ListNode(1)
        c2_1.next = ListNode(4)
        c2_1.next.next = ListNode(5)
        c2_2 = ListNode(1)
        c2_2.next = ListNode(3)
        c2_2.next.next = ListNode(4)
        c2_3 = ListNode(2)
        c2_3.next = ListNode(6)
        c2 = [c2_1, c2_2, c2_3]
        c2_want = list_to_list_node([1, 1, 2, 3, 4, 4, 5, 6])

        c3 = [None, None]

        test_cases: List[Case] = [Case(c1, c1[1]), Case(c2, c2_want), Case(c3, None)]

        for tc in test_cases:
            output = self.s.merge_k_lists(tc.lists)
            self.assertTrue(tc.compare(output))


if __name__ == "__main__":
    unittest.main()
