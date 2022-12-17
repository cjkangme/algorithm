# 2. 이진트리순회(DFS: Depth First Search)
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v, end=" ") # 함수 본연의 일


if __name__=="__main__":
    DFS(1)
