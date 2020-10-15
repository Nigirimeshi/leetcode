"""
阶乘后的零

标签：数学

链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零。

说明: 你算法的时间复杂度应为 O(logn)。

我的解题思路：
1. 计算阶乘。（通过：× 超时）
时间复杂度：低于 O(n^2)。
空间复杂度：O(logn!) = O(nlogn)。

官方解法：
1. 计算因子 5。
末尾 0 的个数，取决于能除几次 10。
对于 5! = 5 * 4 * 3 * 2 * 1 = 120，发现 2 和 5 相乘构成了 10，所以只需要找出有多少对 5 和 2。
再分解一下：
11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    = 11 * (5 * 2) * 9 * (4 * 2) * 7 * (3 * 2) * (1 * 5) * (2 * 2) * 3 * (1 * 2) * 1
含有 2 的因子有：(5 * 2), (4 * 2), (3 * 2), (2 * 2), (1 * 2)
含有 5 的因子有：(5 * 2), (5 * 1)
其中 2 的数量远超于 5，所以计算 2 和 5 的对数，仅需计算 5 即可。

进一步分析，从 1 到 n 的每位数字中，只有 5，10，15...等至少有 1 个 5，所以，不必一步步向上迭代，可以 5 步向上迭代。

时间复杂度：O(n)。
空间复杂度：O(1)。

2. 高效的计算因子 5。
进一步可以发现，fives = n/5 + n/25 + n/125 + 5/625 +...
这样看起来会一直计算下去，但是并非如此！
我们使用整数除法，最终，分母将大于 n，因此当项等于 0 时，就可以停止我们的计算。

时间复杂度：O(logn)。
空间复杂度：O(1)。

"""
import unittest


class Solution:
    def trailing_zeroes(self, n: int) -> int:
        n_factorial = 1
        for i in range(2, n + 1):
            n_factorial *= i

        ans = 0
        while n_factorial > 10:
            if n_factorial % 10 == 0:
                ans += 1
                n_factorial //= 10
            else:
                break
        return ans


class OfficialSolution:
    def trailing_zeroes(self, n: int) -> int:
        """计算因子 5。"""
        zero_count = 0
        for i in range(5, n + 1, 5):
            cur = i
            while cur % 5 == 0:
                zero_count += 1
                cur //= 5
        return zero_count

    def trailing_zeroes_2(self, n: int) -> int:
        """高效的计算因子 5。"""
        zero_count = 0
        curr_multiple = 5
        while n >= curr_multiple:
            zero_count += n // curr_multiple
            curr_multiple *= 5
        return zero_count


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_trailing_zeroes(self) -> None:
        self.assertEqual(
            self.s.trailing_zeroes_2(3),
            0,
        )
        self.assertEqual(
            self.s.trailing_zeroes_2(5),
            1,
        )
        self.assertEqual(
            self.s.trailing_zeroes_2(10),
            2,
        )
        self.assertEqual(
            self.s.trailing_zeroes_2(100),
            24,
        )
        self.assertEqual(
            self.s.trailing_zeroes_2(1000),
            249,
        )


if __name__ == '__main__':
    unittest.main()
