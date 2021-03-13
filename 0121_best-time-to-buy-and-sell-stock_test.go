package leetcode

import (
	"math"
	"testing"
)

/*
买卖股票的最佳时机

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
*/

func maxProfit(prices []int) int {
	n := len(prices)
	dpI0, dpI1 := 0, math.MinInt32
	for i := 0; i < n; i++ {
		dpI0 = max(dpI0, dpI1+prices[i])
		dpI1 = max(dpI1, -prices[i])
	}
	return dpI0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func TestMaxProfit(t *testing.T) {
	testcases := []struct {
		prices []int
		want   int
	}{
		{prices: []int{7, 1, 5, 3, 6, 4}, want: 5},
		{prices: []int{7, 6, 4, 3, 1}, want: 0},
	}

	for _, tc := range testcases {
		output := maxProfit(tc.prices)
		if output != tc.want {
			t.Errorf("maxProfit(%v) return: %v != %v\n", tc.prices, output, tc.want)
		}
	}
}
