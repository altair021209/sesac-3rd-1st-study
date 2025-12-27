




``` python

import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6) # 재귀시 깊이 커질 때 에러 방지용

N = int(input())
cnt = 0

cols = [False] * N                  # 열 충돌 체크
diag1 = [False] * (2 * N - 1)        # / 대각선 체크 (row + col)
diag2 = [False] * (2 * N - 1)        # \ 대각선 체크 (row - col + N - 1)

def backtrack(row):   row번째 행에 퀸 놓는 과정
    global cnt  # 함수 내부에서 바깥 변수 cont를 수정하기 위해 global  사용 

    if row == N:  # 종료 조건
        cnt += 1
        return

    for col in range(N):  # 현재 행에 놓을 열 탐
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = True
            backtrack(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = False

backtrack(0)
print(cnt)


```
