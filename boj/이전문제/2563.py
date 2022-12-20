#2563. 색종이
import sys
input = sys.stdin.readline
# 도화지 리스트 초기화
paper = list(range(100))
for i in range(100):
    paper[i] = list(range(100))
# 색종이를 붙인 부분을 *로 표시
T = int(input())
for t in range(T):
    x, y = map(int,input().split())
    for n in range(x, x+10):
        for m in range(y, y+10):
            paper[n][m] = "*"
# * 개수를 세어 넓이 계산
cnt = 0
for i in range(100):
    cnt += paper[i].count("*")
print(cnt)