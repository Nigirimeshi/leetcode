""""
除自身以外数组的乘积

标签：数组

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output，

其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

我的解题思路：
1.
首先得到 nums 中所有元素的乘积，然后遍历 nums，每个元素的结果只需要用所有元素的乘积除以遍历到的元素即可。
但是，题目要求不使用除法。

特殊情况：
 - 存在 0。

官方解法：
1. 乘积 = 当前数左边的乘积 * 当前数右边的乘积。

时间复杂度：O(n)
空间复杂度：O(1) 输出数组不被视为额外空间。

"""
from typing import List
import unittest


class OfficialSolution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """乘积 = 左乘积 * 右乘积。"""
        ans = [1] * len(nums)
        
        # 计算各元素左边的乘积。
        k = 1
        for i in range(len(nums)):
            ans[i] = k
            k *= nums[i]
        
        # 计算各元素右边的乘积，从右向左遍历，并乘上已经计算好的左边乘积。
        k = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= k
            k *= nums[i]
        
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_product_except_self(self) -> None:
        self.assertListEqual(
            self.s.product_except_self([1, 2, 3, 4]),
            [24, 12, 8, 6],
        )


if __name__ == '__main__':
    unittest.main()
