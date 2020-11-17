"""
复制带随机指针的链表

链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。

提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

我的解题思路：
1. 遍历原始链表，拷贝一份。（通过）

时间复杂度：O(n)
空间复杂度：O(n)

官方解法：
1. 回溯。

2. 迭代。

3. 交错链表（O(1) 空间的迭代）。（最优解）
通过扭曲原链表，将每个拷贝结点放在原来结点的旁边。
这种旧结点和新结点交错的方法可以不使用额外的空间解决该题。
1）遍历原始链表并拷贝每一个结点，将拷贝结点放在原始结点的旁边，创造出一个旧结点和新结点交错的链表。
原始链表：A -> B -> C
交错链表：A -> A' -> B -> B' -> C -> C'

原始结点 next 指向的是新创建的结点。
cloned_node.next = original_node.next
origin_node.next = clone_node

2）迭代这个新旧交错的链表，并使用旧结点的 random 指针更新对应新结点的 random 指针。
比如说，B 的 random 指针指向 A，意味着 B' 的 random 指针指向 A'。

3）目前 random 指针已被正确赋值，只剩修改 next 指针，将新旧链表分隔开即可。
交错链表：A -> A' -> B -> B' -> C -> C' -> None
A.next = A'.next
A'.next = B.next

B.next = B'.next
B'.next = C.next

C.next = C'.next = None

空间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 空链表，直接返回。
        if not head:
            return None
        
        # 创建新链表。
        node = Node(head.val)
        # 存储新链表所有结点的地址（下标对应索引，值对应地址）。
        new_address = [node]
        # 保留新链表的头结点，用于结果返回。
        new_head = node
        
        # 存储 head 链表各结点地址。
        old_address = [head]
        # 复制一份 head，用于遍历，从第二个结点开始。
        head_cp = head.next
        
        # 深拷贝 head 链表，不含 random。
        while head_cp:
            # 构造新链表。
            node.next = Node(head_cp.val)
            node = node.next
            new_address.append(node)
            
            # 记录 head 链表各结点地址。
            old_address.append(head_cp)
            # 移动 head 链表。
            head_cp = head_cp.next
        
        head_cp = head
        node = new_head
        # 补充新链表各结点的 random 值。
        while head_cp:
            # 根据 head 链表 random 地址指向 old_address 的相对索引位置，填充新链表的 random 地址。
            if head_cp.random in old_address:
                node.random = new_address[old_address.index(head_cp.random)]
            else:
                node.random = None
            # 移动链表。
            node = node.next
            head_cp = head_cp.next
        
        return new_head


class OfficialSolution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """回溯。"""
        pass
    
    def copyRandomList_2(self, head: 'Node') -> 'Node':
        """迭代。"""
    
    def copyRandomList_3(self, head: 'Node') -> 'Node':
        """交错链表。（最优解）"""
        if not head:
            return head
        
        # 遍历原始链表并拷贝每一个结点，将拷贝结点放在原始结点的旁边，创造出一个旧、新结点交错的链表。
        # 假设 A -> B -> C 是原始结点。
        # 遍历完会变成 A -> A' -> B -> B' -> C -> C'。
        ptr = head
        while ptr:
            # 克隆原始结点。
            new_node = Node(ptr.val)
            
            # 将新结点放在老结点右边。
            # 假设老结点 A -> B。
            # 修改后会变成 A -> A' -> B。
            new_node.next = ptr.next
            ptr.next = new_node
            
            # 移动到下一个旧结点。
            ptr = new_node.next
        
        # 遍历这个新旧交错的链表，并使用旧结点的 random 指针更新对应新结点的 random 指针。
        # 比如：B 结点的 random 指针指向 A，那么意味着 B' 的 random 指针指向 A'。
        ptr = head
        while ptr:
            # 如果旧结点的 random 指针指向非空，则新结点必然指向旧结点 random 指针指向结点的下一个结点。
            ptr.next.random = ptr.random.next if ptr.random else None
            # 移动到下一个旧结点。
            ptr = ptr.next.next
        
        # 修改交错链表的 next 指针，将新、旧链表分隔开。
        ptr_new = head.next  # A' -> B' -> C'
        ptr_old = head  # A -> B -> C
        # 记录新链表的头结点，用于返回结果。
        new_head = head.next
        while ptr_old:
            ptr_old.next = ptr_new.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
        
        return new_head


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
