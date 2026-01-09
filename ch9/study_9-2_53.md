# 집합 표현하기
- 집합과 원소가 같은 집합에 포함되어있는지 확인하는 연산 수행
- 경로 압축이 필요한 전형적인 union-find 문제

# 코드 :

```python
import sys
input =sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input()).split()
parent = [0] * (N+1)

def find(a):
    if a == parent[a]: # 대표 노드를 찾는 find 연산, index와 value 가 일치하는지 확인합니다
        return a
    else :
         parent[a] = find(parent[a]) #재귀형태로 구현, 경로를 압축합니다
    return parent[a]


def union(a,b): # 대표 노드끼리 합치는 union 연산
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):  #두 원속 ㅏ같은 집합에 속해 있는지 확인합니다
    a = find(a)
    b - find(b)
    if a== b:
        return True
    else:
        return False

for i in range(0, N+1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("yes")
        else:
            print("NO")

```