import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
# print()
rst=((v-a)/(a-b))+1
print(math.ceil(rst))