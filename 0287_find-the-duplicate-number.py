"""
寻找重复数

链接：https://leetcode-cn.com/problems/find-the-duplicate-number

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），

可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
1. 不能更改原数组（假设数组是只读的）。
2. 只能使用额外的 O(1) 的空间。
3. 时间复杂度小于 O(n2) 。
4. 数组中只有一个重复的数字，但它可能不止重复出现一次。

我的解题思路：
1. 双层遍历。（超时）

官方解法：
1. 二分查找。
1.1）抽屉原理：桌上有 10 个苹果，要把这 10 个苹果放到 9 个抽屉里，无论怎样放，至少有一个抽屉的苹果会大于 2。
题目给出了数组 nums 中数字的取值范围为 1 到 n，且只有 1 个重复数字，
假设 nums 大小为 8，那么 n 就等于 7，nums 中数字取值范围为 [1, 7]，可知中位数为 4，
遍历 nums，统计小于等于 4 的元素个数 count：
 - 若 count > 4，说明 1 到 4 之间存在重复元素；
 - 若 count = 4，说明 1 到 4 之间可能存在重复元素，也可能不存在；
 - 若 count < 4，说明 5 到 7 之间存在重复元素。

时间复杂度：O(NlogN)
空间复杂度：O(1)

2. 环形链表（快慢指针）。
设指针 fast，slow 指向下标 0，fast 每次移动 2 步，slow 每次移动 1 步。
fast = nums[nums[fast]]
slow = nums[slow]
首先找出 fast 和 slow 相遇的位置，若此时下标 0 又有一个 slow 指针开始出发，原有 slow 指针继续移动，
那么两个 slow 指针必然会在环节点相遇。


"""
from typing import List
import unittest


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:
        """双层遍历。"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]


class OfficialSolution:
    def find_duplicate(self, nums: List[int]) -> int:
        """二分查找。"""
        n = len(nums)
        left, right = 1, n - 1
        while left < right:
            mid = left + (right - left) // 2
            # 计算 nums 中小于等于 mid 的元素个数。
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # 根据抽屉原理，小于等于 mid 的树的个数如果严格大于 mid 个，则重复元素一定在 [left, mid] 中。
            if count > mid:
                right = mid
            # 反之，则在 [mid + 1, right]。
            else:
                left = mid + 1
        
        return left
    
    def find_duplicate2(self, nums: List[int]) -> int:
        """环形链表。"""
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow


class OfficialTestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_find_duplicate(self) -> None:
        self.assertEqual(
            self.s.find_duplicate([1, 3, 4, 2, 2]),
            2,
        )
        self.assertEqual(
            self.s.find_duplicate([3, 1, 3, 4, 2]),
            3,
        )


if __name__ == '__main__':
    unittest.main()
