#평균 구하기

*문제: 점수N개를 입력한다. 이 중 최댓값을 M, 모든 점수를 a라고 할 때 모든 a_n에 대해 이하의 
변환을 적용한다
```python
*a_n = a_n / M * 100*
```
이렇게 최댓값을 제외한 모든 점수를 변환했을 때, 새로운 평균을 구하는 프로그램을 작성


*핵심 아이디어: 최댓값을 제외한 숫자가 3개 존재할 때, 이런 수식이 세워진다 

```python
average = ((a1 / M * 100) + (a2 / M * 100) + (a2 / M* 100)) / 3 
```
해당 수식에서는 M*100의 부분이 겹치기 때문에 식을 이렇게 정리할 수 있다

```python
averge  = (a1 + a2 + a3) / (M * 100) / 3

```

따라서 각 값에 대한 연산을 시행할 필요 없이
-모든 값을 리스트에 적용
-최댓값과 리스트 내부의 합을 구함
-연산 적용
이런 프로세스로 진행하면 된다

*코드
```python
N = int(input())
my_scores = map(int, input().split())
Sum = sum(my_scores)
Max = max(my_scores)

average = Sum / (Max * 100) / N
print(average)
```