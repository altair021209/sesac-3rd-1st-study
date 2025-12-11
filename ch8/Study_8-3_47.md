*문제 47번
![alt text](image-5.png)

->비율을 이용해 모든 재료의 최소 정수량을 구하는 문제

*문제 분석: n-1개의 비율로 n개의 재료의 전체 비율을 알아낼 수 있다. 그래프 관점에서 생각하면 사이클이 없는 트리 구조로 이해할 수 있다.
임의의 노드에서 DFS(Depth-First Search)를 진행. 그 과정에서 유클리드 호제법을 사용하여 최소 공배수, 최대 공약수를 구하게 된다.



![alt text](image-6.png)

*그래프
```python
      (1:1)
   0 -------\
             \
(3:1)         \
1 ------------ 4 ------------ 2
               (5:1)
               |
               |
               3
               (7:1)
```


*코드 구현
```python
N = int(input())             # N개의 재료
A = [[] for _ in range(N)]   # 그래프 저장할 이중 리스트
visited = [False] * (N)      # 탐색여부
D = [0] * (N)                # 각 재료의 비율에 따른 양 저장
lcm = 1

def gcd(a, b):              # 최대공약수
    if b == 0:
        return a
    else: 
        return gcd(b, a % b)

for i in range(N - 1):       # 그래프를 이중리스트에 저장
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm = lcm * (p * q // gcd(p, q))        #최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것

D[0] = lcm
        

def DFS(v):                 #DFS 탐색 함수 구현
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)


DFS(0)              # DFS(0)->DFS(4)->(for문 :노드0 패스, 노드1->DFS(1), 노드2->DFS(2),노드3->DFS(3))
mgcd = D[0]

for i in range(1, N):
    mgcd = gcd(mgcd, D[i])  

for i in range(N)::
    print(int(D[i] // mgcd), end=' ')  

```

* 그래프가 저장되는 모양
```python
A[0] = [(4,1,1)]
A[1] = [(4,3,1)]
A[2] = [(4,5,1)]
A[3] = [(4,7,1)]
A[4] = [(0,1,1), (1,3,1), (2,5,1), (3,7,1)]
```