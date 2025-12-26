
#문제 정의 
A가 B를 신뢰할 경우  B를 해킹하면 A도 해킹 가능


#입력 형태
3 1 이라 하면 3이 1을 신뢰하는 것, 즉 1을 해킹하면 3도 해킹 가능

# 문제 해석
모든 노드 각각을 BFS 탐색 알고리즘 수행해서 탐색되는 노드들의 신뢰도를 증가해줌

코드 구현
``` python

import sys  
from collections import deque
input = sys.stdin.readline  

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

def BFS(v):
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1   # 신규 노드 인덱스의 정답 리스트값을 증가
                queue.append(i)

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N + 1):   # 모든 노드에서 BFS 실행
    BFS(i)

maxVal = max(answer)
for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ')


```
