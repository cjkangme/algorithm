li = ["Intel", "Facebook", "Zillow", "Yahoo", "Pinterest", "Twitter", "Verizon", "Bing", "Apple", "Google", "Microsoft", "Sony", "Paypal", "Skype", "IBM", "Ebay "]

for i in range(len(li)-1):
    for j in range(i, len(li)):
        temp = ""
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print(li)

# 실행 횟수 : N + (N-1) + (N-2)... = N(N+1)/2
# 즉 N**2에 비례한다.
