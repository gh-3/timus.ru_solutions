import sys
import math

lines = sys.stdin.readlines()
squere_root = [math.sqrt(float(number))
               for line in lines
               for number in line.split()]

squere_root.reverse()

for x in squere_root:
    print(x)
