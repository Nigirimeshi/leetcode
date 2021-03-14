"""
买卖股票的最佳时机 IV

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv

给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

提示：
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

解法：
1. 动态规划（状态机）
"""
import unittest
from typing import List


class Solution:
    def max_profit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # k 超过最多可交易次数，相当于无限。
        if k > (n // 2):
            return self.max_profit_k_inf(prices)

        dp: List[List[List[int]]] = [
            [[0 for ___ in range(2)] for __ in range(k + 1)] for _ in range(n)
        ]
        for i in range(n):
            for j in range(k + 1):
                if i == 0:
                    # dp[0][j][0] = max(dp[-1][j][0], dp[-1][j][1] + prices[0])
                    #             = max(0, -infinity + prices[0])
                    #             = 0
                    dp[0][j][0] = 0

                    # dp[0][j][1] = max(dp[-1][j][1], dp[-1][j-1][0] - prices[0])
                    #             = max(-infinity, 0 - prices[0])
                    #             = -prices[0]
                    dp[0][j][1] = -prices[0]
                    continue

                if j == 0:
                    # dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1] + prices[i])
                    #             = max(0, -infinity + prices[i])
                    #             = 0
                    # 没交易过，利润为 0。
                    dp[i][0][0] = 0

                    # dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][-1][0] - prices[i])
                    #             = max(-infinity, -infinity - prices[i])
                    #             = -infinity
                    # 没交易过，不可能持有股票。
                    dp[i][0][1] = float("-inf")
                    continue

                # 第 i 天，交易过 j 次，未持有股票，存在 2 种可能情况：
                # 1. 前一天也没持有股票，今天啥也不干。
                # 2. 前一天持有股票，然后卖了股票。
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])

                # 第 i 天，交易过 j 次，持有股票，存在 2 种可能情况：
                # 1. 前一天持有股票，今天啥也不干。
                # 2. 前一天未持有股票，然后买了股票。
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

    def max_profit_k_inf(self, prices: List[int]) -> int:
        """允许任意次交易，k 无限制。"""
        dp_i_0, dp_i_1 = 0, float("-inf")
        for price in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, tmp - price)
        return dp_i_0


class Cases:
    def __init__(self, k: int, prices: List[int], want: int):
        self.k = k
        self.prices: List[int] = prices
        self.want: int = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_max_profit(self) -> None:
        test_cases = [
            Cases(k=2, prices=[2, 4, 1], want=2),
            Cases(k=2, prices=[3, 2, 6, 5, 0, 3], want=7),
        ]
        for tc in test_cases:
            self.assertEqual(tc.want, self.s.max_profit(k=tc.k, prices=tc.prices))


if __name__ == "__main__":
    unittest.main()
