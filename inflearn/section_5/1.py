import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")

num_str, m = map(int,input().split())
lst = list(map(int,str(num_str)))
largest = []
for num in lst:
    while m > 0:
        if len(largest) == 0:
            largest.append(num)
            break
        if largest[-1] >= num:
            largest.append(num)
            break
        else:
            largest.pop()
            m -= 1
    if m == 0:
        largest.append(num)
if m != 0:
    largest = largest[:-m]
string = "".join(map(str,largest))
print(int(string))



