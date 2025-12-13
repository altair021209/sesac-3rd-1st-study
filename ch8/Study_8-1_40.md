#소수 구하기:
에라토스테네스의 채 알고리즘을 사용합니다


#코드구현:
-2부터 N까지 모든 정수를 적는다.

-아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.

-P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.

-아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성


```python
import sys

# 입력 받기
N, K = map(int, sys.stdin.readline().split())

# 지워졌는지 확인할 체크 리스트 (인덱스 0~N까지 생성, 처음엔 모두 False)
# False: 안 지워짐, True: 지워짐
is_deleted = [False] * (N + 1)

count = 0

# 2부터 N까지 순회
for i in range(2, N + 1):
    # 아직 지워지지 않은 수라면 (그것은 소수 P)
    if is_deleted[i] == False:
        # P와 P의 배수들을 지워나감 (range(start, end, step))
        for j in range(i, N + 1, i):
            # 아직 안 지워진 수만 카운트
            if is_deleted[j] == False:
                is_deleted[j] = True # 지움 표시
                count += 1
                
                # K번째로 지워진 수 발견 시 출력 후 종료
                if count == K:
                    print(j)
                    sys.exit()
    
```

#생각해볼 점
에라토스테네스의 채 알고리즘은 해당 수 P를 기준으로
P를 제외한 P를 배수를 지워가면서 소수를 찾는 과정인데,

실제로 리스트를 지우기보다도 지운셈 치고 넘어가는것이 편하다

remove()도 $O(n)$의 시간복잡도를 가지기에 이를 반복문에서 시행하면 실질적인 시간복잡도가 $O(n^2)$가 되기 때문
