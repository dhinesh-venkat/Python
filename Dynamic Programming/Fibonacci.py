fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        value = 1

    elif n>2:
        value = fib(n-1) + fib(n-2)
    fib_cache[n] = value

    return value

def main():
	try:
		while True:
			n = int(input())
			print(fib(n))
	except:
		pass
		
if __name__ == '__main__':
	main()
