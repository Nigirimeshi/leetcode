"""
Excel 表列序号

链接：https://leetcode-cn.com/problems/excel-sheet-column-number

给定一个Excel表格中的列名称，返回其相应的列序号。

例如：
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701

我的解题思路：
1. 26 进制。

时间复杂度：O(n)。
空间复杂度：O(1)。

"""
import unittest


class Solution:
    def title_to_number(self, s: str) -> int:
        """26进制。"""
        ans = 0
        for c in s:
            num = ord(c) - ord('A') + 1
            ans = ans * 26 + num
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_title_to_number(self) -> None:
        self.assertEqual(
            self.s.title_to_number('A'),
            1,
        )
        self.assertEqual(
            self.s.title_to_number('AB'),
            28,
        )
        self.assertEqual(
            self.s.title_to_number('ZY'),
            701,
        )


if __name__ == '__main__':
    unittest.main()
