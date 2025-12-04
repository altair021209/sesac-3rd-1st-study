#병합정렬

병합정렬은 분할과 정복 방식을 ㅅ용해 데이터를 분할하고 집합을 정렬하며 합치는 알고리즘

그룹을 N/2^i 개로 나누어서 정렬을 시행한다

<img width="2098" height="2119" alt="image" src="https://github.com/user-attachments/assets/9e3192ad-69f0-40a1-bcdf-6e7111f25da7" />

병합정렬은 투 포인터에 의해 정렬된다


#수 정렬하기2
*그룹을 N/^i 개로 나누고, 각 그룹을 병합하는 과정에서 오름차순 정렬한다 

```python
import sys
input = sys.stdin.readline

def merge_sort(s,e):
  if e-s < 1: return # 더이상 쪼갤 수 없으면 실행 종료
  m = int(s + (e -s) / 2) # 중간지점 m 정의
  merge_sort(s,m)      # 앞에서 부터m까지
  merge_sort(m + 1, e) # m에서부터 끝까지 // 이들은 재귀함수로 호출되기 때문에 쪼갤 수 없을 때까지 계속 쪼갠다
  for i in range(s, e + 1): 
    tmp[i] = A[i] #데이터 임시 백업

  k = s
  index1 = s  #앞 배열의 첫번째 인덱스
  index2 = m + 1 #뒷 배열의 첫번째 인덱스 선언
  while index1 <= m and index2 <= e: 
    if tmp[index1] > tmp[index2]:
      A[k] = tmp[index2]
      k += 1
      index2 += 1  
    else:
      A[k] = tmp[index1]
      k += 1
      index += 1 

#투포인터를 이용하여 병합할 때 정렬을 실행; 
#만약 앞의 그룹의 요소가 뒤 그룹의 요소보다 작다면 뒤의 데이터를 병합할 그룹에 삽입함
#그 후 뒤 요소의 인덱스를 1 증가, 이를 반복하여 정렬을 실행


  while index1 <= m:
    A[k] = tmp[index1]
    k += 1
    index1 += 1
  while index2 <= e:
    A[k] = tmp[index2]
    k+= 1
    index2 += 1

#바로 위의 루프가 끝났다면 남은 요소를 그 뒤에 다 채워넣음


N = int(input())
A = [0] * int(N+1)
tmp = [0] * int(N+1)

for i in range(1, N+1):
  A[i] = int(input())

merge_sort(1,N)

for i in range(1, N+1):
  print((A[i], end=" ")

```
