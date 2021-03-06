"""
位 1 的个数

链接：https://leetcode-cn.com/problems/number-of-1-bits

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 1：
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

示例 2：
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

示例 3：
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。
在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的示例 3 中，输入表示有符号整数 -3。

进阶:
如果多次调用这个函数，你将如何优化你的算法？

官方解法：
1. 循环和位移动。
遍历数字的 32 位，如果某一位是 1，计数器加 1。

时间复杂度：O(1)。运行时间依赖于数字 nn 的位数。由于这题中 nn 是一个 32 位数，所以运行时间是 O(1) 的。
空间复杂度：O(1)。没有使用额外空间。

"""
import unittest


class OfficialSolution:
    def hamming_weight(self, n: int) -> int:
        count = 0
        mask = 1
        i = 0
        while i < 32:
            if (n & mask) != 0:
                # 与运算结果不为 0，说明该位数字为 1，计数器加 1。
                count += 1
            mask <<= 1
            i += 1
        return count


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_hamming_weight(self) -> None:
        self.assertEqual(
            self.s.hamming_weight(128),
            1,
        )


if __name__ == '__main__':
    unittest.main()
