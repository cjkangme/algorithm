# https://www.acmicpc.net/problem/2193

if __name__=="__main__":
    N = int(input())
    dy = [[0 for _ in range(2)] for _ in range(N+1)]
    dy[1][1] = 1
    for i in range(2, N+1):
        dy[i][1] = dy[i-1][0]
        dy[i][0] = dy[i-1][0] + dy[i-1][1]
    print(sum(dy[N]))