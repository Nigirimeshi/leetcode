"""
环形链表

链接：https://leetcode-cn.com/problems/linked-list-cycle

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3, 2, 0, -4], pos = 1
图形：3 -> 2 -> 0 -> 4
          ↑  <----  ↓
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1, 2], pos = 0
图形：1 -> 2
     ↑ <- ↓
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
图形：1 -> None
输出：false
解释：链表中没有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？

我的解题方案：
1. 哈希表记录链表节点，存在重复节点时返回。
时间复杂度：O(n)
空间复杂度：O(n)

官方解题方案：
1. 快慢指针

时间复杂度：O(n)，让我们将 n 设为链表中结点的总数。为了分析时间复杂度，我们分别考虑下面两种情况。
 - 链表中不存在环：
   快指针将会首先到达尾部，其时间取决于列表的长度，也就是 O(n)。

 - 链表中存在环：
   我们将慢指针的移动过程划分为两个阶段：非环部分与环形部分：
   1) 慢指针在走完非环部分阶段后将进入环形部分：
      此时，快指针已经进入环中 "迭代次数 = 非环部分长度 = N"
   2) 两个指针都在环形区域中：
      考虑两个在环形赛道上的运动员 - 快跑者每次移动两步而慢跑者每次只移动一步。其速度的差值为 1，
      因此需要经过 "二者之间距离/速度差值" 次循环后，快跑者可以追上慢跑者。
      这个距离几乎就是 "环形部分长度 K" 且速度差值为 1，我们得出这样的结论 "迭代次数=近似于 '环形部分长度 K'".
因此，在最糟糕的情形下，时间复杂度为 O(N+K)，也就是 O(n)。

空间复杂度：O(1)，我们只使用了慢指针和快指针两个结点，所以空间复杂度为 O(1)。

"""
import unittest

from structure.linked_list import ListNode


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        d = dict()
        while head is not None:
            if d.__contains__(head):
                return True
            d[head] = None
            head = head.next
        return False
    
    def has_cycle_2(self, head: ListNode) -> bool:
        """
        快慢指针。
        慢指针每次走 1 步，快指针每次走 2 步。
        当快慢指针指向同一个结点时，说明存在环。
        当快指针指向尾节点时，说明不存在环。
        """
        if not head:
            return False
        
        slow, fast = head, head
        while fast:
            # 慢指针每次移动 1 步。
            slow = slow.next
            # 若快指针 next 为空，说明到了尾结点，即不存在环。
            if not fast.next:
                return False
            # 快指针每次移动 2 步。
            fast = fast.next.next
            # 当快慢指针重合时，说明存在环。
            if fast == slow:
                return True
        # 快指针移动到了尾部，不存在环。
        return False


class OfficialSolution:
    def has_cycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == '__main__':
    unittest.main()
