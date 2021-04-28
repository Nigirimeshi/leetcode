package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

/*
除自身以外数组的乘积

标签：数组

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output，

其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

特殊情况：
 - 存在 0。

官方解法：
1. 乘积 = 当前数左边的乘积 * 当前数右边的乘积。

时间复杂度：O(n)
空间复杂度：O(1) 输出数组不被视为额外空间。

*/

func productExceptSelf(nums []int) []int {
	n := len(nums)
	output := make([]int, n, n)

	// output[i] 为 nums[i] 左侧所有元素的乘积。
	// 因为下标 0 左边没有元素，所以初始化为 1。
	output[0] = 1
	for i := 1; i < n; i++ {
		output[i] = nums[i-1] * output[i-1]
	}

	// output[j] 为 nums[j] 右侧所有元素的乘积。
	// 因为下标 n - 1 右边没有元素，所以初始化为 1。
	val := 1
	for j := n - 1; j >= 0; j-- {
		output[j] *= val
		val *= nums[j]
	}

	return output
}

func TestProductExceptSelf(t *testing.T) {
	cases := []struct {
		nums, want []int
	}{
		{
			[]int{1, 2, 3, 4}, []int{24, 12, 8, 6},
		},
	}
	for i := range cases {
		tc := cases[i]
		output := productExceptSelf(tc.nums)
		assert.ElementsMatch(t, tc.want, output)
	}
}
