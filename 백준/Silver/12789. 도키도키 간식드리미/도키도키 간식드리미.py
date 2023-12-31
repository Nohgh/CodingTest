import sys

input = sys.stdin.readline
rst = 1
next_n = 1
s1 = []
s2 = []
n = int(input())
str = input().strip()
s1 = list(map(int, str.split(" ")))  #중요
if (len(s1) != n):
  print("error")
for x in s1:
  while (1):
    if (len(s2) > 0
        and s2[len(s2) - 1] == next_n):  #대기열에 원소가 있고 마지막 원소가 출력 숫자인경우 팝
      s2.pop()
      next_n += 1
    else:
      break
  if (x == next_n):  #넣을 숫자가 출력 숫자인 경우
    next_n += 1  #출력숫자 올림,push,pop아무 연산도 안하고 다음으로 넘어가면 됨
    continue
  else:  #넣을 숫자가 출력 숫자가 아닌 경우
    #맨위의 if에서 나갈 숫자는 이미 나감
    if (len(s2) > 0 and
        s2[len(s2) - 1] < x):  #근데 넣는 수가 대기줄 마지막 원소보다 큰경우 ->이러면 다음 나갈때 막혀서 못나감
      rst = 0
      break
    else:
      s2.append(x)
if (rst != 0):
  print("Nice")
else:
  print("Sad")
