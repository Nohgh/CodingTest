import sys
from collections import deque

input = sys.stdin.readline
q = deque()
rst = []
n, k = map(int, input().split())

for x in range(1, n + 1):
    q.append(x)

result_str = "<"

while q:
    for x in range(k - 1):
        q.append(q.popleft())
    result_str += str(q.popleft())
    
    if q:
        result_str += ", "

result_str += ">"
print(result_str)
