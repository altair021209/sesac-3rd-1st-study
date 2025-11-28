#구간 합 구하기 1


*문제: 수 N개가 주어졌을 때, i번째수에서 j 번째 수까지의 합을 구하는 프로그램을 작성

*핵심 아이디어: 해당 수들의 합 배열을 구하고, 이를 이용해서 구간의 합을 구한다

*코드

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split))
prefix_list = [0]

for i in range(1, N+1):
    prefix_list[i] = prefix_list[i-1] + numbers[i]

for i in range(M):
    num1, num2 = map(int, input())
    print(prefix_list[num2] - prefix_list[num1-1])

```