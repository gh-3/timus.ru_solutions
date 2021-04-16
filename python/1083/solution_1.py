def factorial(n, k):
    fact = 1
    coefficient = 0
    compare = n % k
    if not compare:
        compare = k

    while(True):
        v = n - (coefficient * k)
        if v >= compare:
            fact = fact * v
            coefficient += 1
        else:
            return fact


n, second = input().split()
n = int(n)
k = len(second)
print(factorial(n, k))
