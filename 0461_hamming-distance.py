"""
汉明距离

链接：https://leetcode-cn.com/problems/hamming-distance

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

我的解题思路：
1. 先取 x 与 y 的异或值，得到 z，然后扫描 z 中 1 的位数。

官方解法：
1. 内置位计数功能。

时间复杂度：O(1)。
该算法有两个操作。计算 XOR 花费恒定时间。
调用内置的 bitCount 函数。最坏情况下，该函数复杂度为 O(k)，其中 k 是整数的位数。
在 Python 和 Java 中 Integer 是固定长度的。因此该算法复杂度恒定，与输入大小无关。

空间复杂度：O(1)，使用恒定大小的空间保存 XOR 的结果。
假设内置函数也使用恒定空间。

2. 移位。
为了计算 x 异或 y 后的值中 1 的位数，可以将该值每个位移动到最左侧或最右侧，然后检查该位是否为 1。
更准确的说，应该进行逻辑位移，移入 0 替代丢弃的位。
这里采用右移位，检查最右位是否为 1，可以使用取模运算（i % 2）或 AND 操作（i & 1），这两个操作都会屏蔽最右位以外的其他位。

时间复杂度：O(1)，在 Python 和 Java 中 Integer 的大小是固定的，处理时间也是固定的。 32 位整数需要 32 次迭代。
空间复杂度：O(1)，使用恒定大小的空间。

3. 布赖恩·克尼根算法。
布赖恩·克尼根位计数算法的基本思想：遇到最右边的 1 后，跳过中间的 0，直接跳到下一个 1。
例如：number = 10001000
当我们在 number 和 number-1 上做 AND 位运算时，原数字 number 的最右边等于 1 的比特会被移除。
          x = 1 0 0 0 1 0 0 0
      x - 1 = 1 0 0 0 0 1 1 1
x & (x - 1) = 1 0 0 0 0 0 0 0
基于以上思路，通过迭代 2 次就可以知道 10001000 中 1 的位数，而不需要迭代 8 次。

"""
import unittest


class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        distance = 0
        mask = 1
        z = x ^ y
        for i in range(32):
            if (z & mask) != 0:
                distance += 1
            mask <<= 1
        return distance


class OfficialSolution:
    def hamming_distance(self, x: int, y: int) -> int:
        """使用内置位计数器得到 1 的位数。"""
        return bin(x ^ y).count('1')

    def hamming_distance_2(self, x: int, y: int) -> int:
        """移位。"""
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor >>= 1
        return distance

    def hamming_distance_3(self, x: int, y: int) -> int:
        """布莱恩·克尼根算法。"""
        distance = 0
        xor = x ^ y
        while xor:
            distance += 1
            xor = xor & (xor - 1)
        return distance


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_hamming_distance(self) -> None:
        self.assertEqual(
            self.s.hamming_distance(1, 4),
            2,
        )


if __name__ == '__main__':
    unittest.main()
