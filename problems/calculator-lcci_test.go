package problems

import (
	"math"
	"testing"
)

/*
计算器

链接：https://leetcode-cn.com/problems/calculator-lcci

给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。 整数除法仅保留整数部分。

示例 1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

解法：
1. 栈。
算法：
1）遍历字符串：
1.1）遇到空格时，跳过。
1.2）遇到数字时，可能不止一位，需要向后查找，获取完整的数字 a，并入栈。
1.3）遇到运算符号时，查找下一位完整的数字 b，并根据运算符做下列计算：
1.3.1）遇到 + 号，直接将数字 b 入栈。
1.3.2）遇到 - 号，将数字 -b 入栈。
1.3.3）遇到 * 号，弹出栈顶元素 c 并乘上 b，再入栈。
1.3.4）遇到 / 号，弹出栈顶元素 c 并除以 b，只保留整数部分再入栈。
1.4）栈中剩余数字之和就是答案。

*/

func calculate(s string) int {
	stack := []int{}

	runeSlice := []rune(s)
	size := len(runeSlice)
	i := 0
	for i < size {
		c := runeSlice[i]

		// 遇到空格时，跳过。
		if c == ' ' {
			i++
			continue
		}

		// 遇到数字时，向后查找完整的数字，并入栈。
		if '0' <= c && c <= '9' {
			num := 0
			for i < size && '0' <= runeSlice[i] && runeSlice[i] <= '9' {
				num = num*10 + (int(runeSlice[i] - '0'))
				i++
			}
			// 将数字入栈。
			stack = append(stack, num)
			continue
		}

		// 遇到运算符。
		if c == '+' || c == '-' || c == '*' || c == '/' {
			// 记录运算符。
			sign := c

			// 右移一位。
			i = i + 1

			// 跳过空格。
			for i < size && runeSlice[i] == ' ' {
				i++
				continue
			}

			// 获取运算符后的数字。
			num := 0
			for i < size && '0' <= runeSlice[i] && runeSlice[i] <= '9' {
				num = num*10 + (int(runeSlice[i]) - '0')
				i++
			}

			// + 号，将运算符后的数字入栈。
			if sign == '+' {
				stack = append(stack, num)
			} else if sign == '-' { // - 号，将运算符后的数字取反再入栈。
				stack = append(stack, -num)
			} else if sign == '*' { // * 号，取出栈顶数字，乘以 num 后再入栈。
				x := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				stack = append(stack, x*num)
			} else if sign == '/' { // / 号，取出栈顶数字，除以 num 后只保留整数部分，再入栈。
				x := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				stack = append(stack, int(math.Floor(float64(x/num))))
			}
			continue
		}
	}
	// 栈中剩余数字的和即最后结果。
	ans := 0
	for _, v := range stack {
		ans += v
	}
	return ans
}

func TestCalculator(t *testing.T) {
	testCases := []struct {
		s    string
		want int
	}{
		// {s: "3+2*2", want: 7},
		// {s: " 3/2 ", want: 1},
		// {s: " 3+5 / 2 ", want: 5},
		{s: "42", want: 42},
	}
	for _, tc := range testCases {
		output := calculate(tc.s)
		if output != tc.want {
			t.Errorf("calculate(%v) return %+v != %+v", tc.s, output, tc.want)
		}
	}
}
