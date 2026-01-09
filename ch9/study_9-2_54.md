# 여행 계획 짜기
- N개의 도시에 대해서 여행 경로를 짤 떄, 여행 계획이 가능한지 판별하는 프로그램을 작성합니다.
- 이때 도시끼리는 연결되어있지 않을 수도 있습니다.




```python

import sys
input = sys.stdin.readline

# 유니온 파인드

def find(x):
    if graph[x] < 0:
        return x
        
    graph[x] = find(graph[x])
    return graph[x]
    
def union(x, y): #weighted union find
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if graph[x] < graph[y]:
        graph[y] = x
    elif graph[y] < graph[x]:
        graph[x] = y
    else:
        graph[x] = y
        graph[y] -= 1
        
    return

N = int(input())
M = int(input())
graph = [-1]*(N+1)

# 연결 관계가 1인 두 노드의 루트 노드를 합쳐준다.(그래프 합치기)
for start in range(1, N+1):
    for end, isLinked in zip(range(1, N+1), map(int, input().split())):
        if isLinked:
            union(start, end)
   
path = list(set(map(int, input().split())))
result = "YES"
# 방문 경로 내 도시 중, 한 쌍이라도 루트 노드가 서로 다르다면
# 즉, 서로가 한 그래프 내에 존재하지 않는다면 방문 경로는
# 절대로 다 돌 수 없으므로 result = "NO"
# 한 편, len(path)가 1인 경우는 그냥 그 도시만 방문하면되니까
# YES 출력
for i in range(1, len(path)):
    if find(path[0]) != find(path[i]):
        result = "NO"
        break
print(result)

```

## Weighted Union Find 
- 단순하게 union 연산을 할 경우, 노드가 일자로 연결되는 경우가 생길 수 있습니다 : 
이때 가장 마지막 노드가 대표 노드를 찾는 연산에 많은 시간이 걸립니다.

- 이를 해결하기 위해 낮은 트리를 높은 트리 아래 붙인다는 규칙을 추가합니다. 이렇게 하면 트리의 높이가 유지되어 find 연산이 빨라집니다

- value가 양수일때: 자신의 부모 노드 표현
- value가 음수일때: 절대값은 자식노드의 개수

- 그래서 위의 `def union` 부분에선 value가 음수일때 더 큰 쪽(절대값이 낮은 쪽) 을 작은쪽 아래에 넣습니다