# 문제 정의
이분 그래프란?
: 각 집합에 속한 노드끼리 서로 인접하지 않는 두 집합으로 그래프의 노드를 나눌 수 있을 때 (같은 그룹 내부에는 간선이 절대 없음)

# 문제 해석


# 코드 구현
``` python

import sys
sys.setrecursionlimit(10**6) # 깊은 DFS탐색 수행하기 위해 
input = sys.stdin.readline

N = int(input())
# 테스트 케이스, 쓰는 이유? 한 번의 코드로 여러 상황을 동시에 검증위해 

IsEven = True  # 현재 그래프가 이분 그래프인지 여부를 저장 

def DFS(node):
    global IsEven
    # 전역 변수로 선언, 왜? DFS함수 밖의 IsEven값을 바꾸기 위해 
    visited[node] = True # 현재 노드를 방문 처리 
    for i in A[node]: # 현재 노드와 연결된 모든 인접 노드를 하나씩 확인
        if not visited[i]:
            check[i] = (check[node] + 1) % 2
            # 인접 노드는 반드시 다른 그룹에 속해야됨 
            DFS(i)
        
        elif check[node] == check[i]:
            IsEven = False
            # 인접 노드가 같은 그룹에 속하면 False 

for _ in range(N):
    V, E = map(int, input().split()) # V: 노드 수 , E : 간선 수 
    A = [[] for _ in range(V + 1)] # 노드 번호가 1번부터 시작이니까 V+1 
    visited = [False] * (V + 1) # 각 노드 방문 여부 저장
    check = [0] * (V + 1)
    IsEven = True

    for i in range(E): # 간선 개수만큼 반복 
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start) # 무방향 그래프 

 
    for i in range(1, V + 1):
        if IsEven:
            if not visited[i]:
                DFS(i)
        else:
            break

    if IsEven:
        print("YES") # 모든 조건 만족시 
    else:
        print("NO") # 하나라도 위반시




```
