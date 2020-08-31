"""
给定一个整数数组，判断是否存在重复元素。

链接：https://leetcode-cn.com/problems/contains-duplicate

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """我的第一种解法：比较去重后的集合和列表长度"""
        return len(set(nums)) != len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """我的第二种解法：先排序，如果存在重复元素，排序后它们应该相邻"""
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


def main():
    s = Solution()
    result = s.containsDuplicate([1, 2, 3, 1])
    if result:
        print("ok")
    else:
        print("wrong")


if __name__ == '__main__':
    main()
