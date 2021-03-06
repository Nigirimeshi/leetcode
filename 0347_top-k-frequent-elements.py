"""
前 k 个高频元素

链接：https://leetcode-cn.com/problems/top-k-frequent-elements

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
 - 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
 - 你的算法的时间复杂度必须优于 O(n log n)，n是数组的大小。
 - 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
 - 你可以按任意顺序返回答案。

我的解题思路：
1.
遍历数组计算各元素出现次数，同时出现次数最多的 k 个元素。

官方解法：
1. 堆。
首先遍历数组，用哈希表记录各数组出现的次数，并形成一个“出现次数数组”。
找出原数组的前 k 个高频元素，就相当于找出“出现次数数组”的前 k 大的值。
最简单的做法是给“出现次数数组”排序。但时间复杂度不符合题目要求。

因此，需要利用堆的思想：建立一个小顶堆，然后遍历“出现次数数组”。
 - 如果堆的元素个数小于 k，则可以直接插入堆中。
 - 如果堆的元素等于 k，则检查堆顶与之前出现次数的大小。
   - 若堆顶更大，说明至少有 k 个数字出现次数比当前值大，故舍弃当前值；
   - 否则，弹出栈顶，将当前值插入堆中。

时间复杂度：O(N*logK)。哈希表记录共需 O(N) 的时间，堆操作需要 O(logK)。
空间复杂度：O(N)。哈希表需用 O(N)，堆用 O(K)。

2. 桶排序。
首先用哈希表统计数字频率，
然后创建一个数组，用频率作为下标，将不同频率的数字存入对应下标集合。
最后倒叙遍历数组，跳过空桶，返回倒数后 k 个元素集合即可。

时间复杂度：O(n)
空间复杂度：O(n)

"""
from collections import Counter
import heapq
from typing import List
import unittest


class OfficialSolution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        哈希表 + 小根堆。
        首先用哈希表记录数组中各元素及次数。
        然后遍历哈希表，将对应次数及元素插入小根堆。
        保持小根堆元素个数不超过 k 个。

        时间复杂度：O(n*logk)
        空间复杂度：O(n)
        """
        # 统计各元素出现次数。
        counts = Counter(nums)
        
        # 用小根堆存储次数及元素。
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            # 确保小根堆元素个数不超过 k 个，每次弹出小根堆堆顶（即最小值），那么剩下的就是前 k 大的。
            if len(heap) > k:
                heapq.heappop(heap)

        # 获取出现频率前 k 高的元素。
        ans = []
        for _, num in heap:
            ans.append(num)

        return ans

    def top_k_frequent_2(self, nums: List[int], k: int) -> List[int]:
        """桶排序。"""
        # 统计各数字频率。
        counts = Counter(nums)
    
        # 创建桶，下标对应数字次数，值为数字集合（可能存在出现次数相同的数字）。
        # 由于下标对应次数，所以桶的长度至少为 nums 的大小 + 1。
        bucket: List[List[int]] = [[] for _ in range((len(nums) + 1))]
        for num, count in counts.items():
            # 根据次数将数字加到桶对应下标的集合中。
            bucket[count].append(num)
    
        # 从后向前（因为下标对应次数）遍历桶，跳过空集合，倒数后 k 个非空集合即为所求结果。
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            # 跳过空桶（对应下标（次数）没有数字）。
            if not bucket[i]:
                continue
        
            ans.extend(bucket[i])
            if len(ans) == k:
                break
        return ans


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_top_k_frequent(self) -> None:
        self.assertListEqual(
            self.s.top_k_frequent_2(
                [1, 1, 1, 2, 2, 3],
                2,
            ),
            [1, 2],
        )


if __name__ == '__main__':
    unittest.main()
