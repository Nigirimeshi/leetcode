"""
三数之和

链接：https://leetcode-cn.com/problems/3sum

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0，请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

官方解法：
1. 排序 + 双指针。
难点在于去除重复解。
算法流程：
1) 特判，若数组长度不足 3，立即返回 []；
2) 将数组排序；
3) 遍历排序后的数组：
3.1) 若 nums[i] > 0，由于数组已经排序好了，所以后面不可能有 3 个数加起来等于 0，此时直接返回结果；
3.2) 跳过重复元素，避免重复解；
3.3) 令左指针 L 等于 i + 1，右指针 R 等于 n - 1，当 L < R 时，执行循环：
3.3.1) 当 nums[i] + nums[L] + nums[R] == 0 的适合，记录解，并执行循环，跳过左右指针下一位的重复元素，并将 L，R 移动到下一位置；
3.3.2) 若 nums[i] + nums[L] + nums[R] 大于 0，说明 nums[R] 太大，需要左移；
3.3.3) 当 nums[i] + nums[L] + nums[R] 小于 0，说明 nums[L] 太小，需要右移。

时间复杂度：O(n^2)。数组排序 O(NlogN)，遍历数组 O(n)，双指针遍历 O(n)，总体 O(NlogN) + O(n) * O(n)。
空间复杂度：O(1)。我们修改了输入的数组 nums，在实际情况下不一定允许，
因此也可以看成使用了一个额外的数组存储了nums 的副本并进行排序，空间复杂度为 O(N)。

"""
import unittest
from typing import List


class OfficialSolution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """排序 + 双指针。"""
        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        ans = []

        for i in range(n):
            # 当遍历到的元素大于 0 时，后面不可能存在 3 个数相加等于 0，此时直接返回结果。
            if nums[i] > 0:
                return ans
            # 跳过重复元素。
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 设置左、右指针。
            left, right = i + 1, n - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的左右指针对应的元素。
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 移动左右指针。
                    left += 1
                    right -= 1

                # 和大于 0，说明 nums[right] 偏大，需要左移。
                elif sums > 0:
                    right -= 1

                # 和小于 0，说明 nums[left] 偏小，需要右移。
                else:
                    left += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_three_sum(self) -> None:
        print(self.s.three_sum([-1, 0, 1, 2, -1, -4]))
        print(self.s.three_sum([0, 0, 0, 0]))
        print(self.s.three_sum([3, 0, -2, -1, 1, 2]))
        print(self.s.three_sum(
            [-12, -1, 4, -14, 0, 10, 7, -7, -6, 9, 6, -2, 7, 13, 9, -1, 4, 12, 9, 4, 14, 0, -4, 0, 0, 10, 2, -7, 7, -4,
             -11, 10, 2, 8, 4, -12, -4, -12, -4, -3, 12, 9, 11, 4, -1, -3, 10, -12, -6, -4, -1, -14, 3, 2, -7, -11, -3,
             10, -11, -10, 13, -15, 7, 0, 0, -4, -5, 11, 0, -2, -14, -11, -8, 12, 1, -1, -14, -12, -6, -5, 0, 9, -4,
             -12, -4, 4, 14, 9, -9, 10, 14, -11, 10, 6, -3, -4, 10, -1, 14, -13, 13, 7, -9, 12, 4, -1, -4, 5, 3, 6, 8,
             10, 0, 11, 13, 11, -7, 5, -3, -1, 0, -4, -4, -4, 10, 0]))


if __name__ == '__main__':
    unittest.main()
