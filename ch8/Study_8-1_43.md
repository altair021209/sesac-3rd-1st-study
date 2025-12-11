# 문제 043 --- 제곱이 아닌 수 찾기

## 문제 설명

\[min, max\] 범위 안에서 제곱수의 배수가 아닌 값들을 세는 문제다.

min과 max 구간이 주어졌을 때
이 범위 안에서 제곱수의 배수가 아닌 값들이 몇 개인지 세는 문제다.
일반적으로 1조 같은 값이 등장해서 범위가 매우 넓어 보이지만
실제로는 max - min 의 차이가 1,000,000 이내이기 때문에
이 구간만을 대상으로 하면 충분히 빠르게 계산할 수 있다.

제곱수 판별을 일반 반복문으로 하면 시간이 오래 걸리기 때문에
에라토스테네스의 체 개념을 제곱수에 맞게 응용한다.
즉 어떤 i에 대해 i의 제곱수를 pow로 두고
구간 안에서 pow의 배수들을 모두 체크해 버린다.
체크되지 않은 값만 세면 제곱수가 아닌 수가 된다.

## 풀이 과정

구간 길이에 맞춰 False로 이루어진 리스트를 만든다.
i를 2부터 시작해 ii 값이 max보다 큰 순간까지 반복한다.
ii 를 현재 제곱수로 보고
min부터 시작될 수 있는 첫 배수를 찾고
범위 끝까지 반복하며 해당 위치를 True로 바꾼다.
마지막에 리스트에서 False로 남아있는 값들을 세어 출력한다.

## 코드

``` python
import math
Min, Max = map(int, input().split())
Check = [False] * (Max - Min + 1)    # 구간의 길이에 맞춘 체크 리스트

for i in range(2, int(math.sqrt(Max) + 1)):
    pow = i * i                       # 현재 제곱수
    start_index = int(Min / pow)      # 처음 시작할 배수 위치
    if Min % pow != 0:
        start_index += 1              # 나누어 떨어지지 않으면 +1

    for j in range(start_index, int(Max / pow) + 1):
        Check[int(j * pow) - Min] = True   # 제곱수의 배수는 제거 표시

count = 0

for i in range(0, Max - Min + 1):
    if not Check[i]:                  # 제거되지 않은 값만 센다
        count += 1

print(count)
```
