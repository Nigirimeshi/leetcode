"""
两数之和 II - 输入有序数组

链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted

给定一个已按照 升序排列的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，

所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]

示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]

提示：
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案

我的解题思路：
1. 哈希表（没充分利用数组有序）。
首先用哈希表记录数组元素出现次数及下标数组，
遍历哈希表的 key，查找 target - key 是否存在于哈希表中，若存在，取出索引值，
比较索引值，确保 index1 小于 index2。

官方解法：
1. 二分查找。
首先遍历有序序列，固定第一个数，
然后二分查找第二个数，第二个数等于 target 减去第一个数，
为了避免重复查找，只在第一个数的右侧寻找第二个数。

时间复杂度：O(NlogN)
空间复杂度：O(1)

2. 双指针。

设置指针 left，right 分别指向数组最左端和最右端下标。
比较两指针指向元素之和：
 - 若和等于 target，则返回 left + 1, right + 1；
 - 若和大于 target，则令 right 向左移动；
 - 若和小于 target，则令 left 向右移动。

时间复杂度：O(N)
空间复杂度：O(1)

"""
import unittest
from typing import Dict, List, Union


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """哈希表。"""
        idx: Dict[int, Dict[str, Union[int, List[int]]]] = {}
        for i, v in enumerate(numbers):
            if v not in idx:
                idx[v] = {
                    'count': 1,
                    'index': [i],
                }
            else:
                idx[v]['count'] += 1
                idx[v]['index'].append(i)
        
        index1, index2 = 0, 0
        for k in idx.keys():
            dif = target - k
            if dif in idx and idx[dif]['count'] > 0:
                index1 = idx[k]['index'].pop() + 1
                index2 = idx[dif]['index'].pop() + 1
                idx[k]['count'] -= 1
                idx[dif]['count'] -= 1
                break
        
        if index2 < index1:
            index1, index2 = index2, index1
        return [index1, index2]
    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """二分查找。"""
        n = len(numbers)
        # 遍历有序序列，固定第一个数。
        for i in range(n):
            # 只在第一个数的右侧寻找第二个数。
            low, high = i + 1, n - 1
            # 二分查找第二个数。
            while low <= high:
                mid = (low + high) // 2
                # target 与第一个数的差值。
                dif = target - numbers[i]
                # 找到了第二个数，就将索引各加一并返回。
                if numbers[mid] == dif:
                    return [i + 1, mid + 1]
                # 修改右边界，向左查找。
                elif numbers[mid] > dif:
                    high = mid - 1
                # 修改左边界，向右查找。
                else:
                    low = mid + 1
        return [-1, -1]

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        """双指针。"""
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > total:
                right -= 1
            else:
                left += 1
        return [-1, -1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
