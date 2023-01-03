# https://www.acmicpc.net/problem/1309

if __name__=="__main__":
    N = int(input())
    dy = [[0 for _ in range(3)] for _ in range(N)]
    devider = 9901
    dy[0] = [1, 1, 1]
    for i in range(1, N):
        dy[i][0] = sum(dy[i-1]) % devider
        dy[i][1] = (dy[i-1][0] + dy[i-1][2]) % devider
        dy[i][2] = (dy[i-1][0] + dy[i-1][1]) % devider
    print(sum(dy[-1])%devider)