n = int(input())
output = 0
if n >= 1:
    output = int(n * (n + 1) / 2)

if n == 0:
    output = 1

elif n < -1:
    output = int(n * (n - 1) / 2) * -1 + 1

print(output)
