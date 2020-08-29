"""
删除排序数组中的重复项

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

解题思路：
1. 双指针法
分别设置 fast、slow 指针，当 nums[slow] = nums[fast] 时，就增加 fast 以跳过重复项。
当遇到 nums[slow] != nums[fast] 时，说明跳过重复项的运行已经结束，因此必须将 nums[fast] 的值复制给 nums[slow+1]，
随后递增 slow，接着重复相同的过程，指导 fast 到达数组尾端。

时间复杂度：O(n)，假设数组的长度是 n，那么 slow 和 fast 分别最多遍历 n 步。
空间复杂度：O(1)。
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        官方解法：快慢指针
        时间复杂度：O(n)，假设数组的长度是 n，那么 slow 和 fast 分别最多遍历 n 步。
        空间复杂度：O(1)。
        """
        if len(nums) == 0:
            return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


def main():
    cases = [1, 1, 2]
    s = Solution()
    result = s.removeDuplicates(cases)
    print(cases)
    if result == 2:
        print('ok')
    else:
        print('wrong')


if __name__ == '__main__':
    main()
