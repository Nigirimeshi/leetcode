"""
LRU 缓存机制

链接：https://leetcode-cn.com/problems/lru-cache

运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。

实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

提示：
1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put


"""
import unittest
from typing import Dict


class ListNode:
    def __init__(self, key: int = None, value: int = None) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 键为 key，值为 ListNode。
        self.map: Dict[int, ListNode] = {}
        self.head = ListNode()
        self.tail = ListNode()
        # 连接头节点和尾结点。
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_node_to_tail(self, key: int) -> None:
        """将目标 key 所在节点移动到双向链表尾节点前。"""
        node = self.map[key]
        
        # 先把目标节点单独拎出来，连接 node 的上一节点与下一节点。
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # 将目标节点移动到尾节点前。
        # 连接 tail 的上一节点与 node。
        self.tail.prev.next = node
        node.prev = self.tail.prev
        # 连接 node 和 tail。
        self.tail.prev = node
        node.next = self.tail
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        # 将 key 对应节点移动到 tail 前。
        self.move_node_to_tail(key)
        node = self.map[key]
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            # 空间不足。
            if self.capacity == len(self.map):
                # 删除 map 里最久未访问的 key，即 head 的 next 节点。
                self.map.pop(self.head.next.key)
                
                # 删除最久未访问的节点，即 head 的 next 节点。
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            
            node = ListNode(key, value)
            # 将 node 放到 tail 节点前。
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            # 记录 key 和节点。
            self.map[key] = node
        else:
            node = self.map[key]
            # 更新 node 值，并移动至 tail 前。
            node.value = value
            self.move_node_to_tail(key)


class TestSolution(unittest.TestCase):
    def test_lru_cache(self) -> None:
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(1, lru.get(1))
        lru.put(3, 3)
        self.assertEqual(-1, lru.get(2))
        lru.put(4, 4)
        self.assertEqual(-1, lru.get(1))
        self.assertEqual(3, lru.get(3))
        self.assertEqual(4, lru.get(4))


if __name__ == '__main__':
    unittest.main()
