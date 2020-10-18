"""
x 的平方根

链接：https://leetcode-cn.com/problems/sqrtx

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2

说明: 8 的平方根是 2.82842...,
    由于返回类型是整数，小数部分将被舍去。

官方解法：
1. 二分法。
由于 x 平方根的整数部分是满足 k^2 < x 的最大值 k，因此可以对 x 进行二分查找。
二分查找的下界为 0，上界可以粗略的设定为 x。
二分查找的每一步中，只需比较中间值 mid 的平方与 x 的大小，并通过比较调整上下界的范围。
由于所有运算都是整数运算，不会存在误差，因此得到 ans 后，不需要再去尝试 ans + 1 了。

时间复杂度：O(logN)。
空间复杂度：O(1)。

"""
import unittest


class OfficialSolution:
    def my_sqrt(self, x: int) -> int:
        """二分法。"""
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_my_sqrt(self) -> None:
        self.assertEqual(
            self.s.my_sqrt(4),
            2,
        )
        self.assertEqual(
            self.s.my_sqrt(8),
            2,
        )


if __name__ == '__main__':
    unittest.main()
