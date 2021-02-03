"""
盛最多水的容器

链接：https://leetcode-cn.com/problems/container-with-most-water

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。

在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

提示：
n = height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104

我的解题思路：
1. 暴力双层循环（提交超时！）。

时间复杂度：O(N^2)
空间复杂度：O(1)

官方解法：
1. 双指针。
设置指针 left，right 分别指向 height 头部与尾部，
易知，计算面积时，高度受两端较小值限制，可得：
 - 面积 = (right - left) * min(height[left], height[right])
然后向内移动指针，移动指针元素较小的指针：
 - 若 height[left] 小于 height[right]，将 left 右移；
 - 若 height[left] 大于 height[right]，将 right 左移；

时间复杂度：O(N)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        """暴力双层循环。"""
        n = len(height)
        max_capacity = 0
        for i in range(n):
            for j in range(i, n):
                max_capacity = max(max_capacity, (j - i) * min(height[j], height[i]))
        return max_capacity


class OfficialSolution:
    def max_area(self, height: List[int]) -> int:
        """双指针。"""
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            # 计算面积。
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_max_area(self) -> None:
        self.assertEqual(
            self.s.max_area([1, 1]),
            1
        )
        self.assertEqual(
            self.s.max_area([4, 3, 2, 1, 4]),
            16
        )


if __name__ == '__main__':
    unittest.main()
