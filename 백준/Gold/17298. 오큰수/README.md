# [Gold IV] 오큰수 - 17298 

[문제 링크](https://www.acmicpc.net/problem/17298) 

### 성능 요약

메모리: 155536 KB, 시간: 1084 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 1월 13일 23:07:00

### 문제 설명

<p>크기가 N인 수열 A = A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 있다. 수열의 각 원소 A<sub>i</sub>에 대해서 오큰수 NGE(i)를 구하려고 한다. A<sub>i</sub>의 오큰수는 오른쪽에 있으면서 A<sub>i</sub>보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.</p>

<p>예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.</p>

### 입력 

 <p>첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub> (1 ≤ A<sub>i</sub> ≤ 1,000,000)이 주어진다.</p>

### 출력 

 <p>총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.</p>

### O(N**2)코드
```python
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))

s=[]
rst=[]
sysout=[]
for x in range(len(a)):
    rst.append(a[x])
    for z in range(x+1,len(a)):
        if a[x] <= a[z]:
            rst.append(a[z])
    
    if(len(rst)==1):
        sysout.append(-1)
    else:
        while(len(rst)!=2):
            rst.pop()
        sysout.append(rst.pop())
    rst.clear()
print(sysout)
'''데이터 100만, 1초 o(n)으로 풀어야함 '''

```


### O(N)코드
- 해결방법: for문으로 순회를 하며 x를 인덱스로 만들고 인덱스를 저장할 스택을 하나 생성
- 스택 내의 인덱스는 전 인덱스라고 생각하면 되고 a[x]가 현재 인덱스의 값 따라서 a[stack[-1]과 a[x]를 비교
- 스택에서 pop한 원소인 인덱스를 다음 값으로 주면 오큰수를 계산할 수 있음
### 포인트: 순회를 for문을 이용해 높은 시간복잡도를 스택을 이용하여 한번의 순회로 모든값을 비교할 수 있다.
