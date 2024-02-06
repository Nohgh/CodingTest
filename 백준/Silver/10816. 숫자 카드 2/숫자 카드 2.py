'''
이분 탐색을 하는데 원소의 유무만 판단하는 것이 아니라 몇개의 원소가 리스트에
있는지를 구하는 문제
'''
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr1=list(map(int,input().split()))
# arr1.sort()
# arr1=deque(arr1)
m=int(input())
arr2=list(map(int,input().split()))

hash={}
for x in arr1:
    if x in hash:
        hash[x]+=1
    else:
        hash[x]=1
for x in arr2:
    if x in hash:
        print(hash[x],end=' ')
    else:
        print(0,end=' ')
