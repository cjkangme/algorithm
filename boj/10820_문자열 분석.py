# 10820. 문자열 분석

import sys

if __name__=="__main__":
    while True:
        try:
            string = input()
            #소문자, 대문자, 숫자, 공백
            answer = [0, 0, 0, 0]
            for c in string:
                if c.islower():
                    answer[0] += 1
                elif c.isupper():
                    answer[1] += 1
                elif c.isdigit():
                    answer[2] += 1
                else:
                    answer[3] += 1
            print(*answer)
        except:
            sys.exit(0)
