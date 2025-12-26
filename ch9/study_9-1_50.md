
# 문제 정의 
A가 B를 신뢰할 경우  B를 해킹하면 A도 해킹 가능


# 입력 형태
(코드 기준) 3 1 이라 하면, 즉 3을 해킹하면 1도 해킹 가능

# 문제 해석
모든 노드 각각을 BFS 탐색 알고리즘 수행해서 탐색되는 노드들의 신뢰도를 증가해줌



# 코드 구현
``` python

import sys  
from collections import deque
input = sys.stdin.readline  

N, M = map(int, input().split()) # N은 노드 개수, M은 간선 개수
A = [[] for _ in range(N + 1)]
# 인접 리스트 방식의 그래프, 노드 번호가 1부터 시작이니 N+1 사용

answer = [0] * (N + 1)
# 각 노드가 몇 번 해킹되는지 누적 카운트 위해 사용 

def BFS(v):
    visited = [False] * (N + 1)  # 각 노드의 방문리스트 만들어줌 
    queue = deque()
    queue.append(v)  # 시작 노드를 큐에 삽입 
    visited[v] = True  # 시작 노드 방문 처리 
    while queue: # 큐에 값이 있으면 True니까 큐가 없을 때까지 반복
        now_Node = queue.popleft() # 현재 탐색중인 노드 추출
        for i in A[now_Node]: # 현재 노드에서 갈 수 있는 모든 노드 탐색
            if not visited[i]: # 아직 방문하지 않은 노드 가 있다면 조건문 수행
                visited[i] = True 
                answer[i] += 1   # i는 해킹당할 수 있음을 의미 
                queue.append(i)

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E) # A인접 리스트 작성함 , S 를 해킹하면 E도 해킹 가능

for i in range(1, N + 1):   # 모든 노드에서 BFS 실행
    BFS(i)

maxVal = max(answer) # 가장 많이 해킹된 횟수 
for i in range(1, N + 1):   # answer값이 최대인 노드 i를 모두 찾기 
    if maxVal == answer[i]:
        print(i, end=' ')


```
