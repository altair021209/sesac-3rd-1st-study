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

## 유의사항

1. 진입 차수(Indegree)의 갱신 로직

큐에서 노드를 꺼낼 때마다, 그 노드와 연결된 후행 노드들의 진입 차수를 반드시 -1 해줘야 합니다. 이는 물리적으로 '화살표(간선)를 끊어내는 행위'와 같습니다.

2. 큐(Queue)에 들어가는 조건

아무 노드나 큐에 넣는 것이 아니라, 오직 indegree == 0이 된 순간에만 넣어야 합니다. 이는 '이전 작업이 모두 끝난 작업만 수행할 수 있다'는 위상 정렬의 핵심 원리입니다
