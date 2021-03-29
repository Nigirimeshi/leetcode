package leetcode

import (
	"testing"

	"leetcode/utils"
)

/*
排序数组

链接：https://leetcode-cn.com/problems/sort-an-array

给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

解法：
1. 快速排序。
时间复杂度：O(logN)
空间复杂度：O(1)
*/

func quickSort(nums []int, left, right int) {
	if left >= right {
		return
	}

	pivot := partition(nums, left, right)
	quickSort(nums, left, pivot-1)
	quickSort(nums, pivot+1, right)
}

func partition(nums []int, left, right int) int {
	pivot := left

	for left < right {
		// 从右向右移动，找到小于等于 nums[pivot] 的。
		for left < right && nums[right] > nums[pivot] {
			right--
		}
		// 从左向右移动，找到大于 nums[pivot] 的。
		for left < right && nums[left] <= nums[pivot] {
			left++
		}
		// 此时 right 刚好指向一个小于等于 nums[pivot] 的值，right 刚好指向一个大于 nums[pivot] 的值，交换它们。
		nums[left], nums[right] = nums[right], nums[left]
	}
	// 此时 left 和 right 指向同一位置，与 pivot 交换。
	nums[pivot], nums[right] = nums[right], nums[pivot]
	return right
}

func TestQuickSort(t *testing.T) {
	tests := []struct {
		nums []int
		want []int
	}{
		{nums: []int{1}, want: []int{1}},
		{nums: []int{5, 2, 3, 1}, want: []int{1, 2, 3, 5}},
		{nums: []int{5, 1, 1, 2, 0, 0}, want: []int{0, 0, 1, 1, 2, 5}},
		{nums: []int{-4, 0, 7, 4, 9, -5, -1, 0, -7, -1}, want: []int{-7, -5, -4, -1, -1, 0, 0, 4, 7, 9}},
	}
	for i := range tests {
		tc := tests[i]
		quickSort(tc.nums, 0, len(tc.nums)-1)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("quickSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}
