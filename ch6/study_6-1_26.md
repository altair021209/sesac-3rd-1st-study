# 문제 정의
자연수 N과 M이 주어졌을 때 길이가 M인 수열 구하기
1부터 N까지 자연수중에서 중복 없이 M개를 고른 수열


# 코드 설명
``` python

N, M = map(int, input().split())
# 입력 한줄에서 N,M 읽음

S = [0] * M              # 길이 M짜리 리스트 만듦 
visited = [False] * N   # True 면  i+1 숫자를 이미 수열에 사용 중 

def backtrack(length):
    if length == M:     # 길이가 M인 수열 다 채웠으면 종료
        print(' '.join(str(x + 1) for x in S)) # 완성된 수열 s 출력  , s에는 i 저장해서 출력은 x+1로 함
        return

    for i in range(N):  # S[length]에 넣을 후보 0~N-1까지 전부 시도
        if not visited[i]:  
            visited[i] = True  # i+1을 사용중으로 표시
            S[length] = i  # 현재 자리에 i를 넣음
            backtrack(length + 1)  # 다음 칸 채우러 감 (재귀)
            visited[i] = False   # 재귀가 끝나고 돌아오면 방금 선택했던 i를 취소 

backtrack(0)


```
