def lis(arr):
	n = len(arr)
	dp = [1] * n
	for i in range(1,n):
		for j in range(i):
			if arr[i]>arr[j] and dp[i]<dp[j]+1:
				dp[i] = dp[j] +1
	print(max(dp))

def main():
	try:
		while True:
			arr = list(map(int,input().split()))
			lis(arr)
	except:
		pass
if __name__ =='__main__':
	main()