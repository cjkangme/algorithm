def solution(num):
    if num == 0:
        return 0
    answer = ""
    while num != 0:
        if num % (-2): # 1 or -1
            answer = "1" + answer
            num = num // (-2) + 1
        else:
            answer = "0" + answer
            num = num // (-2)
    return answer

if __name__=="__main__":
    N = int(input())
    print(solution(N))