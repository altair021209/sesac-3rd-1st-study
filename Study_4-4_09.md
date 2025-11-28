
*문제 요약

민호는 임의로 만든 DNA 문자열 내의 일부 구간을 비밀번호로 사용하려고 한다.
DNA 문자열은 A, C, G, T로 구성된다.

하지만 비밀번호가 되려면 각 문자(A/C/G/T)가 최소 몇 번 이상 등장해야 한다는 조건이 있다.

DNA 문자열의 길이와 비밀번호로 사용할 부분 문자열의 길이가 1,000,000 으로 매우 크기 때문에 
슬라이딩 윈도우의 개념을 이용하여 시간 복잡도 O(N) 안에 해결해야 한다.

* 슬라이딩 윈도우란?
길이가 P인 일정한 크기의 창(window)을 잡고,
오른쪽으로 한 칸씩 이동하며 조건을 검사하는 방식.

-처음 window가 S 문자열의 앞부분에 위치

-이후 window가 오른쪽으로 한 칸씩 이동

-이동할 때마다 빠진 문자 하나, 새로 들어온 문자 하나만 반영해 효율적으로 계산



✔ 1단계: 초기 준비

DNA 문자열 리스트: C C T G G A T T G

필요한 최소 조건 리스트:

A: 2

C: 0

G: 1

T: 1

✔ 2단계: 초기 window 만들기

길이 P만큼 문자를 카운팅하여
현재 상태 리스트를 만든다.
예: A=1, C=1, G=1, T=1 

(초기 window가 조건 리스트와 비교했을 때
예를 들어 A가 부족하면 → 비밀번호 조건 실패)

✔ 3단계: 윈도우 이동

윈도우를 한 칸 오른쪽으로 이동하면서:

왼쪽에서 빠진 문자 카운트 -1

오른쪽의 새 문자 카운트 +1

변경된 현재 상태 리스트와
비밀번호 조건 리스트를 비교하여
조건을 만족하면 → “유효한 비밀번호 개수 +1”

이 과정을 문자열 끝까지 반복.

*핵심은?
매 이동마다 전체 카운트를 다시 새로 계산하지 않고,
빠진 문자와 새로 들어온 문자만 갱신하여 조건을 만족하는 window의 총 개수를 출력한다



*코드 구현

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

# 함수 정의
def myadd(c): # 새로 들어온 문자를 처리하는 함수
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


def myremove(c): # 제거되는 문자를 처리하는 함수
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


S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# checkList[i] 값이 0이면 이미 조건 충족
for i in range(4):
if checkList[i] == 0:
checkSecret += 1

# 초기 P 부분 문자열 처리
for i in range(P):
myadd(A[i])
if checkSecret == 4:
Result += 1

# 슬라이딩 윈도우 진행
for i in range(P, S):
j = i - P
myadd(A[i])
myremove(A[j])
if checkSecret == 4:
Result += 1

print(Result)