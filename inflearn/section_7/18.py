# Merge_sort

arr = [23, 11, 45, 36, 15, 67, 33, 21]


def merge_sort(lt, rt):
    if lt < rt:  # lt부터 rt까지의 영역을 두개로 잘라 나누는 역할을 함
        mid = (lt + rt) // 2
        merge_sort(lt, mid)
        merge_sort(mid+1, rt)
        temp = []  # 분할 후 정복(합병)
        low, high = lt, mid+1
        while low <= mid and high <= rt:
            if arr[low] <= arr[high]:
                temp.append(arr[low])
                low += 1
            else:
                temp.append(arr[high])
                high += 1
        if low <= mid:
            temp = temp + arr[low:mid+1]
        if high <= rt:
            temp = temp + arr[high:rt+1]
        for i in range(len(temp)):
            arr[i+lt] = temp[i]


if __name__ == "__main__":
    print("Before Sort : ", arr)
    merge_sort(0, len(arr)-1)
    print("After Sort : ", arr)
