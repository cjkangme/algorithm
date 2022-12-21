#https://www.acmicpc.net/problem/2004

def cnt_2(num):
    cnt = 0
    while num > 1:
        num = num // 2
        cnt += num
    return cnt

def cnt_5(num):
    cnt = 0
    while num > 1:
        num = num // 5
        cnt += num
    return cnt

n, m = map(int,input().split())

n_2, n_5 = cnt_2(n), cnt_5(n)
m_2, m_5 = cnt_2(m), cnt_5(m)
nm_2, nm_5 = cnt_2(n-m), cnt_5(n-m)

ans_2 = n_2 - m_2 - nm_2
ans_5 = n_5 - m_5 - nm_5

print(min(ans_2, ans_5))