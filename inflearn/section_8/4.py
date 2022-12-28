# 4. 최대 부분 증가 수열

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

# 내 접근
if __name__=="__main__":
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = [1] * N
    for i in range(1, N):
        for j in reversed(range(i)):
            if lst[i] > lst[j]: # 리스트 j에서 증가할 수 있음
                if cnt[j] >= cnt[i]: # cnt j에서 증가하는 것이 현재 최대값일 경우 1 증가
                    cnt[i] = cnt[j] + 1
    print(max(cnt)) # 최대 증가 수열 출력