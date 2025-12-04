#기수 정렬

*값을 비교하지 않고 대표자리값 끼리만을 비교하는 정렬,
*일의자리 -> 십의 자리 -> 백의 자리 순서대로 비교하여 정렬함
*시간복잡도는 O(Kn) //K는 데이터의 자릿수

*시간복잡도가 가장 짧은 정렬


#기수정렬 알고리즘

원본 배열을 일의자릿수 기준으로 하여 큐에 삽입
-> 들어간 순서대로 pop
-> 십의 자리를 기준으로 과정 진행

#수 정렬하기3
*기수정렬에서 서브 알고리즘으로 사용하는 계수정렬 알고리즘을 구현한다

```python
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for i in range(N):
  count[int(input()] += 1

for i in range(10001):
  if count[i] != 0:
    for j in range(count[i]):
      print(i)

```
