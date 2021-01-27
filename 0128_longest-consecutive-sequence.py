"""
最长连续序列。

链接：https://leetcode-cn.com/problems/longest-consecutive-sequence

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。


进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：
0 <= nums.length <= 104
-109 <= nums[i] <= 109

我的解题思路：
1. 哈希表。
思路：
1）首先用哈希表 nums_set 记录 nums 中所有数字，
2）递增排序 nums，
3）遍历有序 nums，找出最长连续序列 max_len：
3.1）若 nums[i] == nums[i-1]，则跳过；
3.2）若 nums[i] + 1 在哈希表 nums_set 中，说明连续序列长度加 1；
3.3）若 nums[i] + 1 不在哈希表 nums_set 中，说明序列中断，此时比较并更新 max_len，并将连续序列长度重新置为 1。

时间复杂度：O(NlogN)
空间复杂度：O(N)

"""
import unittest
from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """哈希表。"""
        # 索引各个数字。
        nums_set = set(nums)
        # 排序。
        nums.sort()
        ans = 0
        seq_length = 1
        for i in range(len(nums)):
            # 若当前数字和上一次数字相同，则跳过。
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 若当前数字 + 1 存在，说明序列连续，长度加 1。
            if (nums[i] + 1) in nums_set:
                seq_length += 1
            # 序列不连续，记录最大长度，并重置连续序列长度为 1。
            else:
                ans = max(ans, seq_length)
                seq_length = 1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
