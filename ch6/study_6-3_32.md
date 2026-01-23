# 수 찾기

- N개의 정수(A)가 주어지고, M개의 숫자(X)들이 주어집니다.
- 각 X가 A 안에 들어있는지 확인해서 있으면 1, 없으면 0을 출력해야 합니다.
- N이 최대 10만, M도 최대 10만입니다. 그냥 if X in A: (순차 탐색)를 쓰면 10만 X 10만 = 100억 번 연산하게 되어 시간 초과로 탈락합니다. 빠르기가 생명인 문제입니다.

# 과정

- 리스트 정렬
- 찾아야할 숫자들을 하나씩 꺼냄
- 이진 탐색 알고리즘으로 숫자들을 확인

# 이진 탐색
- `start` , `end` 를 정해두고, 그 사이의 `mid` 인덱스를 구함
- `list[mid]` > `target` 이라면 `end` = `mid-1`
- `list[mid]` < `target` 이라면 `start` = `mid+1`


# 코드
```python
import sys
input = sys.stdin.readline

# 1. 입력 받기
N = int(input())
# 이진 탐색을 할 '대상 리스트'
A = list(map(int, input().split()))

M = int(input())
# 찾아야 할 '타겟 숫자들'
targets = list(map(int, input().split()))

# 2. 정렬 (이진 탐색 필수 조건!)
A.sort()

# 3. 이진 탐색 함수 정의
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        

        if array[mid] == target:
            return True
        # 타겟이 중간값보다 작으면, 왼쪽 부분만 본다
        elif array[mid] > target:
            end = mid - 1
        # 타겟이 중간값보다 크면, 오른쪽 부분만 본다
        else:
            start = mid + 1
    return False

# 4. 각 타겟에 대해 탐색 실행
for target in targets:
    if binary_search(A, target, 0, N - 1):
        print(1)
    else:
        print(0)

```