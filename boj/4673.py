#4673. self number

numbers = list(range(1,10001)) # 1~10000까지 범위 정해주기
remove=[]              # 생성자 리스트
for num in numbers: 
    for n in str(num): # str로 변환
        num += int(n)  # 생성자 구하기 
    if num <= 10000:   #1000보다 작으면 
        remove.append(num) # remove 리스트에 올리기
for num in set(remove): #중복된 숫자 정리
    numbers.remove(num)
for self in numbers: # 최종 구하는 값
    print(self)