import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N, s, e, k = map(int,input().split())
    num_list = [*map(int,input().split())]
    sort_list = num_list[s-1:e]
    sort_list.sort()
    print(f'#{t} {sort_list[k-1]}')