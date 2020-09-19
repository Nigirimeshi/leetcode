"""
3 的幂

链接：https://leetcode-cn.com/problems/power-of-three

标签：数学

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？

我的解法：
1. 遍历。
n 循环除 3，当 n % 3 不等于 0 时退出循环；若 n 是 3 的幂次方，退出循环后值应为 1。
时间复杂度：O(logb(n))，b 是 n / 3 的次数。
空间复杂度：O(1)，没有使用额外的空间。

官方解法：
1. 整数限制。
n 的类型是 int。在 Java 中说明了该变量是四个字节，他的最大值为 2147483647。
知道了 n 的限制，我们现在可以推断出 n 的最大值，也就是 3 的幂，是 1162261467。
因此我们只需要将 3^19 除以 n，若余数为 0 意味着 n 是 3^19 的除数，因此是 3 的幂。

"""
import unittest


class Solution:
    def is_power_of_three(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3
        return n == 1


class OfficialSolution:
    def is_power_of_three(self, n: int) -> bool:
        """整数限制。"""
        return n > 0 and 1162261467 % n == 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_power_of_three(self) -> None:
        self.assertTrue(self.s.is_power_of_three(27))
        self.assertFalse(self.s.is_power_of_three(0))
        self.assertTrue(self.s.is_power_of_three(9))
        self.assertFalse(self.s.is_power_of_three(45))


if __name__ == '__main__':
    unittest.main()
