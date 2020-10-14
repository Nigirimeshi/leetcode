"""
快乐数

标签：数学

链接：https://leetcode-cn.com/problems/happy-number

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

我的解题思路：
1. 暴力计算。
依次计算各位数字平方和，递归判断是否为 1。
用集合记录已出现过的平方和以及 n，若递归过程中出现重复数字，说明会无限循环，此时返回 False。

官方解法：
1. 用哈希集合检查循环。（通过：√）
每次计算各位数字平方和，最终会有以下 3 种可能：
 - 最终得到 1。
 - 无限循环。
 - 值越来越大，最后接近无穷大。
   对于 3 位数的数字，它不可能大于 243。
   这意味着它要么被困在 243 以下的循环内，要么跌到 1。
   4 位或 4 位以上的数字在每一步都会丢失一位，直到降到 3 位为止。
   所以我们知道，最坏的情况下，算法可能会在 243 以下的所有数字上循环，
   然后回到它已经到过的一个循环或者回到 1。
   但它不会无限期地进行下去，所以我们排除第三种选择。

时间复杂度：O(243⋅3 + logn + loglogn + logloglogn)... = O(logn)。
空间复杂度：O(logn)。

2. 快慢指针检查环。
反复计算平方和实际得到的链是一个链表，只需要判断链表是否有环，即可判断无限循环计算的情况。
slow 指针每次移动 1 个结点，fast 每次移动 2 个结点。
 - 若 slow 和 fast 相等，则存在环，返回 False；
 - 若 fast 等于 1，则返回 True。

时间复杂度：O(logn)。
空间复杂度：O(1)。

"""
import unittest
from typing import Set


class Solution:
    def is_happy(self, n: int) -> bool:
        return self.compute(n, {n, })

    def compute(self, n: int, nums: Set[int]) -> bool:
        if n == 1:
            return True

        _sum = 0
        while n > 0:
            num = n % 10
            _sum += num * num
            n //= 10

        if _sum in nums:
            return False

        nums.add(_sum)
        return self.compute(_sum, nums)


class OfficialSolution:
    def is_happy(self, n: int) -> bool:
        """快慢指针检查环。"""
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1

    def get_next(self, n: int) -> int:
        _sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            _sum += digit ** 2
        return _sum


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_happy(self) -> None:
        self.assertTrue(
            self.s.is_happy(1)
        )
        self.assertTrue(
            self.s.is_happy(19)
        )
        self.assertFalse(
            self.s.is_happy(123)
        )


if __name__ == '__main__':
    unittest.main()
