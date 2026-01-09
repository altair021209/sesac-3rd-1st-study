# 게임 개발하기
: 건물을 짓는 데에 순서가 필요하고, 여러개의 건물을 동시에 지을 수 있습니다
N개의 건물을 짓는 데에 필요한 최소시간을 구합니다.


# 건물 짓기 (위상 정렬 + DP) 구현

```python
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input()) # 건물 개수
ans = [0] * (N+1) # 최종 정답 리스트(각 건물 짓는 총 필요 시간)
cost = [0] * (N+1) # 각 건물 짓는 순수시간
degree = [0] * (N+1) # 진입차수 리스트
Q = deque()

graph = defaultdict(list) 

# 입력 처리 및 그래프 구성
for i in range(1, N+1):
    temp = list(map(int, input().split())) # [시간, 선행1, 선행2, ..., -1]
    cost[i] = temp[0]
    
    # temp[1:-1] : 마지막 -1을 제외한 선행 건물들
    for ele in temp[1:-1]:
        graph[ele].append(i) # 선행 건물(ele) -> 현재 건물(i) 방향으로 연결
        degree[i] += 1 

# 초기 큐 세팅 (선행 조건 없는 건물)
for i in range(1, N+1):
    if degree[i] == 0:
        Q.append(i)
        ans[i] = cost[i] # 선행 건물이 없으면 자신의 비용이 곧 정답

# 위상 정렬 수행
while Q:
    now = Q.popleft()
    
    for e in graph[now]:
        degree[e] -= 1
        # [핵심 로직] 
        # 이전 건물들 중 가장 오래 걸린 시간(ans[now]) + 내 건설 시간(cost[e])
        # 기존에 계산된 값과 비교하여 최대값(Max)으로 갱신 (병렬 작업 고려)
        ans[e] = max(ans[e], cost[e] + ans[now])
        
        if degree[e] == 0:
            Q.append(e)

print(*ans[1:], sep='\n')
```


# 유의사항


1. ​위상 정렬과 DP(다이나믹 프로그래밍)의 결합
​단순히 작업의 '순서'만 정하는 것이 아니라, 작업에 걸리는 '누적 시간'을 계산해야 합니다.
​ans[e] = max(ans[e], cost[e] + ans[now]) 부분이 핵심입니다. 선행 건물이 여러 개일 경우, 그중 가장 늦게 끝나는 건물이 완성되어야 현재 건물을 지을 수 있기 때문에 max 함수를 사용하여 메모이제이션을 수행합니다.

2. ​입력 데이터의 역방향 그래프 모델링
​문제의 입력은 [현재 건물 비용, 선행 A, 선행 B ...] 형태로 "나를 짓기 위해 필요한 것"을 줍니다.
​하지만 위상 정렬을 수행하기 위해서는 "내가 완료되면 지을 수 있는 다음 건물"을 알아야 하므로, graph[ele].append(i)와 같이 방향을 뒤집어서 인접 리스트를 구성하는 것이 구현의 포인트입니다.

3. ​동시성(Concurrency) 처리
​이 문제는 여러 건물을 동시에 지을 수 있다는 가정이 깔려 있습니다.
​만약 순차적으로만 지을 수 있다면 모든 시간을 더해야겠지만, 동시 진행이 가능하므로 **병목 지점(Critical Path, 가장 오래 걸리는 경로)**이 전체 완료 시간을 결정한다는 점을 코드로 구현한 것입니다.
