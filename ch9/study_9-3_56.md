# 줄세우기
: N명의 학생들 중 일부 학생들의 키를 둘씩 비교한 결과로만 줄을 세웁니다


# 위상 정렬 (Topological Sort) 구현 코드

```python
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[] for i in range(N+1)]
indegree = [0] * (N+1) # 각 노드의 진입 차수(선행 조건 수)를 저장할 리스트

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)     # S -> E로 가는 방향 그래프 연결
    indegree[E] += 1   # E로 들어오는 간선(진입 차수) 개수 증가

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0: # 선행 조건이 없어 바로 시작 가능한 노드 탐색
        queue.append(i)

while queue:
    now = queue.popleft() # 처리할 노드를 큐에서 꺼냄
    print(now, end=' ')
    
    for next in A[now]:
        indegree[next] -= 1  # 연결된 노드의 진입 차수 1 감소 (조건 해제)
        if indegree[next] == 0: # 모든 선행 조건이 해결되었다면
            queue.append(next)  # 큐에 넣어 방문 대기열에 추가
```


