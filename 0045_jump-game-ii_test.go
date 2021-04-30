package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

/*
跳跃游戏 ii

链接：https://leetcode-cn.com/problems/jump-game-ii

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: [2,3,0,1,4]
输出: 2

提示:
1 <= nums.length <= 1000
0 <= nums[i] <= 105

解法：
1. 模拟跳跃。
1）初始化当前可跳跃的区间 [start, end] = [0, 0]；
2）遍历区间 [start, end] 内的元素，计算能够跳跃到的最远位置下标；
3）更新 start 和 end 位置；
4）若 end >= (len(nums) - 1)，说明已到达最后一个位置。

时间复杂度：O(N)
空间复杂度：O(1)

*/

func jump(nums []int) int {
	// 记录跳跃次数。
	ans := 0
	// 跳跃的起始、结束位置。
	start, end := 0, 0
	// 当 end >= 数组下标范围，说明已跳跃过了最后一个位置。
	for end < (len(nums) - 1) {
		// 记录可跳跃到的最远位置。
		maxPos := 0
		// 计算可跳跃到的最远位置。
		for i := start; i <= end; i++ {
			// 当前元素可跳跃的最远位置。
			currMaxPos := i + nums[i]
			// 更新可跳跃到的最远位置。
			if currMaxPos > maxPos {
				maxPos = currMaxPos
			}
		}

		start = end + 1 // 更新下次跳跃的起始位置。
		end = maxPos    // 更新下次跳跃的结束位置。
		ans++           // 更新跳跃次数。
	}
	return ans
}

func TestJump(t *testing.T) {
	cases := []struct {
		nums []int
		want int
	}{
		{[]int{2, 3, 1, 1, 4}, 2},
		{[]int{2, 3, 0, 1, 4}, 2},
	}

	for i := range cases {
		tc := cases[i]
		output := jump(tc.nums)
		assert.Equal(t, tc.want, output)
	}
}
