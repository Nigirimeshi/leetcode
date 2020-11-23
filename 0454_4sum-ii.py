""""
四数相加 II

链接：https://leetcode-cn.com/problems/4sum-ii

给定四个包含整数的数组列表 A , B , C , D, 计算有多少个元组 (i, j, k, l)，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度N，且 0 ≤ N ≤ 500 。

所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

解法：
1. 如果是两个数组，可以用哈希表存一组，然后遍历另一组，和哈希表对比。
题目有 4 个数组，可分为 3 种情况：
1）哈希表存 1 个数组，然后嵌套遍历另外 3 个数组进行对比，时间复杂度为 O(n) + O(n^3) = O(n^3)
2）哈希表存 3 个数组之和，然后遍历剩下的 1 个数组进行对比，时间复杂度为 O(n^3) + O(n) = O(n^3)
3）哈希表存 2 个数组之和，然后嵌套遍历另外 2 个数组进行对比，时间复杂度为 O(n^2) + O(n^2) = O(n^2)
由上可知，选择第 3 种方法时间复杂度相对较低。

具体步骤：
1）首先求出 A 和 B 两个数组中任意 2 数之和 sumAB，并将 sumAB 作为 key，sumAB 出现的次数为 value，存储在哈希表中。
2）然后求出 C 和 D 两个数组中任意 2 数之和的相反数 sumCD，若哈希表中存在 sumCD，则累加对应 value。

时间复杂度：O(n^2)
空间复杂度：O(2n)

"""
from collections import Counter
from typing import List
import unittest


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        哈希表。
        首先用哈希表存 2 组数组任意元素之和，
        然后用剩下 2 组数组任意元素之和的相反数，去哈希表中查找是否存在：
        - 若存在，则累加哈希表中对应元素的 value。

        时间复杂度：O(N^2)
        空间复杂度：O(2N)
        """
        counts = Counter([a + b for a in A for b in B])
        return sum(counts.get(-(c + d), 0) for c in C for d in D)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
