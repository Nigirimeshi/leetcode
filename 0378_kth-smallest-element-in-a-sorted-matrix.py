"""
有序矩阵中第 k 小的元素

链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix

标签：堆

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2。

我的解题思路：
1. 排序（暴力）（居然通过了）。
遍历矩阵所有元素，转为一维数组，再排序，第 k 小的元素即有序数组中下标 k - 1 的元素。

时间复杂度：O(n^2 * logn)
空间复杂度：O(n^2)

官方解法：
1. 归并排序（小根堆）。
每次弹出矩阵中最小的值，第 k 个被弹出的就是结果。
由题意可知，矩阵左上角元素最小，我们可以维护一组 “最小值候选人”，只要保证最小值必然从这组候选人中产生，每次从中弹出最小的一个即可。
我们选择矩阵第一列为第一组候选人，因为每一个数组都是对应行的最小值，全局最小值也必然在其中。
每次弹出候选人中的最小值，然后将弹出候选人的右边一个补进候选人中，就能保证全局最小值一定在候选人列表中产生。
至于 “最小值候选人” 可以用小根堆来存储，每次弹出堆顶元素（最小值）。

解题步骤：
1）用矩阵第一列初始化一个小根堆。
2）弹出最小值候选人。
3）将弹出候选人右边的元素作为新候选人加入小根堆。
4）重复 k - 1 次。
5）返回小根堆堆顶元素。

时间复杂度：O(k*logn)  归并 k 次，每次堆插入和弹出的时间复杂度为 logn。
空间复杂度：O(n) 堆的大小始终为 n。

2. 二分查找。

时间复杂度：O(n*log(r-l))  二分查找进行次数为O(log(r−l))，每次操作时间复杂度为 O(n)
空间复杂度：O(1)


"""
import heapq
from typing import List
import unittest


class Solution:
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """排序。"""
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                array.append(matrix[i][j])
        array.sort()
        return array[k - 1]


class OfficialSolution:
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """归并排序（小根堆）。"""
        # n x n 的矩阵，长宽相等。
        n = len(matrix)
        
        # 用矩阵第一列元素初始化小根堆，并记录坐标，作为第一组最小值候选人。
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)
        
        # 一共需要弹 k 次，这里只弹 k - 1 次，因为需要返回第 k 个最小值。
        for i in range(k - 1):
            # 弹出最小值及其坐标。
            num, x, y = heapq.heappop(min_heap)
            # 对应行的列元素还没有全部弹出。
            if y != n - 1:
                # 将弹出最小值的右边一个元素加入最小值候选人。
                heapq.heappush(min_heap, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(min_heap)[0]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_kth_smallest(self) -> None:
        self.assertEqual(
            self.s.kth_smallest(
                [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15]
                ],
                8,
            ),
            13,
        )


if __name__ == '__main__':
    unittest.main()
