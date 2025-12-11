5-4 퀵 정렬
기준값(pivot)을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는것을 반복해 정렬하는 알고리즘.
기준값을 어떻게 선정하는지가 시간 복잡도에 많은 영향을 미친다.
평균적인 시간 복잡도는 O(nlogn)이며 최악의 경우는 O(n^2)이다.

*핵심 이론
pivot을 중심으로 계속 데이터를 2개의 집합으로 나누면서 정렬하는 것이 퀵 정렬의 핵심.

1.배열에서 피벗(pivot) 선택
2.피벗보다 작은 값은 왼쪽 그룹, 큰 값은 오른쪽 그룹에 모음
3.왼쪽 그룹과 오른쪽 그룹을 재귀적으로 다시 퀵 정렬
4.모든 부분 배열이 정렬되면 전체가 정렬된 상태가 됨

*문제 요약
정수 N개가 주어졌을 때, 오름차순으로 정렬했을 때 K번째로 오는 수를 출력하는 문제.
즉, N개의 수 중에서 K번째 작은 수를 찾는 것.

(pivot 선택에 따라 최악의 시간 복잡도가 n^2이므로 이 문제는 병합 정렬등을 이용하는 것이 안전하지만,
퀵 정렬을 이해하고자 퀵 정렬 풀이로 진행)

*pivot을 정하는 방법:
-pivot == K : K번째 수를 찾은 것이므로 알고리즘 종료
-pivot > K : pivot의 왼쪽 부분에 K가 있으므로 왼쪽(Start point ~ pivot-1)만 정렬을 수행
-pivot < K : pivot의 오른쪽 부분에 K가 있으므로 오른쪽(pivot+1 ~ End point)만 정렬을 수행


*코드 구현
import sys
input = sys.stdin.readline
N, k = map(int, input().split())
A = list(map(int, input().split()))  


def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K: # K번째 수가 pivot 이면 더는 구할 필요 없음
            return
        elif K < pivot: # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else:           # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(S, E):
    global A

    # 원소가 2개일 때 처리
    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E    

    # 피벗을 중앙 값으로 교환하여 선택
    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]

    i = S + 1
    j = E    

    while i <= j:
        while pivot < A[j] and j > 0:
            j -= 1
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1

    #i==j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j


# K번째 수 찾기
quickSort(0, N - 1, k - 1)
print(A[k - 1])
