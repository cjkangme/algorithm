# Quick Sort

def quick_sort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):  # pivot값 기준으로 파티션 수행
            if arr[i] <= pivot:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        arr[pos], arr[rt] = arr[rt], arr[pos]
        # pos(pivot값이 저장된 인덱스) 기준으로 좌우로 나뉘어 퀵정렬 수행
        quick_sort(lt, pos-1)
        quick_sort(pos+1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before Sort : ", arr)
    quick_sort(0, len(arr)-1)
    print("After Sort : ", arr)
