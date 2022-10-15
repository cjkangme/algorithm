li = ["Intel", "Facebook", "Zillow", "Yahoo", "Pinterest", "Twitter", "Verizon", "Bing", "Apple", "Google", "Microsoft", "Sony", "Paypal", "Skype", "IBM", "Ebay "]


def do_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_arr, pivot_arr, right_arr = [], [], []
    for data in arr:
        if data < pivot:
            left_arr.append(data)
        elif data == pivot:
            pivot_arr.append(data)
        else:
            right_arr.append(data)
    return do_quick_sort(left_arr) + pivot_arr + do_quick_sort(right_arr)

print(do_quick_sort(li))