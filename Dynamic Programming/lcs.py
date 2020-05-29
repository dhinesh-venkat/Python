def lcs(a,b):
	x = len(a) + 1
	y = len(b) + 1

	dp = [[0 for j in range(y)]for i in range(x)]

	for row in range(1,x):
		for col in range(1,y):
			if a[row-1] == b[col-1]:
				dp[row][col] = dp[row-1][col-1] + 1
			else:
				dp[row][col] = max(dp[row-1][col],dp[row][col-1])

	print("The length of Longest Common Subsequence is : {}".format(dp[x-1][y-1]))

	index = dp[x-1][y-1]
	i = x - 1
	j = y - 1
	ans = ""
	while i>0 and j>0:
		if a[i-1] == b[j-1]:
			ans += a[i-1]
			i -= 1
			j -= 1
		elif dp[i-1][j]>dp[i][j-1]:
			i -= 1
		else:
			j -= 1
	print("The Longest Common Subsequence is : {}".format(ans[::-1]))
	
def main():
	try:
		while True:		
			a = input()
			b = input()
			lcs(a,b)
	except:
		pass

if __name__ == '__main__':
	main()