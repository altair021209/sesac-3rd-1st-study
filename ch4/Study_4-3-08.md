# 좋은 수

- N개의 수가 주어졌을 때, 어떤 수가 **"다른 수 두 개의 합"**으로 나타낼 수 있다면 그 수를 "좋다(GOOD)"고 합니다.
- 이 문제의 함정은 **"자기 자신을 포함하면 안 된다"**는 것입니다. (예: 0 + 3 = 3 일 때, 3을 만들기 위해 3 자신을 쓰면 안 됨)
- N이 최대 2,000이라서 이중 반복문을 쓰면 시간 초과가 날 수 있으니 투 포인터를 써야 합니다.


# 과정 설명

- 리스트를 오름차순 정렬
- for 문으로 목표값을 설정
- 목표값을 제외한 나머지 리스트에서 투 포인터를 돌림
- 같으면 카운트를 세고 다음 타겟으로 넘어감


# 코드

```python
import sys
input = sys.stdin.readline

# 1. 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 2. 정렬 (투 포인터 사용을 위해 필수)
nums.sort()

count = 0

# 3. 모든 수를 하나씩 target으로 잡고 확인
for i in range(N):
    target = nums[i]
    
    # 투 포인터 초기화 (전체 범위에서 찾음)
    start = 0
    end = N - 1
    
    while start < end:
        current_sum = nums[start] + nums[end]
        
        if current_sum == target:
            # 정답을 찾았는데, 그게 자기 자신(i)을 포함하면 안 됨!
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                # 자기 자신이 아닌 다른 두 수의 합이라면 성공!
                count += 1
                break # 하나 찾으면 되니까 루프 종료
        elif current_sum < target:
            start += 1 # 합을 키워야 하니까 왼쪽 포인터 이동
        else:
            end -= 1 # 합을 줄여야 하니까 오른쪽 포인터 이동

print(count)
```