# https://www.acmicpc.net/problem/1463

if __name__=="__main__":
    N = int(input())
    dy = [0] * (N+1)
    for i in range(2, N+1):
        if i % 6 == 0:
            dy[i] = min(dy[i-1]+1, dy[i//3]+1, dy[i//2]+1)
        elif i % 2 == 0:
            dy[i] = min(dy[i-1]+1, dy[i//2]+1)
        elif i % 3 == 0:
            dy[i] = min(dy[i-1]+1, dy[i//3]+1)
        else:
            dy[i] = dy[i-1]+1
    print(dy[N])