package leetcode

/*
N 皇后

链接：https://leetcode-cn.com/problems/n-queens

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

解法：
1. 回溯。

时间复杂度：O(N!)
空间复杂度：O(N)。
空间复杂度主要取决于递归调用层数、记录每行放置的皇后的列下标的数组以及三个集合，
递归调用层数不会超过 N，数组的长度为 N，每个集合的元素个数都不会超过 N。
*/

import (
	"strings"
	"testing"
)

func solveNQueens(n int) [][]string {
	// 初始化 n * n 的棋盘。
	board := make([][]rune, n)
	for i := range board {
		board[i] = make([]rune, n)
		for j := range board[i] {
			board[i][j] = '.'
		}
	}

	// 初始化答案。
	ans := make([][]string, 0)

	// 按行回溯。
	backtract(board, 0, &ans)
	return ans
}

func backtract(board [][]rune, row int, ans *[][]string) {
	// 回溯终止条件，遍历过了最后一行。
	if row == len(board) {
		// 记录答案。
		var tmp []string
		for i := range board {
			builder := strings.Builder{}
			for j := range board[i] {
				builder.WriteRune(board[i][j])
			}
			tmp = append(tmp, builder.String())
		}
		*ans = append(*ans, tmp)
		return
	}

	// 选择每一列。
	for col := range board[row] {
		// 跳过不合法的位置。
		if !isValid(board, row, col) {
			continue
		}

		// 选择列。
		board[row][col] = 'Q'
		// 递归下一行。
		backtract(board, row+1, ans)
		// 撤销选择的列。
		board[row][col] = '.'
	}
}

func isValid(board [][]rune, row int, col int) bool {
	// 列是否合法。
	for i := range board[row] {
		if board[i][col] == 'Q' {
			return false
		}
	}

	// 右上方是否合法。
	for r, c := row-1, col+1; r >= 0 && c < len(board[row]); r, c = r-1, c+1 {
		if board[r][c] == 'Q' {
			return false
		}
	}

	// 左上方是否合法。
	for r, c := row-1, col-1; r >= 0 && c >= 0; r, c = r-1, c-1 {
		if board[r][c] == 'Q' {
			return false
		}
	}

	return true
}

func compareDoubleSlice(a, b [][]string) bool {
	if len(a) != len(b) {
		return false
	}

	if a == nil || b == nil {
		return false
	}

	for i := range a {
		if len(a[i]) != len(b[i]) {
			return false
		}

		if a[i] == nil || b[i] == nil {
			return false
		}

		for j := range a[i] {
			if a[i][j] != b[i][j] {
				return false
			}
		}
	}

	return true
}

func TestSolveNQueens(t *testing.T) {
	testCases := []struct {
		n    int
		want [][]string
	}{
		{n: 4, want: [][]string{{".Q..", "...Q", "Q...", "..Q."}, {"..Q.", "Q...", "...Q", ".Q.."}}},
		{n: 1, want: [][]string{{"Q"}}},
	}
	for _, tc := range testCases {
		output := solveNQueens(tc.n)
		if !compareDoubleSlice(output, tc.want) {
			t.Errorf("solveNQueens(%v) return: %+v != %+v\n", tc.n, output, tc.want)
		}
	}
}
