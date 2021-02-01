"""
移除元素

链接：https://leetcode-cn.com/problems/remove-element

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

我的解题思路：
1. 双指针。(通过：√)
循环：
 1. 设置指针 left，right 指向下标 0，
 2. 先不断右移 left 指针，直到其指向的元素等于 val，
 3. 若 left 指向元素等于 val 且 right 等于 0，则将 right = left + 1，
 4. 接着不断右移 right，直到其指向的元素不等于 val，
 5. 此时交换 left，right 指向的元素，并各自右移 1 位，重复上述循环。
返回 left。

官方解法：
1. 双指针。
设 i 为 0，
遍历数组，遍历时的下标为 j：
 - 若当前元素 nums[j] 不等于 val，则令 nums[i] = nums[j]，并使 i + 1。
最后返回 i 即为所求。

时间复杂度：O(N)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """双指针。"""
        n = len(nums)
        
        if val not in nums:
            return n
        
        left, right = 0, 0
        while left < (n - 1) and right < n:
            if nums[left] != val:
                left += 1
                continue
            
            if right == 0:
                right = left + 1
            
            if nums[right] == val:
                right += 1
                continue
            
            # 交换 left 和 right 指向的元素。
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right + 1
        return left
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        """双指针。"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
