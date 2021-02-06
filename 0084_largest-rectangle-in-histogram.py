"""
柱状图中最大的矩形

链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:
输入: [2,1,5,6,2,3]
输出: 10

官方解法：
1. 暴力解法（两边扩散）（提交：超时）。
核心：依次遍历柱形的高度，对于每个高度分别向两边扩散，求出以当前高度为矩形的最大宽度是多少。
两边扩散的过程：
 - 向左扩散：看看最多能向左延伸多长，找到大于等于当前柱形高度的最左边元素的下标；
 - 向右扩散：看看最多能向右延伸多长，找到大于等于当前柱形高度的最右边元素的下标；
对每个位置，都进行两边扩散的操作，得到一个矩形面积，求最大值。

时间复杂度：O(N^2)
空间复杂度：O(1)

2. 单调栈。
优化暴力解法中两边扩散的双重循环：
 - 暴力解法中，需要嵌套一层 while 来向左右两边寻找第 1 个比当前柱形 i 高度小的柱形，这个过程是 O(N) 的；
 - 可以利用单调栈（递增），对于栈中柱形来说，其栈中左边元素就是第 1 个比其高度小的柱形。
算法：遍历每个柱形
 - 若当前柱体高度大于等于栈顶柱体的高度，就将当前柱体下标入栈；
 - 若当前柱体高度小于栈顶柱体的高度，说明 ”当前遍历到的柱体“ 是 “栈顶柱体” 的右边界，“栈顶柱体” 左侧柱体即左边界，
   因此可将栈顶柱体出栈，计算以其为高的面积。

时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest
from typing import List


class OfficialSolution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """暴力解法（两边扩散）。"""
        n = len(heights)
        if n == 0:
            return 0
        
        area = 0
        # 依次遍历柱形的高度。
        for i in range(n):
            curr_height = heights[i]
            
            # 向左扩散，找到大于等于当前柱形高度的最左边的元素下标。
            left = i
            while left > 0 and heights[left - 1] >= curr_height:
                left -= 1
            
            # 向右扩散，找到大于等于当前柱形高度的最右边的元素下标。
            right = i
            while right < n - 1 and heights[right + 1] >= curr_height:
                right += 1
            
            # 计算当前柱形高度向两边扩散的最大面积。
            curr_area = (right - left + 1) * curr_height
            area = max(area, curr_area)
        return area
    
    def largest_rectangle_area_2(self, heights: List[int]) -> int:
        """单调栈（递增）。"""
        # 为了使代码简洁，在柱体高度数组的头部和尾部插入高度为 0 的柱体。
        heights.insert(0, 0)
        heights.append(0)
        
        # 单调递增栈，存放柱体下标。
        stack: List[int] = []
        # 最大矩形面积。
        area = 0
        # 遍历每个柱体。
        for i in range(len(heights)):
            # 若当前柱体高度小于栈顶柱体，即可计算面积。
            while stack and heights[i] < heights[stack[-1]]:
                # 弹出栈顶元素，获取对应柱体高度。
                h = heights[stack.pop()]
                # 计算面积 = 弹出栈顶元素的高度 * (当前遍历的柱体下标（右边界） - 现在的栈顶柱体下标（左边界） - 1)
                area = max(area, h * (i - stack[-1] - 1))
            
            # 当前柱体高度大于等于栈顶柱体，入栈。
            stack.append(i)
        return area


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_largest_rectangle_area(self) -> None:
        self.assertEqual(
            10,
            self.s.largest_rectangle_area_2([2, 1, 5, 6, 2, 3]),
        )


if __name__ == '__main__':
    unittest.main()
