"""
两整数之和

链接：https://leetcode-cn.com/problems/sum-of-two-integers

不使用运算符 + 和 -，计算两整数 a、b 之和。

示例 1:
输入: a = 1, b = 2
输出: 3

示例 2:
输入: a = -2, b = 3
输出: 1

参考解法：
1. 异或和与运算。
对于 python 来说,主要的难点在于, python 整数类型为 Unifying Long Integers, 即无限长整数类型，需要额外处理溢出值。
python 由于不知道符号位是第几位，因此需要额外操作：
 1. 将输入数字转成无符号整数；
 2. 计算无符号整数并相加得到结果；
 3. 将结果根据范围判断，映射为有符号整数。

"""
import unittest


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        """异或运算获得和，与运算获得进位。"""
        # 转为 32 bit 无符号整数，0xFFFFFFFF = 2^32 - 1。
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF

        # 无符号整数加法。
        while b:
            # 获取进位位置，再左移 1 位，就是正确的位置。
            carry = a & b
            # 计算和，缺少进位。
            a ^= b
            # 模拟溢出操作。
            b = (carry << 1) & 0xFFFFFFFF

        # 若超出范围，则符号位一定是负，映射为有符号整数，0x80000000 = 2^31。
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_get_sum(self) -> None:
        self.assertEqual(
            self.s.get_sum(1, 2),
            3,
        )
        self.assertEqual(
            self.s.get_sum(-2, -2),
            -4,
        )


if __name__ == '__main__':
    unittest.main()
