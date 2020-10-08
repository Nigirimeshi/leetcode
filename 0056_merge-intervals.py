"""
合并区间

链接：https://leetcode-cn.com/problems/merge-intervals

给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
intervals[i][0] <= intervals[i][1]


我的解题思路：
1.
发现的规律：
 - 满足 intervals[i][-1] >= intervals[i+1][0] 的话，intervals[i] 与 intervals[i+1] 即在一个区间。

官方解法：
1. 排序。
按照区间的左端点排序，那么在排完序的列表中，可以合并的区间一定是连续的。
算法：
 - 用数组 merged 存储最终的答案。
 - 首先，将列表中区间按左端点升序排序。然后将第一个区间加入 merged，并按顺序考虑之后的每个区间：
    - 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，因此可以直接将该区间加入 merged 的末尾。
    - 否则，它们重合，则用当前区间的右端点更新 merged 中最后一个区间的右端点，将其置为二者的较大值。

时间复杂度：O(n*log n)。排序耗费 O(n*log n)。
空间复杂度：O(log n)。排序耗费 O(log n)。

"""
import unittest
from typing import List


class OfficialSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """排序。"""
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或当前区间与上一区间不重合，直接添加。
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则，和上一区间进行合并。
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_merge(self) -> None:
        self.assertListEqual(
            self.s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertListEqual(
            self.s.merge([[1, 4], [4, 5]]),
            [[1, 5]],
        )


if __name__ == '__main__':
    unittest.main()
