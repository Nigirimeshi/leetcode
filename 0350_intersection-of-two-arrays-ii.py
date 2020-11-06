"""
两个数组的交集 II

链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii

给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。

进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

我的解题思路：
1. 哈希表。
首先分别计算 nums1，nums2 中各个数字出现的次数，
遍历 nums2，若 nums1 中存在相同数字，取次数最小值，并将该数字加入结果数组。

时间复杂度：O(m+n)
空间复杂度：O(m+n)

官方解法：
1. 哈希表。
首先用哈希表存储第一个数组中各元素的出现次数，
然后遍历第二个数组，若元素在哈希表中，则将元素加入结果集，并将哈希表中该元素减 1，
哈希表中元素为 0 时可删除。

为了降低时间复杂度，首先遍历较短的数组，并用哈希表存储次数，然后再遍历较长数组，得到交集。

时间复杂度：O(m+n)
空间复杂度：O(min(m, n))

2. 排序（双指针）。
首先对两个数组排序，然后使用两个指针遍历两个数组。
初始时，两个指针分别指向两个数组的头部。
每次比较两个指针指向的两个数字：
 - 若两个数字不相等，则将指向较小数字的指针右移一位；
 - 若两个数字相等，则将该数字加入答案，并使两个指针都右移一位。
当任一指针超出数组范围时，退出循环。

时间复杂度：O(mlogm + nlogn)
空间复杂度：O(min(m, n))

"""
from collections import Counter
from typing import List
import unittest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """哈希表。"""
        counts_nums1 = Counter(nums1)
        counts_nums2 = Counter(nums2)
        
        ans = []
        for num in counts_nums1.keys():
            if counts_nums2[num]:
                min_count = min(counts_nums1[num], counts_nums2[num])
                ans += [num] * min_count
        
        return ans


class OfficialSolution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """哈希表。"""
        # 为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
            
            # 计算较短数组中元素次数。
        counts = Counter(nums1)
        
        ans = []
        for num in nums2:
            if counts[num] > 0:
                ans.append(num)
                # 将哈希表中对应数字减 1，若等于 0 了，直接删除。
                counts[num] -= 1
                if counts[num] == 0:
                    counts.pop(num)
        return ans
    
    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """排序（双指针）。"""
        nums1.sort()
        nums2.sort()
        
        ans = []
        # 初始化指针。
        p1, p2 = 0, 0
        # 当任一指针超出数组范围时，退出循环。
        while p1 < len(nums1) and p2 < len(nums2):
            # 当数字相同时，将其加入答案，并使两个指针都右移一位。
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            # 数字不同时，将较小元素指针右移一位。
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            
            # nums1[p1] > nums2[p2]
            else:
                p2 += 1
        
        return ans


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_intersect(self) -> None:
        self.assertListEqual(
            self.s.intersect([1, 2, 2, 1], [2, 2]),
            [2, 2],
        )


if __name__ == '__main__':
    unittest.main()
