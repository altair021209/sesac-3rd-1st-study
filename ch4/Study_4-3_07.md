*문제
재료의 개수 N개
갑옷을 만드는 데 필요한 수 M
각 재료의 고유번호가 주어지고 서로 다른 2개의 재료의 고유번호 합이 M이 되는 경우의 수를 구하는 문제(각 재료는 한번만 사용 가능)

*문제풀이
N의 최대값이 15000이므로 시간복잡도는 O(nlogn)입니다. 정렬 알고리즘의 시간 복잡도가 O(nlogn) 이므로 정렬을 사용해도 되지만 투포인터를 사용해 접근해보겠습니다. 
재료 리스트를 오름차순으로 정렬하고 투포인터를 양끝에 위치시킨 후 규칙에 따라 포인터를 이동해 합이 M이 되는 조합의 개수를 찾습니다.
*이동 규칙 :
왼쪽 포인터 l = 0, 오른쪽 포인터 r = N-1
합이 M이면 → 카운트 +1, l++, r--
합이 M보다 작으면 → l++
합이 M보다 크면 → r--

```python
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

A = list(map(int, input().split()))
A.sort()

l, r = 0, n - 1
count = 0

while l < r:
    if A[l] + A[r]<M:
        l += 1
    elif A[l] + A[r]>M:
        r -= 1
    else:
        count += 1
        l += 1
        r -= 1

print(count)

'''
