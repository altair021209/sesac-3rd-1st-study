
5-3 삽입 정렬
이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치에 삽입시켜 정렬하는 방식.
시간 복잡도는 O(n^2)로 느린 편이지만 구현하기 쉽다.

*핵심 이론
선택 데이터를 현재 정렬된 데이터 범위 내에서 적절한 위치에 삽입하는 것.
-수행 방식:
    1.현재 index에 있는 데이터 값을 선택한다.
    2.현재 선택한 데이터가 정렬된 데이터 범위에 삽입될 위치를 탐색한다.
    3.삽입 위치부터 index에 있는 위치까지 shift 연산을 수행한다.
    4.삽입 위치에 현재 선택한 데이터를 삽입하고 index++연산을 수행한다.
    5.전체 데이터의 크기만큼 index가 커질 때까지, 즉 선택한 데이터가 없을 때까지 반복한다.

*문제 요약
여러 사람이 ATM에서 돈을 인출하는 데 필요한 시간이 각각 주어질 때,
전체 대기 시간의 총합이 최소가 되도록 사람들의 순서를 정하는 문제

*핵심 아이디어
기다리는 시간이 가장 짧은 사람부터 ATM을 사용하게 해야 전체 합이 최소가 됨.
즉, 주어진 시간들을 오름차순으로 정렬한 후,
각 사람의 대기 시간 누적합을 모두 더한 값이 최소 총 대기 시간.


*코드 구현
import sys
input = sys.stdin.readline

N = int(input())  # 사람수
A = list(map(int, input().split()))  # 각 사람의 인출 시간을 저장한 리스트
S = [0] * N  # 각 사람이 돈을 인출하는데 걸리는 시간의 합을 저장할 리스트

for i in range(N):
    insert_point = i
    insert_value = A[i]
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j - 1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)
