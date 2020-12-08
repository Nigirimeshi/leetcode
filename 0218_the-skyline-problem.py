"""
天际线问题

链接：https://leetcode-cn.com/problems/the-skyline-problem

标签：

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
 - lefti 是第 i 座建筑物左边缘的 x 坐标。
 - righti 是第 i 座建筑物右边缘的 x 坐标。
 - heighti 是第 i 座建筑物的高度。

天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。

关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。

此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。

例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；

三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

示例 1：
输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。

示例 2：
输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]

提示：
1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings 按 lefti 非递减排序。


官方解法：
1. 扫描线法。
使用扫描线，从左至右扫过。如果遇到左端点，将高度入堆，如果遇到右端点，则将高度从堆中删除。使用 last 变量记录上一个转折点。

解法：
1）只考虑每个建筑的的左上角和右上角的坐标，将所有点按 x 轴排序，然后开始遍历。
2）用一个大根堆存储遍历坐标的高度，即 y 轴坐标。
3）遇到左、右坐标时，有不同的处理机制：
3.1）遇到左坐标，将其 y 轴坐标加到堆中。
3.2）遇到右坐标，将其 y 轴坐标从堆中删除，也就是删除了对应的左上角坐标的 y 值。
4）最后判断大根堆中堆顶元素有没有更新，若更新了，就把当前的 x 和更新后的堆顶（最高高度 y）作为一个坐标加入到最终结果中。


"""
import heapq
from typing import List
import unittest


class Solution:
    def get_Skyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """扫描线法。"""
        if not buildings:
            return []
        
        # 存储每个建筑的左上角和右上角坐标。
        points = []
        for left, right, height in buildings:
            # 由于 heapq 只有小根堆，所以左端点高度用负数存储。
            points.append((left, -height, right))
            points.append((right, height, 0))
        
        # 按 x 轴排序。
        points.sort()
        
        # 用大根堆存储遍历过的坐标的高度，即 y 轴坐标。
        # 初始大根堆，0 是初始高度，float('inf') 对应无穷右边界。
        heap = [[0, float('inf')]]
        # 存储答案。
        ans = [[0, 0]]
        
        for x, h, r in points:
            # 遇到右端点，将其高度从堆中删除。
            # 保证当前堆顶为去除之前建筑物右端点的最大值。
            # 每次在判断关键点的时候，移除所有右端点 ≤ 当前点的堆顶。
            while x >= heap[0][1]:
                heapq.heappop(heap)
            
            # 左端点入堆。
            if h < 0:
                heapq.heappush(heap, [h, r])
            
            # 若堆顶元素发生变化，说明是天际线中的关键点，加入结果集。
            if ans[-1][1] != -heap[0][0]:
                ans.append([x, -heap[0][0]])
        
        return ans[1:]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
