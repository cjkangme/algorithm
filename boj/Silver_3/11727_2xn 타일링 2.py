# https://www.acmicpc.net/problem/11727

if __name__=="__main__":
    n = int(input())
    dy = [0] * (n+2)
    dy[1] = 1
    dy[2] = 3
    for i in range(3, n+1):
        dy[i] = dy[i-1] + dy[i-2] * 2
    print(dy[n]%10007)