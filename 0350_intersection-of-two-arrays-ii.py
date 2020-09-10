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
1. 先用哈希表分别记录两数组中各元素个数，再取哈希表中相同元素的最小值，该值即为该元素出现在交集内的次数。
"""
import collections
from typing import List, Dict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def count(nums) -> Dict[int, int]:
            d = dict()
            for k in nums:
                if not d.__contains__(k):
                    d[k] = 1
                    continue
                d[k] += 1
            return d

        d1 = count(nums1)
        d2 = count(nums2)

        intersection = list()
        for k in d1.keys():
            if not d2.__contains__(k):
                continue
            for i in range(min(d1[k], d2[k])):
                intersection.append(k)

        return intersection


class OfficialSolution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection


def main():
    s = Solution()
    s.intersect([1, 2, 2, 1], [2, 2])


if __name__ == '__main__':
    main()
