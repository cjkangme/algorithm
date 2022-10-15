li = ["Intel", "Facebook", "Zillow", "Yahoo", "Pinterest", "Twitter", "Verizon", "Bing", "Apple", "Google", "Microsoft", "Sony", "Paypal", "Skype", "IBM", "Ebay "]

def do_quick_sort(arr):
    def do_sort(left,right):
        if right <= left:
            return
        mid = do_partition(left, right)
        do_sort(left, mid - 1)
        do_sort(mid, right)

    def do_partition(left, right):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        return left
    return do_sort(0, len(arr) - 1)

do_quick_sort(li)
print(li)
