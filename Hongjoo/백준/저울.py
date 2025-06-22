"""
https://www.acmicpc.net/problem/2437

# 문제
- 저울 N개의 조합의 합으로 구현할 수 없는 양의 최소값 구하기
- N<=1000개
- 1개 무게 >= 1,000,0000
유형 : dp 인줄 알았지만 greedy 라는데 
-최소값 


N개 의 무게추 중 
"""
#1. 입력 저울추 & 오름차순 정렬
N = int(input())
weights = sorted(list(map(int, input().split())))
target = 1 
for w in weights : 
  if target < w :
    break
  
  target += w
print(target)
