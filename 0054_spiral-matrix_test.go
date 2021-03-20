package leetcode

import (
	"testing"

	"leetcode/utils"
)

/*
螺旋矩阵

链接：https://leetcode-cn.com/problems/spiral-matrix

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

*/
func spiralOrder(matrix [][]int) []int {
	// m 是行数，n 是列数。
	m, n := len(matrix), len(matrix[0])

	// 初始化坐标。
	left, right, top, button := 0, n-1, 0, m-1

	// 存放结果列表。
	ans := make([]int, 0, m*n)

	for {
		// 从左向右。
		for j := left; j <= right; j++ {
			ans = append(ans, matrix[top][j])
		}
		top++
		if top > button {
			break
		}

		// 从上向下。
		for i := top; i <= button; i++ {
			ans = append(ans, matrix[i][right])
		}
		right--
		if right < left {
			break
		}

		// 从右向左。
		for j := right; j >= left; j-- {
			ans = append(ans, matrix[button][j])
		}
		button--
		if button < top {
			break
		}

		// 从下向上。
		for i := button; i >= top; i-- {
			ans = append(ans, matrix[i][left])
		}
		left++
		if left > right {
			break
		}
	}
	return ans
}

func TestSpiralOrder(t *testing.T) {
	testCases := []struct {
		matrix [][]int
		want   []int
	}{
		{
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			want: []int{1, 2, 3, 6, 9, 8, 7, 4, 5}},
		{matrix: [][]int{
			{1, 2, 3, 4},
			{5, 6, 7, 8},
			{9, 10, 11, 12},
		},
			want: []int{1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7}},
	}
	for _, tc := range testCases {
		output := spiralOrder(tc.matrix)
		if !utils.CompareSlice(output, tc.want) {
			t.Errorf("spiralOrder(%+v) return: %+v != %+v", tc.matrix, output, tc.want)
		}
	}
}
