# 4. 합이 같은 부분집합 (DFS : 아마존 인터뷰)
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")

def DFS(i, sum):
    if i == N:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
        return
    elif sum > total/2:
        return
    else:
        DFS(i+1, sum + lst[i])
        DFS(i+1, sum)


if __name__=="__main__":
    N = int(input())
    lst = [*map(int,input().split())]
    total = sum(lst)
    DFS(0, 0)
    print("NO")
