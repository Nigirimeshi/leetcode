"""
数据流的中位数

链接：https://leetcode-cn.com/leetbook/read/top-interview-questions/xalff2/

标签：堆，设计

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。

double findMedian() - 返回目前所有元素的中位数。

示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

进阶:
如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？


官方解法：
1. 堆（大根堆、小根堆）。
1）奇偶性决定了中位数的个数。
1.1）数据流个数为奇数，中位数只有 1 个；
1.2）数据流个数为偶数，中位数有 2 个，可称之为：左中位数，右中位数。

2）中位数的特点。
如果从数据流中每读出一位数后都排一次序，中位数会把数据流分为 2 部分：前有序数组，后有序数组。

3）发现以下特征：
3.1）数据流总数为奇数时，中位数是前有序数组的最大值；
3.2）数据流总数为偶数时，左中位数是前有序数组的最大值，右中位数是后有序数组的最小值。

4）由于我们只关心这两个有序数组的最值，因此可以使用堆来存储。
4.1）前有序数组只关心最大值，因此可以动态的放在一个大根堆中；
4.2）后有序数组只关心最小值，因此可以动态的放在一个小根堆中。

5）数据流总数不同时，对应中位数的计算方法：
5.1）数据流总数为偶数时，让两个堆的元素个数相等，两个堆顶元素的平均值就是所求中位数；
5.2）数据流总数为奇数时，只要保证大根堆的元素个数永远比小根堆的个数多一个，那么大根堆的堆顶元素就是所求的中位数。

6）为了得到中位数，两个堆应满足以下条件：
6.1）大根堆的堆顶元素，小于等于小根堆的堆顶元素；
6.2）大根堆的元素个数要么等于小根堆的元素个数，要么比小根堆元素个数多 1。

7）具体情况分析：
7.1）若两个堆元素个数之和为偶数，为了让大根堆中多 1 个元素，流程如下：
     大根堆 -> 小根堆 -> 大根堆
7.2）若两个堆元素个数之和为奇数，此时小根堆必须多 1 个元素，才能使两个堆元素数量相等，流程如下：
     大根堆 -> 小根堆
综上考虑，不论两个堆之和的奇偶，都得先到大根堆，再到小根堆，而当加入 1 个元素后，元素个数为奇数时，
再把小根堆的堆顶元素给大根堆就可以了。

时间复杂度： O(5*logn) + O(1) ≈ O(logn)
- 最坏情况下，从顶部有三个堆插入和两个堆删除。每一个都需要花费 O(logn) 时间。
- 找到平均值需要持续的 O(1) 时间，因为可以直接访问堆的顶部。

空间复杂度：O(n) 用于在容器中保存输入的线性空间。


"""
import heapq
import unittest


class MedianFinder:
    
    def __init__(self):
        """堆。"""
        self.count = 0
        self.max_heap = []
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        # 元素个数加 1。
        self.count += 1
        
        # 存入大根堆，由于 Python 只有小根堆，想要大根堆，存入相反数即可。
        heapq.heappush(self.max_heap, -num)
        
        # 存入小根堆，得把大根堆的数取反还原。
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        
        # 如果元素总数为奇数，就把小根堆的堆顶元素给大根堆。
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)
    
    def findMedian(self) -> float:
        # 若元素总数为奇数，那么大根堆的栈顶元素即为中位数。
        if self.count & 1:
            return -self.max_heap[0]
        
        # 若元素总数为偶数，那么两个堆的堆顶元素的平均值即为中位数。
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class TestMedianFinder(unittest.TestCase):
    def setUp(self) -> None:
        self.mf = MedianFinder()
    
    def test_findMedian(self) -> None:
        self.mf.addNum(6)
        self.assertEqual(self.mf.findMedian(), 6)
        self.mf.addNum(10)
        self.assertEqual(self.mf.findMedian(), 8)
        self.mf.addNum(2)
        self.assertEqual(self.mf.findMedian(), 6)


if __name__ == '__main__':
    unittest.main()
