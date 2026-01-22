*문제
강의 수 : N
블루레이 수 : M
각 강의의 길이가 주어지고 강의 순서는 바꿀 수 없다. 각 블루레이에는 연속된 강의만 담을 수 있다.
모든 강의를 M개의 블루레이에 담을 수 있는 블루레이 최소 크기를 구하는 문제

*문제 풀이
전형적인 이진 탐색 문제
시작 인덱스 : 최대 길이의 레슨
종료 인덱스 : 모든 레슨 길이의 합

*이진 탐색 수행
중앙값 = (시작 인덱스 + 종료 인덱스)/2
중앙값 크기로 모든 레슨을 저장할 수 있으면 종료 인덱스 = 중앙값 - 1 #왼쪽 데이터셋
중앙값 크기로 모든 레슨을 저장할 수 없으면 시작 인덱스 = 중앙값 + 1 #오른쪽 데이터셋
시작 인덱스 > 종료 인덱스를 만족할때까지 진행

'''python
n, m = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start <i :
        start = i
    end += i

while start <= end:
    mid = (start + end) // 2  # 블루레이 크기
    count = 0
    sum = 0

    for i in range(N): #중앙값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > mid:
            count +=1
            sum = 0
        sum += A[i]
    if sum !=0:
        count += 1
    if count > m:
        start = mid +1 
    else:
        end = mid -1

print(start)

'''




