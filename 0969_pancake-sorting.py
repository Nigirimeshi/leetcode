"""
煎饼排序

链接：https://leetcode-cn.com/problems/pancake-sorting

给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。

一次煎饼翻转的执行过程如下：

选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。

以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。

任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。

示例 1：
输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。

示例 2：
输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。

提示：
1 <= arr.length <= 100
1 <= arr[i] <= arr.length
arr 中的所有整数互不相同（即，arr 是从 1 到 arr.length 整数的一个排列）

解法：
1. 从大到小排序。
算法：
1）找出区间 [0, i] 内最大的元素 max_，其下标是 max_idx；
2）通过 2 次翻转将最大元素放到最后的位置 i；
2.1）将 [0, max_idx] 内的元素反转，
2.2）将 [0, i] 内的元素反转，此时 max_ 即在序列尾部；
3）因为最大值已在尾部，所以下次搜索的区间变为 [0, i-1]，重复 1 ~ 3。

时间复杂度：O(n^2)
空间复杂度：O(n)

"""
import unittest
from typing import List


class Solution:
    def pancake_sort(self, arr: List[int]) -> List[int]:
        """从大到小排序。"""

        ans = []
        n = len(arr)
        for i in range(n - 1, 0, -1):
            # 找出 [0, i] 内的最大值下标。
            max_idx = self.get_max_idx(arr, i)
            # 头元素不是最大元素，才需要反转。
            if max_idx > 0:
                # 反转 [0, max_idx] 内的元素。
                arr[: max_idx + 1] = arr[: max_idx + 1][::-1]
                # 记录反转位置，max_idx + 1 是相对位置，不是下标。
                ans.append(max_idx + 1)
            # 反转 [0, i] 整个区间内的元素。
            arr[: i + 1] = arr[: i + 1][::-1]
            # 记录反转位置，i + 1 是相对位置，不是下标。
            ans.append(i + 1)

        return ans

    def get_max_idx(self, arr: List[int], end: int) -> int:
        # 找出区间 [0, end] 之间的最大值下标。
        max_idx = 0
        # 传进来的 end 是下标，所以要 + 1。
        for i in range(end + 1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx

    def pancake_sort_2(self, arr: List[int]) -> List[int]:
        """从大到小排序。"""
        ans = []
        n = len(arr)
        while n:
            # 已知输入序列为 1 到 n，最大值即为 n。
            # 首先找出最大值 n 的下标。
            idx = arr.index(n)
            # 反转 [0, idx] 内的元素。
            arr[: idx + 1] = arr[: idx + 1][::-1]
            # 记录反转相对位置。
            ans.append(idx + 1)

            # 将最大值放到序列尾部，反转 [0, n - 1] 内的元素。
            arr[:n] = arr[:n][::-1]
            ans.append(n)

            # 缩小区间。
            n -= 1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_pancake_sort(self) -> None:
        arr = []
        self.s.pancake_sort(arr)
        self.assertListEqual(
            [],
            arr,
        )

        arr = [1, 2, 3, 4]
        self.s.pancake_sort(arr)
        self.assertListEqual(
            [1, 2, 3, 4],
            arr,
        )

        arr = [3, 2, 4, 1]
        self.s.pancake_sort(arr)
        self.assertListEqual(
            [1, 2, 3, 4],
            arr,
        )


if __name__ == "__main__":
    unittest.main()
