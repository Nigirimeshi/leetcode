package leetcode

import (
	"testing"
)

/*
正则表达式匹配

链接：https://leetcode-cn.com/problems/regular-expression-matching

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串 s 的，而不是部分字符串。

示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。
因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false

提示：
0 <= s.length <= 20
0 <= p.length <= 30
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符

解法：
1. 动态规划。
基本思想：
 - 从 s[:1] 和 p[:1] 是否匹配开始判断，每次添加一个字符并判断是否匹配，直到添加完整个字符串 s 和 p。
 - 假设 s[:i] 和 p[:j] 可以匹配，那么下一次就需要判断 2 种状态：
   1. 添加 1 个字符 s(i+1) 后能否匹配？
   2. 添加 1 个字符 p(i+1) 后能否匹配？
 - 因此，共有 m * n 种状态。
 - 此外，需要根据 “普通字符”，“.”，“*” 做出不同的状态转移。

状态：dp[i][j] 代表 s 的前 i 个字符串和 p 的前 j 的字符串能否匹配。

状态转移：
 - 注意：dp[0][0] 是空字符串，为 True；另外 dp[i][j] 对应添加的字符是 s[i-1] 和 p[j-1]。
 - 当 p[j-1] = '*' 时，以下任一条件成立时，dp[i][j] 为 True：
    - 当 dp[i][j-2] = True 时：即把 “p[j-2]*” 看作出现 0 次时，能否匹配。
    - 当 dp[i-1][j] = True 且 s[i-1] = p[j-2] 时：即让 p[j-2] 多出现 1 次时，能否匹配。
    - 当 dp[i-1][j] = True 且 p[j-2] = '.' 时：即让 '.' 多出现 1 次时，能否匹配。
 - 当 p[j-1] != '*' 时，以下任一条件成立时，dp[i][j] 为 True：
    - 当 dp[i-1][j-1] = True 且 s[i-1] = p[j-1] 时：即之前的字符都匹配，当前的字符相同。
    - 当 dp[i-1][j-1] = True 且 p[j-1] = '.' 时：即之前的字符都匹配，当前的 “.” 可匹配任一字符。

初始值：需要初始化首行。
 - dp[0][0] = True，即 2 个空字符串能够匹配。
 - 当 dp[0][j-2] = True 且 p[j-1] = '*' 时，dp[0][j] = True，相当于 p 的奇数位下标一直是 '*'，p 可以一直当作一个空字符串。

返回值：dp 矩阵右下角的值，代表 s 和 p 能否匹配。
*/

func isMatch(s string, p string) bool {
	sLen, pLen := len(s)+1, len(p)+1

	// dp 表示字符结尾到 s[i-1] 和 p[j-1] 时，s 和 p 是否匹配。
	var dp = make([][]bool, sLen)
	for i := 0; i < sLen; i++ {
		dp[i] = make([]bool, pLen)
	}

	// base case.
	// 2 个空字符串能够匹配。
	dp[0][0] = true
	// p 的奇数位下标为 '*' 时，可以当作空字符串匹配。
	for j := 2; j < pLen; j += 2 {
		dp[0][j] = dp[0][j-2] && p[j-1] == '*'
	}

	for i := 1; i < sLen; i++ {
		for j := 1; j < pLen; j++ {
			// 当 p[j-1] = '*' 时。
			if p[j-1] == '*' {
				// 可以将 p[j-2]* 看作空字符。
				// 例如：s = 'ab', p = 'ac*'
				if dp[i][j-2] {
					dp[i][j] = true
					continue
				}

				// 例如：s = 'aa', p = 'a*'
				if dp[i-1][j] && s[i-1] == p[j-2] {
					dp[i][j] = true
					continue
				}

				// 例如：s = 'ab', p = 'a.*'
				if dp[i-1][j] && p[j-2] == '.' {
					dp[i][j] = true
					continue
				}

			} else { // 当 p[j-1] != '*' 时。

				// 之前的字符串都匹配，且当前字符相同。
				if dp[i-1][j-1] && s[i-1] == p[j-1] {
					dp[i][j] = true
					continue
				}

				// 之前的字符串都匹配，且当前的 p 是 '.'。
				if dp[i-1][j-1] && p[j-1] == '.' {
					dp[i][j] = true
					continue
				}
			}
		}
	}

	return dp[sLen-1][pLen-1]
}

func TestIsMatch(t *testing.T) {
	testCases := []struct {
		s, p string
		want bool
	}{
		{s: "aa", p: "a", want: false},
		{s: "aa", p: "a*", want: true},
		{s: "ab", p: ".*", want: true},
		{s: "aab", p: "c*a*b", want: true},
		{s: "mississippi", p: "mis*is*p*.", want: false},
	}
	for _, tc := range testCases {
		output := isMatch(tc.s, tc.p)
		if output != tc.want {
			t.Errorf("isMatch(%v, %v) return: %+v != %+v\n", tc.s, tc.p, output, tc.want)
		}
	}
}
