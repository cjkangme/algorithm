if __name__ == "__main__":
    N = int(input())
    dy = [0] * (N+2)
    dy[0] = 1
    dy[2] = 3
    for i in range(4, N+1, 2):
        dy[i] = dy[i-2] * 3 + sum(dy[:i-2]) * 2
    dy[0] = 0
    print(dy[N])