package leetcode

import (
	"testing"

	"leetcode/utils"
)

/*
找到字符串中所有字母异位词

链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string

定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

解法：
1. 滑动窗口。

*/

func findAnagrams(s string, p string) []int {
	// 滑动窗口。

	need := make(map[rune]int)
	window := make(map[rune]int)

	sRune := []rune(s)
	pRune := []rune(p)

	for _, c := range pRune {
		if _, ok := need[c]; !ok {
			need[c] = 0
		}
		need[c]++
	}

	var ans []int
	left, right := 0, 0
	valid := 0
	for right < len(sRune) {
		c := sRune[right]
		right++
		if _, ok := need[c]; ok {
			if _, ok := window[c]; !ok {
				window[c] = 0
			}
			window[c]++
			if window[c] == need[c] {
				valid++
			}
		}

		for (right - left) >= len(pRune) {
			if valid == len(need) {
				ans = append(ans, left)
			}

			d := sRune[left]
			left++
			if _, ok := need[d]; ok {
				if window[d] == need[d] {
					valid--
				}
				window[d]--
			}
		}
	}

	return ans
}

func TestFindAnagrams(t *testing.T) {
	testCases := []struct {
		s    string
		p    string
		want []int
	}{
		{s: "cbaebabacd", p: "abc", want: []int{0, 6}},
		{s: "abab", p: "ab", want: []int{0, 1, 2}},
	}

	for _, tc := range testCases {
		output := findAnagrams(tc.s, tc.p)
		if !utils.CompareSlice(tc.want, output) {
			t.Errorf("findAnagrams(%v, %v) return: %v != %v\n", tc.s, tc.p, output, tc.want)
		}
	}
}
