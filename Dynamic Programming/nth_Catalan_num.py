def catalan(n):
	if n == 0:
		return 1
	catalan = [0] * (n+1)

	catalan[0] = 1
	catalan[1] = 1

	for i in range(2,n+1):
		for j in range(i):
			catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

	return catalan[-1]


def main():
	try:
		while True:
			n = int(input())
			print(catalan(n))
	except:
		pass

if __name__ == '__main__':
	main()