"""
杨辉三角

链接：https://leetcode-cn.com/problems/pascals-triangle

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

我的解题思路：
1. 迭代生成三角形的每一行（索引为 i），每一列（索引为 j）。
每行的首、位元素为 1，每行的其他元素等于上一行的前一列加上一行的当前列，即 ans[i-1][j-1] + ans[i-1][j]。

时间复杂度：O(n^2)
空间复杂度：O(n^2)

"""
import unittest
from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        ans = []
        for i in range(num_rows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                    continue
                tmp.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(tmp)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_generate(self) -> None:
        self.assertListEqual(
            self.s.generate(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ],
        )


if __name__ == '__main__':
    unittest.main()
