*문제
- N개의 수 A₁, A₂, …, Aₙ이 주어진다.
- 연속된 부분 구간의 합이 M으로 나누어떨어지는 (i, j) 쌍의 개수를 구하는 문제.
- 즉,(Aᵢ + Aᵢ₊₁ + ... + Aⱼ) % M == 0 인 경우의 수를 세기.

*핵심 아이디어 (Prefix Sum + Mod Counting)
- 구간 합: S(j) - S(i-1)
- 모듈러 성질:
(S(j) - S(i-1)) % M == 0   ↔   S(j) % M == S(i-1) % M
- 즉, S(j)와 S(i-1)의 나머지가 같으면 구간 합이 M으로 나누어떨어짐.
- 나머지가 0인 prefix sum 개수는 그대로 answer 변수에 더함
- 나머지 빈도수 카운팅:
  - 나머지 r에 대해 S(k) % M == r 인 개수를 세기.
  - 빈도수를 저장할 길이 m인 리스트 생성해서 r에 해당하는 인덱스에 빈도수 누적하기.
  - 빈도수가 f인 나머지 r에 대해, C(f, 2) = (f * (f - 1)) / 2 개의 (i, j) 쌍이 존재
  - answer 변수에 더해준다.

*코드구현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n      # 누적합 배열
C = [0] * m      # 나머지 개수 카운트 배열
S[0] = A[0]
answer = 0

for i in range(1, n):       #합배열
    S[i] = S[i-1] + A[i]

for i in range(n):           
    remainder = S[i] % m     #나머지 계산
    if remainder == 0:       #나머지가 0인 경우 정답에 누적
        answer += 1
    C[remainder] += 1        #나머지 카운팅

for i in range(m):           #나머지 빈도수로 쌍의 개수 계산해서 정답에 누적
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
