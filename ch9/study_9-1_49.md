# 문제 정의

1번부터 N번까지의 도시와 M개의 단방향 도로가 존재함.
모든 거리는 1임
도시 X에서 출발해서 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시 번호 출력

# 코드
``` python

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # 노드의 수, 엣지의 수, 목표 거리, 시작점
A = [[] for _ in range(N + 1)] # 인접 리스트 생성
answer = [] # 최단 거리가 K인 노드 담을 리스트
visited = [-1] * (N + 1) # -1이면 아직 방문 안함,

def BFS(v):  # BFS 탐색 함수 구현
    queue = deque()
    queue.append(v)
    visited[v] += 1 # 시작 노드인 v가 -1 에서 0이됨
    while queue: 
        now_Node = queue.popleft()
        for i in A[now_Node]: # A는 인접 리스트, now_Node에서 한 번에 갈                                   수 있는 이웃 노드들이 들어있음
            if visited[i] == -1: # i노드를 한번도 방문한적 없을 때
                visited[i] = visited[now_Node] + 1
                # i노드에 이전 노드의 visited에서 1을 더함
                queue.append(i) # 새로 방문한 i를 큐에 넣음, 반복문 진행중                                   i를 꺼내서 i도 BFS 수행

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E) # s에서 E로 가는 간선 추가

BFS(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i) # 시작점 x에서 i까지 최단거리가 k이면 정답에 추가

if not answer:
    print(-1) # 정답 없으면 -1 출력
else:
    answer.sort()  # 오름차순으로 정렬 
    for i in answer:
        print(i)


```
