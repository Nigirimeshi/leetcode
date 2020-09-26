from typing import List


# 单链表的定义.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_list_node(arr: List) -> ListNode:
    dummy = ListNode(0)
    n = dummy
    for v in arr:
        n.next = ListNode(v)
        n = n.next
    return dummy.next


def list_node_to_list(node: ListNode) -> List:
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans
