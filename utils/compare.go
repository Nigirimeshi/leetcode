package utils

func CompareSlice(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	if a == nil || b == nil {
		return false
	}

	for i, v := range a {
		if b[i] != v {
			return false
		}
	}
	return true
}

func CompareDoubleSlice(a, b [][]string) bool {
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
