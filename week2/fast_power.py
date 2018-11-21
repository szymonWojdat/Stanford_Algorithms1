# jak to dziala????


def fast_power(a, b):
	if b == 1:
		return a
	else:
		c = a * a
		ans = fast_power(c, b//2)
		if not b % 2 == 0:
			return a * ans
		else:
			return ans


print(fast_power(3, 5))
