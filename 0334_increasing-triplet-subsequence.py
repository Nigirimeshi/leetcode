"""
递增的三元子序列

链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k, 且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true；否则返回 false。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:
输入: [1,2,3,4,5]
输出: true

示例 2:
输入: [5,4,3,2,1]
输出: false

官方解法：
1. 双指针。
用 n1，n2 分别保存较小的数，且 n1 < n2，若还存在一个数大于 n2，则说明存在 3 个递增子序列。

时间复杂度：O(n)
空间复杂度：O(1)

"""
from typing import List
import unittest


class OfficialSolution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        """双指针。"""
        n1, n2 = float('inf'), float('inf')
        for num in nums:
            # 保存第一个较小的数。
            if n1 >= num:
                n1 = num
            
            # 保存第二个较小的数，且大于第一个数。
            elif n2 >= num:
                n2 = num
            
            # 同时大于 n1，n2。
            else:
                return True
        return False


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_increasing_triplet(self) -> None:
        self.assertTrue(self.s.increasing_triplet([1, 2, 3, 4, 5]))
        self.assertFalse(self.s.increasing_triplet([5, 4, 3, 2, 1]))
        self.assertTrue(self.s.increasing_triplet([5, 1, 5, 5, 2, 5, 4]))
        self.assertFalse(self.s.increasing_triplet([0, 4, 2, 1, 0, -1, -3]))
        self.assertFalse(self.s.increasing_triplet(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
