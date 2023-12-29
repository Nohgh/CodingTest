import sys

input = sys.stdin.readline
x = int(input())
st = []
sum = 0
for _ in range(x):
  n = int(input())
  if (n == 0 and len(st) > 0):
    st.pop()
  else:
    st.append(n)
for x in st:
  sum += x
print(sum)
