#거의 소수 구하기: 

어떤 수가 소수의 N제곱 $(N ≥ 2)$ 꼴일 때, 그 수를 거의 소수라고 한다.
두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.

#입력:
왼쪽 범위 A 와 오른쪽 범위 A가 공백을 사이에 두고
한줄에 입력됨


#알고리즘 로직:

소수 판별 범위 설정: 입력된 최대 범위 B가 주어졌을 때, 어떤 소수 P의 제곱이 B보다 작거나 같으려면 P는 B의 제곱근보다 작거나 같아야 한다. 따라서 B의 제곱근까지만 소수를 구하면 됨. 예를 들어 B가 10의 14제곱이라면 10의 7제곱까지만 체를 생성한다

에라토스테네스의 체 실행: B의 제곱근까지의 모든 소수를 구하여 리스트에 저장한다

거듭제곱 수 카운팅: 구해둔 각 소수 P에 대해 P의 제곱, 3제곱, 4제곱 등을 계산하며 그 값이 A와 B 범위 사이에 있는지 확인하고 카운트한다

코드 구현 (Python) 입력값 B가 매우 클 수 있으므로(보통 10의 14제곱), 효율적인 범위 설정이 중요

#코드 구현:
```python
import sys

# 입력 받기 (A: 시작, B: 끝)
A, B = map(int, sys.stdin.readline().split())

# 1. 에라토스테네스의 체 범위 설정
# P^2 <= B 여야 하므로, P <= sqrt(B)
limit = int(B ** 0.5)

# 2. 에라토스테네스의 체 초기화
# is_prime[i]가 True면 i는 소수
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

# 소수 구하기 (sqrt(limit)까지만 반복해도 됨)
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

# 3. 거의 소수 개수 구하기
count = 0

# limit까지의 숫자 중 소수인 것만 탐색
for i in range(2, limit + 1):
    if is_prime[i]: # i가 소수라면
        P = i
        temp = P * P # P^2 부터 시작
        
        # P의 N제곱이 B보다 작거나 같은 동안 반복
        while temp <= B:
            # 범위 [A, B] 안에 들어오는지 확인
            if temp >= A:
                count += 1
            
            # 다음 제곱수 계산 (P^2 -> P^3 -> P^4 ...)
            # 주의: temp * P가 너무 커져서 오버플로우가 날 수 있으나 
            # 파이썬은 큰 정수를 자동 처리함. (타 언어는 주의 필요)
            temp *= P

print(count)
```

