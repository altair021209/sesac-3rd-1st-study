# 4-1. 배열과 리스트

![](https://blog.kakaocdn.net/dna/4cFpD/btrbIHDbRzR/AAAAAAAAAAAAAAAAAAAAAF6PwU_faWXRAmWOTqz6_VZas3Igp_wnb_IaYBmFgzD2/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=gU4j67v%2BnsT80YpGTXZ7hyS62Dk%3D)

## 1. 배열(Array)

배열은 메모리의 연속된 공간에 값이 차례로 저장되는 자료구조이다.

각 요소는 인덱스를 이용해 즉시 접근할 수 있다.

### 배열의 특징

- 인덱스를 사용하여 원하는 값에 즉시 접근 가능
- 중간 삽입/삭제 시 해당 인덱스 주변 요소 이동

---

## 2. 리스트(List)

리스트는 값과 포인터를 가진 노드들이 서로 연결된 구조이다.

### 특징

- 인덱스 없이 순차 접근
- 포인터를 이용해 삽입/삭제가 빠름
- 포인터 저장 공간 추가 필요

---

## 3. 파이썬에서의 배열/리스트

파이썬의 `list`는 배열과 연결리스트의 특징을 모두 포함한다.

- 인덱스 접근 가능
- 크기 가변
- 삽입/삭제 가능

따라서 파이썬에서는 일반적으로 배열과 리스트를 따로 구분하지 않는다.

---

# <문제> 평균 구하기 (백준: 1546)

세준이는 기말고사를 망쳤다. 그래서 점수를 조작해 집에 가져가기로 결심했다. 일단 세준이는 자기 점수 중 최댓값을 골랐다. 그런 다음 최댓값을 M이라고 할 때 모든 점수를 점수/M**100으로 고쳤다. 예를 들어 세준이의 최고점이 70점, 수학 점수가 50점이라면 수학 점수는 50/70**100이가 된다. 세준이의 성적을 이 방법으로 계산했을 때 **새로운 평균을 구하는** 프로그램을 작성하시오.

---

## 코드

```python
#입력
#3
#40 80 60

n = input()  # 과목 개수 입력
mylist = list(map(int, input().split()))  # 점수 리스트
mymax = max(mylist)  # 최댓값 M
sum = sum(mylist)  # 전체 점수 합

print(sum * 100 / mymax / int(n))  # 모든 과목에 대한 수식을 총합과 관련한 수식으로 변환

```

---

# 4-2. 구간 합

시간 복잡도를 줄이기 위해 사용하는 특수한 목적의 알고리즘. 코딩 테스트에서 사용 빈도가 높다.

## 1. 구간 합의 이론

![](https://blog.kakaocdn.net/dna/bdVm8P/btsDfPUeekh/AAAAAAAAAAAAAAAAAAAAAIamd5_Yn0tGu9sA1qqafQihELZpUr3vhuhE8aWLEv-y/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=i%2FEOU%2BP44RNAnhQKfagnb%2Frdv4o%3D)

합 배열(prefix sum)을 사용하면 구간 합을 빠르게 계산할 수 있다.

S[i] = A[0] + ... + A[i]

S[i] = S[i-1] + A[i] 로 O(N)에 생성 가능

구간 i~j의 합은

**S[j] - S[i-1]**

---

# <문제> 나머지 합 구하기 (백준: 10986)

수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구하는 프로그램을 작성하시오.

---

## 핵심 아이디어

## 1. 나머지 연산의 성질 활용

```
(A + B) % M = ((A % M) + (B % M)) % M
```

구간 합을 M으로 나눈 나머지는

각 부분합을 나눈 값들을 더한 뒤 다시 % M을 취한 것과 같다.

---

## 2. 구간 합 공식

합 배열 S[i] = A[0] + … + A[i] 로 정의하면

i부터 j까지의 구간 합은:

```
S[j] - S[i-1]
```

이 값을 M으로 나누어 떨어지게 하려면,

```
(S[j] - S[i-1]) % M == 0
```

상단의 식을 변형하면 다음과 같다:

```
S[j] % M == S[i-1] % M
```

➡️ **누적합을 M으로 나눈 나머지가 같은 두 지점(i-1, j)을 고르면
그 사이 구간의 합이 M으로 나누어떨어진다.**

## 코드

```python
# 입력 예시
# 5 3
# 1 2 3 1 2 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 수열 길이, m: 나눌 값
A = list(map(int, input().split()))  # 수열 A
S = [0] * n  # 누적합 배열
C = [0] * m  # 나머지 카운팅 배열

S[0] = A[0]  # 첫 누적합 초기화
answer = 0

# 누적합 생성
for i in range(1, n):
    S[i] = S[i-1] + A[i]
# 예시 S = [1, 3, 6, 7, 9]

# 각 누적합의 나머지 계산
for i in range(n):
    remainder = S[i] % m  # 합 배열을 M으로 나눈 나머지
    if remainder == 0:  # 나머지가 0이면 하나의 구간이 됨
        answer += 1
    C[remainder] += 1  # 나머지 개수 기록
    
| i   | S[i] | S[i] % 3 | answer | C 배열  |
| --- | ---- | -------- | ------ | ------- |
| 0   | 1    | 1        | 0      | [0,1,0] |
| 1   | 3    | 0        | 1      | [1,1,0] |
| 2   | 6    | 0        | 2      | [2,1,0] |
| 3   | 7    | 1        | 2      | [2,2,0] |
| 4   | 9    | 0        | 3      | [3,2,0] |

# 같은 나머지를 가진 인덱스 조합 계산
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1)) // 2  # nC2 조합 공식

print(answer)

```

| 번호 | 시작 인덱스 i | 끝 인덱스 j | 포함 원소                 | 합  |
| ---- | ------------- | ----------- | ------------------------- | --- |
| 1    | 0             | 1           | A[0..1] = [1, 2]          | 3   |
| 2    | 0             | 2           | A[0..2] = [1, 2, 3]       | 6   |
| 3    | 0             | 4           | A[0..4] = [1, 2, 3, 1, 2] | 9   |
| 4    | 2             | 2           | A[2..2] = [3]             | 3   |
| 5    | 2             | 4           | A[2..4] = [3, 1, 2]       | 6   |
| 6    | 3             | 4           | A[3..4] = [1, 2]          | 3   |
| 7    | 1             | 3           | A[1..3] = [2, 3, 1]       | 6   |

---

# 4-4. 슬라이딩 윈도우

## 1. 개념

![](https://velog.velcdn.com/images/iberis/post/6fc5e78d-ca22-4f96-ac48-1328ef03981f/image.jpg)

고정된 크기의 **윈도우를** 리스트 위에서 한 칸씩 이동시키며

나가는 값과 새로 들어오는 값만 갱신하는 방식(O(N)).

---

# <문제> DNA 비밀번호 (백준: 12891)

문자열에서 부분 문자열을 사용할 때 비밀번호로 사용할 부분문자열의 길이를 P라고 한다. 문자열 S와 P가 주어졌을 때, 부분문자열에 포함되어야 할 부분문자열의 최소 개수가 주어진다. 예를 들어 DNA 문자열은 A, C, G, T로만 이루어져 있다. 만약 문자열 “ACGTACGT"에서 길이가 4인 모든 부분문자열을 검사한다면 다음과 같다. 각 부분문자열에서 A, C, G, T가 각각 몇 번 등장하는지를 검사해 조건에 맞으면 비밀번호로 사용할 수 있다.

문자열의 길이가 매우 길기 때문에 슬라이딩 윈도우로 해결해야 한다.

### 예시

입력

```
4 2 # DNA 문자열의 길이, 부분 문자열의 길이
GATA # DNA문자열
1 0 0 1 # 부분 문자열에 포함되어야 할 A, C, G, T의 최소개수

```

설명:

가능한 부분 문자열:

- AT → A=1, T=1 → 조건 만족
- TA → A=1, T=1 → 조건 만족
    
    총 2개가 조건 충족.
    

출력

```
2
```

---

## 코드

```python
# 입력 예시 GATA
checkList = [0] * 4  # 조건으로 필요한 A, C, G, T 최소 개수
myList = [0] * 4  # 현재 윈도우 내부의 문자 개수
checkSecret = 0  # 4개 조건 중 얼마나 충족했는지

# 새로 들어온 문자를 처리
def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 제거되는 문자 처리
def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())  # S: 전체 문자열 길이, P: 윈도우 크기
A = list(input())  # DNA 문자열
checkList = list(map(int, input().split()))  # 조건 최소 개수
Result = 0
# 입력 예시 GATA

# 초기 윈도우 구성
for i in range(P):
    myadd(A[i])

# 초기 조건 검사
if checkSecret == 4:
    Result += 1

# 윈도우 이동
for i in range(P, S):
    j = i - P  # 제거될 문자 index
    myadd(A[i])  # 새 문자 추가
    myremove(A[j])  # 빠지는 문자 제거
    if checkSecret == 4:  # 조건 만족 여부 확인
        Result += 1

print(Result)

```

---

# 4-5. 스택과 큐

## 1. 스택(Stack)

![](https://blog.kakaocdn.net/dna/coDSZF/btqyV5gKcbn/AAAAAAAAAAAAAAAAAAAAAHg4qofNIkdH2BnHJ9fX-lys0CvOWx7if08midI9tGu4/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=QkGdOHHtztC5clEb%2Bvq17%2F%2ByMA4%3D)

LIFO(Last-In First-Out).

`append()`, `pop()` 사용.

---

## 2. 큐(Queue)

![](https://blog.kakaocdn.net/dna/sUjwg/btsJtHaBBIy/AAAAAAAAAAAAAAAAAAAAAJO6rEkSkManUsmTvZ1Pp1X-UHaMD9eilbQFb5thWMNQ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=xjZ2MTzwOG2kHcQD4YJsCMn1SOs%3D)

FIFO(First-In First-Out).

파이썬에서는 `collections.deque` 사용.

---

# <문제> 카드 게임 (백준: 2164)

N장의 카드가 있다. 각각의 카드는 차례로 1에서 N까지 번호가 붙어 있으며, 1번 카드가 가장 위, N번 카드가 가장 아래에 있는 상태로 놓여 있다. 이제 다음과 같은 동작을 카드가 1장 남을 때까지 반복한다.

먼저 가장 위에 있는 카드를 바닥에 버린다. 그 다음 가장 위에 있는 카드를 가장 아래에 있는 카드 밑으로 옮긴다. 이 작업을 반복했을 때 마지막으로 남는 카드를 구하는 프로그램을 작성하시오.

---

## 코드

| 단계 | 큐 상태 (위 → 아래) | 버린 카드 | 아래로 보낸 카드 |
| ---- | ------------------- | --------- | ---------------- |
| 초기 | 1 2 3 4 5 6         | -         | -                |
| 1    | 3 4 5 6 2           | 1         | 2                |
| 2    | 5 6 2 4             | 3         | 4                |
| 3    | 2 4 6               | 5         | 6                |
| 4    | 6 4                 | 2         | 4                |
| 5    | 4                   | 6         | -                |

```python
from collections import deque

N = int(input())  # 카드 개수
myQueue = deque()

# 1~N 카드를 큐에 넣음
for i in range(1, N+1):
    myQueue.append(i)

# 카드가 1장 남을 때까지 반복
while len(myQueue) > 1:
    myQueue.popleft()  # 맨 위 카드 버림
    myQueue.append(myQueue.popleft())  # 다음 카드 맨 아래로 이동

# 마지막 카드 출력
print(myQueue[0])

```