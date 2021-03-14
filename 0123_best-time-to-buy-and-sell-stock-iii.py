"""
买卖股票的最佳时机 III

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    
示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。

示例 4：
输入：prices = [1]
输出：0

提示：
1 <= prices.length <= 105
0 <= prices[i] <= 105

解法：
1. 动态规划（状态机）

"""
import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp: List[List[List[int]]] = [
            [[0 for ___ in range(2)] for __ in range(max_k + 1)] for _ in range(n)
        ]

        # 边界条件，base case。
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float("inf")

        # 上面已经包含了 k = 0 的情况，所以从 1 开始，到 max_k 结束。
        for k in range(1, max_k + 1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]

        for i in range(1, n):
            for k in range(1, max_k + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 穷举了 n * max_k 个状态。
        return dp[n - 1][max_k][0]

    def max_profit_2(self, prices: List[int]) -> int:
        """动态规划（状态机）"""
        n = len(prices)
        max_k = 2
        dp: List[List[List[int]]] = [
            [[0 for ___ in range(2)] for __ in range(max_k + 1)] for _ in range(n)
        ]
        for i in range(n):
            for k in range(max_k + 1):
                if i == 0:
                    # dp[0][k][0] = max(dp[-1][k][0], dp[-1][k][1] + prices[0])
                    # dp[0][k][0] = max(0, -infinity + prices[0])
                    # dp[0][k][0] = 0
                    dp[0][k][0] = 0

                    # dp[0][k][1] = max(dp[-1][k][1], dp[-1][k][0] - prices[0])
                    # dp[0][k][1] = max(-infinity, -prices[0])
                    # dp[0][k][1] = -prices[0]
                    dp[0][k][1] = -prices[0]
                    continue

                if k == 0:
                    # 不允许交易，未持有股票，利润为 0。
                    dp[i][0][0] = 0
                    # 不允许交易，不可能持有股票，用负无穷表示。
                    dp[i][0][1] = float("-inf")
                    continue

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]

    def max_profit_3(self, prices: List[int]) -> int:
        """动态规划 - 穷举（空间复杂度为 1）"""
        n = len(prices)
        """
        dp[i][0][0] = 0         # 没买过股票，也没持有股票，利润为 0。
        dp[i][0][1] = -infinity # 没买过股票，却持有股票，不可能，用负无穷表示。
        
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                    = max(dp[i-1][1][1], -prices[i])
                    
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
        """

        dp_i_1_0, dp_i_1_1 = 0, float("-inf")
        dp_i_2_0, dp_i_2_1 = 0, float("-inf")
        for price in prices:
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + price)
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - price)

            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + price)
            dp_i_1_1 = max(dp_i_1_1, -price)

        return dp_i_2_0


class Cases:
    def __init__(self, prices: List[int], want: int):
        self.prices: List[int] = prices
        self.want: int = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_max_profit(self):
        test_cases = (
            Cases([3, 3, 5, 0, 0, 3, 1, 4], 6),
            Cases([1, 2, 3, 4, 5], 4),
            Cases([7, 6, 4, 3, 1], 0),
        )

        for tc in test_cases:
            output = self.s.max_profit_3(tc.prices)
            self.assertEqual(tc.want, output)


if __name__ == "__main__":
    unittest.main()
