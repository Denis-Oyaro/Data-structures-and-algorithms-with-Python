""" Top down implementation of merge sort. """

def mergeSort(arr, beginIndx, endIndx):
    if beginIndx >= endIndx:
        return
    middleIndx = (beginIndx + endIndx) // 2
    mergeSort(arr, beginIndx, middleIndx)
    mergeSort(arr, middleIndx + 1, endIndx)
    merge(arr, beginIndx, middleIndx, endIndx)

def merge(arr, beginIndx, middleIndx, endIndx):
    left_subarr = arr[beginIndx:middleIndx + 1]
    right_subarr = arr[middleIndx + 1:endIndx + 1]

    # add sentinel value
    left_max = max(left_subarr)
    right_max = max(right_subarr)
    sentinel = max((left_max,right_max)) + 1
    left_subarr.append(sentinel)
    right_subarr.append(sentinel)

    # perform the sorting
    i = 0 # track left subarray
    j = 0 # track right subarray
    for k in range(beginIndx, endIndx + 1):
        if left_subarr[i] <= right_subarr[j]:
            arr[k] = left_subarr[i]
            i += 1
        else:
            arr[k] = right_subarr[j]
            j += 1
    
    #free allocated memory
    del left_subarr
    del right_subarr


def main():
    arr1 = [77,-5,27,-33,0,6,-5,12,90]
    print("arr1 before mergesort:",arr1)
    mergeSort(arr1, 0, len(arr1) - 1)
    print("arr1 after mergesort:",arr1)

if __name__ == "__main__":
    main()




