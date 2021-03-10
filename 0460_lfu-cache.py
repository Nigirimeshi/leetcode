"""
LFU 缓存

链接：https://leetcode-cn.com/problems/lfu-cache

请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：
LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象

int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。

void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。

当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。

在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。

注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。

使用次数会在对应项被移除后置为 0 。

为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。

对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。


示例：
输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lFUCache.get(1);      // 返回 1
                      // cache=[1,2], cnt(2)=1, cnt(1)=2
lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                      // cache=[3,1], cnt(3)=1, cnt(1)=2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,1], cnt(3)=2, cnt(1)=2
lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                      // cache=[4,3], cnt(4)=1, cnt(3)=2
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,4], cnt(4)=1, cnt(3)=3
lFUCache.get(4);      // 返回 4
                      // cache=[3,4], cnt(4)=2, cnt(3)=3

提示：
0 <= capacity, key, value <= 104
最多调用 105 次 get 和 put 方法。

进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？

解法：
1. 两个哈希表 + N 个双链表。
一个哈希表 node_map 存放：key，node：
 - node 包含：key，value，使用频率 freq。

另一个哈希表 freq_map 存放：使用频率 freq，双链表。
 - 双链表包含：头、尾节点，相同频率的 node。
 
算法：
1）get 操作：
1.1）若 key 不存在，返回 -1。
1.2）若 key 存在，则返回对应节点 value，并将使用频率加 1。
1.2.1）从 freq_map[freq] 的双链表中移除该节点，放到 freq_map[freq + 1] 中双链表的头节点后。
1.2.2）若移除该节点后的双链表只剩头、尾节点，则删除 freq_map[freq] 及其指向的双链表。

2）put 操作：
2.1）若 key 存在，则修改对应 value，并将使用频率加 1；
2.2.1）从 freq_map[freq] 的双链表中移除该节点，放到 freq_map[freq + 1] 中双链表的头节点后。
2.2.2）若移除该节点后的双链表只剩头、尾节点，则删除 freq_map[freq] 及其指向的双链表。
2.2）若 key 不存在：
2.2.1）缓存超过最大容量：
2.2.1.1）则先删除访问频率最低的元素（freq_map[min_freq] 中双链表的尾节点前一个元素）。
2.2.1.2）插入新元素，频率为 1，若频率哈希表中不存在 key 为 1 的链表，需要新建。
2.2.2）缓存不超过最大容量：
2.2.2.1）插入新元素，频率为 1，若频率哈希表中不存在 key 为 1 的链表，需要新建。

3）维护 min_freq:
3.1）插入新元素时，新元素的频率只能是 1，所以将min_freq 置为 1。
3.2）查找/更新元素时，将元素频率 + 1，
     之后若 min_freq 不在 freq_map 中了，说明 freq_map[min_freq] 已被删除，则使 min_freq + 1。

"""
import unittest
from typing import Dict, Optional


class Node:
    def __init__(self, key: int = None, value: int = None, freq: int = 0):
        self.key: int = key
        self.value: int = value
        self.freq: int = freq
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        # 头尾相连。
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self) -> bool:
        """
        判断双链表是否为空链表。
        除了头尾节点，不存在其他节点时为空链表。
        """
        return self.head.next == self.tail

    def last_node(self) -> Optional[Node]:
        """
        获取尾节点的前一个节点。
        只有头尾节点时，返回 None。
        """
        if self.is_empty():
            return None

        return self.tail.prev

    def insert_head(self, node: Node):
        """将节点插到头节点后。"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete(self, node: Node):
        """删除指定节点。"""
        if self.is_empty():
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map: Dict[int, Node] = {}
        self.freq_map: Dict[int, LinkedList] = {}
        self.min_freq: int = 0

    def get(self, key: int) -> int:
        # 不存在。
        if key not in self.node_map:
            return -1

        # 存在。
        node = self.node_map[key]
        # 移动节点所在的链表，增加使用频率。
        self.increment(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 已存在的 key，更新 value。
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            # 移动节点所在的链表，增加使用频率。
            self.increment(node)
            return

        # 不存在的 key。
        # 容量为 0，直接返回。
        if self.capacity == 0:
            return
        # 容量已满，需要先删除使用频率最低且最久未使用的元素。
        if len(self.node_map) == self.capacity:
            self.delete_min_freq_node()

        # 新建节点。
        node = Node(key=key, value=value, freq=0)
        # 移动节点所在的链表，增加使用频率。
        self.increment(node)
        self.node_map[key] = node

    def increment(self, node: Node) -> None:
        # 新节点。
        if node.freq == 0:
            # 节点频率置 1。
            node.freq = 1
            # 插入到频率为 1 链表的头节点后，若频率为 1 的链表不存在，则新建。
            self.set_default_linked_list(node)
            # 插入新值的使用频率是 1，最小使用频率即为 1。
            self.min_freq = 1
            return

        # 已存在的节点。
        # 从原频率链表中删除。
        self.delete_node(node)
        # 使用频率 + 1。
        node.freq += 1
        # 将节点放入新频率链表头部，若对应频率的链表不存在则新建。
        self.set_default_linked_list(node)
        # 若此时最小频率的链表已被删除，则使最小频率 + 1。
        if self.min_freq not in self.freq_map:
            self.min_freq += 1

    def set_default_linked_list(self, node):
        """根据节点的频率，将其插入到对应的链表的头部，若链表不存在，则新建。"""
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = LinkedList()

        linked_list = self.freq_map[node.freq]
        linked_list.insert_head(node)

    def delete_node(self, node: Node) -> None:
        # 从原频率链表中删除。
        linked_list = self.freq_map[node.freq]
        linked_list.delete(node)
        # 若删除后，链表为空，则删除链表。
        if linked_list.is_empty():
            del self.freq_map[node.freq]

    def delete_min_freq_node(self) -> None:
        """删除使用频率最低且最久未使用的节点。"""
        # 找出使用频率最低的链表的尾节点，并删除。
        linked_list = self.freq_map[self.min_freq]
        node = linked_list.last_node()
        linked_list.delete(node)
        del self.node_map[node.key]
        # 若删除后，链表为空，则删除链表。
        if linked_list.is_empty():
            del self.freq_map[node.freq]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.lfu = LFUCache()


if __name__ == "__main__":
    unittest.main()
