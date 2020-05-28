def get_ugly(n):
	dp = [0] * n
	dp[0] = 1
	circle = square = triangle = 0
	next_2 = 2
	next_3 = 3
	next_5 = 5
	for i in range(1,n):
		dp[i] = min(next_2,next_3,next_5)
		if dp[i] == next_2:
			circle += 1
			next_2 = dp[circle] * 2
		if dp[i] == next_3:
			square += 1
			next_3 = dp[square] * 3
		if dp[i] == next_5:
			triangle += 1
			next_5 = dp[triangle] * 5
		#print(circle,square,triangle)
	return dp[-1]

if __name__ == '__main__':
	try:
		while True:
			print(get_ugly(int(input())))
	except:
		pass
