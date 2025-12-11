#시간복잡도 활용하기

#기본적인 시간복잡도 계산


*1번 코드
```maekdown
```python

for i in range(100000):
    print("hello world")
```
기본적으로 for문은 N번 반복하는 것으로 간주한다.
따라서 해당 코드의 빅-오 표기법에 따른 시간 복잡도는
O(N)이다


*2번 코드
```maekdown
```python

for i in range(100000):
    print("hello,")

for i in range(100000):
    print("world! )

```

1번 코드의 시간 복잡도가 O(N)이고,
2번 코드에서는 해당 반복문이 연달아 있으므로, 원래는 O(2N)의 시간복잡도를 가지지만,
코딩 테스트에서는 일반적으로 상수를 무시하므로
두 코드는 모두 시간복잡도가 O(N)이다.
 


#수 정렬 알고리즘
*버블정렬

```markdown
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):               # 전체 반복 횟수 (마지막 원소는 자동 정렬)
        for j in range(n - i - 1):       # 인접한 두 원소를 비교
            if arr[j] > arr[j + 1]:      
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
버블정렬은 앞뒤의 숫자를 비교하는, 모든 경우에 대해 크기비교를 수행하는 알고리즘이다.
따라서 전체 인자를 반복하는 반복횟수가 N번,
인접한 두 원소끼리 비교하는 반복횟수가 N-1번으로,
O(N**2)의 시간 복잡도를 가진다.

O(N)이 1,000,000만번 연산을 나타낸다고 할 때, 
버블정렬은 (1,000,000)**2 = 1,000,000,000,000 으로 2초안에 해결할 수 없는 알고리즘이다.


*병합정렬

```markdown
```python

def merge(left, right):
    i, j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
    	if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
    	sorted_list.append(left[i])
        i += 1
    while j < len(right):
    	sorted_list.append(right[j])
        j += 1
    return sorted_list

```

병합정렬(Merge sort)는 모든 케이스에 대해 비교하는 것이 아니라,
리스트를 계속 절반으로 줄여가며 인자들을 비교한다

이때 모드 인자에 대한 반복을 1회 하여 O(N) 의 시간복잡도를 가지고,
리스트를 절반으로 줄여가며 인자들을 비교하기에 실행횟수 N번이 올라가도 연산횟수는 같이 올라가지 않는다. 
이때 O(log_2(N))의 시간 복잡도를 가지므로 
전체의 코드의 시간 복잡도는 O(N log N)이 된다.

이때의 연산 횟수는 1,000,000 * log_2(1,000,000) = 약 20,000,000 이므로, 
2초 안에 연산이 적합한 알고리즘으로 판단할 수 있다.

