
# 문제 정의

A,B,C의 물통이 있다
A,B물통은 비어 있고 ,C의 물통이 가득 차 있다.
하나의 물통은 비거나 가득 차야한다.
A물퐁이 비어 있을때 C물통에 담겨 있을 수 있는 물의 양은? 

```python


from collections import deque


Sender = [0, 0, 1, 1, 2, 2]
Receiver = [1, 2, 0, 2, 0, 1]
# 물 이동 경우의 수를 6가지로 표현 

now = list(map(int, input().split()))
# A,B,C 물통의 최대 용량 입력 

visited = [[False for j in range(201)] for i in range(201)]
# A,B의 물의양 상태 방문 체크용

answer = [False] * 201
# A가 0일때 가능한 C의 물의 양 기록 

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True # 초기 C의 물의 양을 정답으로 기록

    while queue:
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B  # C는 전체 물의 양에서 A와 B를 뺀 것

        for k in range(6):  # A → B, A → C, B → A, B → C, C → A, C → B
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]]
            next[Sender[k]] = 0

            if next[Receiver[k]] > now[Receiver[k]]:  # 물이 넘칠 때
                # 초과하는 만큼 다시 이전 물통에 넣어 주기
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]] = now[Receiver[k]]  # 대상 물통 최대치로 채우기

            if not visited[next[0]][next[1]]:  # A와 B의 물의 양으로 방문 리스트 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))

                if next[0] == 0:  # A의 물의 양이 0일 때 C의 물의 양을 정답 변수에 저장
                    answer[next[2]] = True


BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')

'''
