package leetcode

import (
	"math/rand"
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
1. 冒泡排序。
时间复杂度：O(N^2)
空间复杂度：O(1)
是否稳定：√
排序方式：内排序

2. 选择排序。
时间复杂度：O(N^2)
空间复杂度：O(1)
是否稳定：×
排序方式：内排序

3. 插入排序。
时间复杂度：O(N^2)
空间复杂度：O(1)
是否稳定：√
排序方式：内排序

4. 希尔排序。
时间复杂度：O(NlogN)
空间复杂度：O(1)
是否稳定：×
排序方式：内排序

5. 归并排序。
时间复杂度：O(NlogN)
空间复杂度：O(N)
是否稳定：√
排序方式：外排序

6. 快速排序。
时间复杂度：O(NlogN)
空间复杂度：O(NlogN)
是否稳定：×
排序方式：内排序
*/

// BubbleSort 冒泡排序。
func BubbleSort(nums []int) {
	/*
		遍历数组，每次比较相邻元素大小，小的在前，大的在后。
	*/
	n := len(nums)
	for i := 0; i < n; i++ {
		// 标记是否发生元素交换。
		flag := false
		for j := i; j < n; j++ {
			if nums[i] > nums[j] {
				nums[i], nums[j] = nums[j], nums[i]
				flag = true
			}
		}
		// 一次交换都没发生，说明已经有序。
		if !flag {
			break
		}
	}
}

// SelectionSort 选择排序。
func SelectionSort(nums []int) {
	/*
		遍历数组，构建有序序列，每次从数组中未排序区间内选择一个最小值，放到有序序列的尾部。
	*/
	n := len(nums)
	for i := 0; i < n; i++ {
		// 从 [i+1, n-1] 区间内找出最小元素下标。
		minIdx := i
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[minIdx] {
				minIdx = j
			}
		}
		// 将最小元素放到有序序列的尾部。
		nums[i], nums[minIdx] = nums[minIdx], nums[i]
	}
}

// InsertionSort 插入排序。
func InsertionSort(nums []int) {
	/*
		遍历数组，构建有序序列，依次选择排序序列中的元素，将其加入到有序序列中何时的位置。
	*/
	n := len(nums)
	if n <= 1 {
		return
	}

	// 假设第一个元素在有序区间，[1, n-1] 为未排序区间。
	for i := 1; i < n; i++ {
		tmp := i
		for j := tmp - 1; j >= 0; j-- {
			if nums[tmp] < nums[j] {
				nums[tmp], nums[j] = nums[j], nums[tmp]
				tmp = j
			} else {
				break
			}
		}
	}
}

// ShellSort 希尔排序。
func ShellSort(nums []int) {
	/*
		以一定增长序列间隔进行插入排序。
	*/
	n := len(nums)
	// 增长序列：n/2, n/2/2, ..., 1。
	for feq := n / 2; feq > 0; feq /= 2 {
		for i := 0; i < n; i++ {
			tmp := i
			for j := tmp - feq; j >= 0; j -= feq {
				if nums[tmp] < nums[j] {
					nums[tmp], nums[j] = nums[j], nums[tmp]
					tmp = j
				} else {
					break
				}
			}
		}
	}
}

// MergeSort 归并排序。
func MergeSort(nums []int) []int {
	/*
		采用分治的思想，将数组自上而下递归拆分至不可再分后，自底向上合并子数组。
	*/
	n := len(nums)
	if n <= 1 {
		return nums
	}

	mid := n / 2
	left := MergeSort(nums[:mid])
	right := MergeSort(nums[mid:])

	ans := merge(left, right)
	return ans
}

func merge(left, right []int) []int {
	n1, n2 := len(left), len(right)
	// 存放合并后的有序切片。
	arr := make([]int, 0, n1+n2)

	i, j := 0, 0
	// 交替合并切片。
	for i < n1 && j < n2 {
		if left[i] <= right[j] {
			arr = append(arr, left[i])
			i++
		} else {
			arr = append(arr, right[j])
			j++
		}
	}

	// 可能剩余 left 元素，直接追加至 arr。
	for i < n1 {
		arr = append(arr, left[i])
		i++
	}
	// 可能剩余 right 元素，直接追加至 arr。
	for j < n2 {
		arr = append(arr, right[j])
		j++
	}
	return arr
}

// QuickSort 基础快速排序。
func QuickSort(nums []int, left, right int) {
	if left >= right {
		return
	}

	pivot := partition(nums, left, right)
	QuickSort(nums, left, pivot-1)
	QuickSort(nums, pivot+1, right)
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

func swap(nums []int, left, right int) {
	nums[left], nums[right] = nums[right], nums[left]
}

// RandomizedQuickSort 随机化快速排序。
func RandomizedQuickSort(nums []int, left, right int) {
	if left >= right {
		return
	}

	pivot := randomizedPartition(nums, left, right)
	RandomizedQuickSort(nums, left, pivot-1)
	RandomizedQuickSort(nums, pivot+1, right)
}

func randomizedPartition(nums []int, left, right int) int {
	// 区间范围内随机选择一个基准值下标。
	randomIdx := rand.Intn(right-left) + left
	// 将基准值先放到区间最右边。
	swap(nums, right, randomIdx)

	// i 指向小于基准值的元素。
	i := left - 1
	// 遍历区间 [left, right)。
	for j := left; j < right; j++ {
		// j 遇到大于等于基准值的元素时，直接右移。

		// j 遇到小于基准值的元素时，将其与 i 指向元素后面的元素交换。
		// 因为 i + 1 指向的是大于等于基准值的元素。
		if nums[j] < nums[right] {
			i++
			swap(nums, i, j)
		}
	}

	// i 此时指向最后一个小于基准值的元素，i + 1 指向第一个大于等于基准值的元素。
	i++
	// 将一开始放到区间最右边的基准值与 i 交换。
	// 交换后 i 指向基准值，i 前面的元素都比基准值小，i 后面的元素都大于等于基准值。
	swap(nums, i, right)
	return i
}

var tests = []struct {
	nums []int
	want []int
}{
	{nums: []int{1}, want: []int{1}},
	{nums: []int{5, 2, 3, 1}, want: []int{1, 2, 3, 5}},
	{nums: []int{1, 2, 3, 4, 5}, want: []int{1, 2, 3, 4, 5}},
	{nums: []int{5, 1, 1, 2, 0, 0}, want: []int{0, 0, 1, 1, 2, 5}},
	{nums: []int{-4, 0, 7, 4, 9, -5, -1, 0, -7, -1}, want: []int{-7, -5, -4, -1, -1, 0, 0, 4, 7, 9}},
}

func TestBubbleSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		BubbleSort(tc.nums)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("BubbleSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestSelectionSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		SelectionSort(tc.nums)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("SelectionSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestInsertionSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		InsertionSort(tc.nums)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("InsertionSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestQuickSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		QuickSort(tc.nums, 0, len(tc.nums)-1)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("QuickSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestRandomizedQuickSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		RandomizedQuickSort(tc.nums, 0, len(tc.nums)-1)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("RandomizedQuickSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestShellSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		ShellSort(tc.nums)
		if !utils.CompareSlice(tc.nums, tc.want) {
			t.Fatalf("ShellSort(%+v) return %+v != %+v", tc.nums, tc.nums, tc.want)
		}
	}
}

func TestMergeSort(t *testing.T) {
	for i := range tests {
		tc := tests[i]
		output := MergeSort(tc.nums)
		if !utils.CompareSlice(output, tc.want) {
			t.Fatalf("MergeSort(%+v) return %+v != %+v", tc.nums, output, tc.want)
		}
	}
}
