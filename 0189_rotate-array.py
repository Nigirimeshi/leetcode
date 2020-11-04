"""
旋转数组

链接：https://leetcode-cn.com/problems/rotate-array

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。

解法:
方法 1：暴力
最简单的方法是旋转 k 次，每次将数组旋转 1 个元素。

时间复杂度：O(n*k)。每个元素都被移动 1 步（O(n)） k 次（O(k)） 。
空间复杂度：O(1)。没有额外空间被使用。

方法 3：环状替换
我们可以试着把每一个数字放到它最后的位置，但这样的后果是遗失原来的元素。
因此，我们需要把被替换的数字保存在变量 temp 里面。
然后，将被替换数字 temp 放到它正确的位置，并继续这个过程 n 次， n 是数组的长度。
但是，这种方法可能会有个问题，如果 n % k == 0，其中 k = k % n
（因为如果 k 大于 n ，移动 k 次实际上相当于移动 k % n 次）。
这种情况下，我们会发现在没有遍历所有数字的情况下回到出发数字。此时，我们应该从下一个数字开始再重复相同的过程。

时间复杂度：O(n)
空间复杂度：O(1)


方法 4：使用反转
这个方法基于这个事实：当我们旋转数组 k 次， k%n 个尾部元素会被移动到头部，剩下的元素会被向后移动。
在这个方法中，我们首先将所有元素反转。然后反转前 k 个元素，再反转后面 n-k 个元素，就能得到想要的结果。

假设 n=7 且 k=3。
原始数组                  : 1 2 3 4 5 6 7
反转所有数字后             : 7 6 5 4 3 2 1
反转前 k 个数字后          : 5 6 7 4 3 2 1
反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果

时间复杂度：O(n) 。 n 个元素被反转了总共 3 次。
空间复杂度：O(1) 。 没有使用额外的空间。

"""
from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """暴力。"""
        for i in range(k):
            previous = nums[len(nums) - 1]
            for j in range(len(nums)):
                tmp = nums[j]
                nums[j] = previous
                previous = tmp
    
    def rotate_3(self, nums: List[int], k: int) -> None:
        """环状替换。"""
        pass
    
    def rotate_4(self, nums: List[int], k: int) -> None:
        """反转。"""
        
        def reverse(arr: List[int], start, end: int) -> None:
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1
        
        length = len(nums)
        k = k % length
        reverse(nums, 0, length - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, length - 1)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_rotate(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.s.rotate(nums, 3)
        self.assertListEqual(nums, [5, 6, 7, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
