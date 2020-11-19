"""
排序链表

链接：https://leetcode-cn.com/problems/sort-list

给你链表的头结点 head，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
4 -> 2 -> 1 -> 3
       ↓
1 -> 2 -> 3 -> 4

输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
-1 -> 5 -> 3 -> 4 -> 0
           ↓
-1 -> 0 -> 3 -> 4 -> 5

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105


我的解题思路：
1. 排序数组。（提交通过）
先将链表转成数组，然后排序数组，再将数组转成链表。

时间复杂度：O(nlogn)
空间复杂度：O(n)

官方解法：
1. 归并排序（递归）。
题目要求时间复杂度为 O(nlogn)，自然想到二分法，从而联想到归并排序。
对数组做归并排序空间复杂度为 O(n)，由新开辟数组 O(n) 和递归函数调用 O(logn) 组成，而根据链表特性：
 - 数组额外空间：链表可通过修改引用改变节点顺序，无需额外空间。
 - 递归额外空间：无法避免，若想达到 O(1) 空间复杂度，则不能使用递归。

通过递归实现链表归并排序，有以下 2 个环节：
1）题目输入的 head == None 时，无需处理，直接返回 None。

2）分割 cut 环节：找到当前链表中点，并从中点将链表断开。
 - 使用快慢双指针法，找到中点，奇数个节点找到中心节点，偶数个节点找到中心左边的节点。
 - 找到中点 slow 后，执行 slow.next = None 将链表断开。
 - 递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp（因为链表是从 slow 切断的）。
 - cut 递归终止条件：当 head.next == None 时，说明只有一个节点了，直接返回该节点。

3）合并 merge 环节：将两个排序链表合并称为一个排序链表。
 - 双指针法合并，建立辅助 ListNode h 作为链表头部。
 - 设置两指针 left 和 right，分别指向两个链表的头部，比较两指针处节点值大小，由小到大加入辅助链表 h，指针交替前进，直至添加完两个链表。
 - 返回辅助链表 h 的下一个节点 h.next 即为合并后的排序链表。
 - 时间复杂度 O(l + r)，l 和 r 分别为 2 个链表长度。
 
 时间复杂度：O(nlogn)
 空间复杂度：O(logn)
 
2. 归并排序（循环）。（满足题目进阶要求）


"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        排序数组 + 数组链表转换。
        """
        # 将链表转成数组，再排序。
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        
        # 将排序后的数组转成链表。
        node = ListNode(0)
        new_head = node
        for val in arr:
            new_node = ListNode(val)
            node.next = new_node
            node = node.next
        return new_head.next


class OfficialSolution:
    def sortList(self, head: ListNode) -> ListNode:
        """归并排序（递归）。"""
        # 当输入 head 为空时，无需排序，直接返回。
        # 当输入 head.next 为空时，说明链表只有一个节点，作为递归切割的终止条件。
        if not head or not head.next:
            return head
        
        # 通过快慢指针找到链表中点，当快指针移动到尾部，慢指针即指向中点。
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # 从中点切割链表。
        mid, slow.next = slow.next, None
        # 递归切割链表，获取排序后的 2 个链表。
        left, right = self.sortList(head), self.sortList(mid)
        
        # 建立辅助链表头，用于返回结果。
        h = res = ListNode(0)
        # 合并 2 个有序链表。
        while left and right:
            # 由小到大，交替移动指针合并。
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        # 当 2 个链表长度和为奇数时，某个链表会先移动到尾部，从而剩余一个节点。
        h.next = left if left else right
        
        # 返回辅助链表的 next 节点即为答案。
        return res.next


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
