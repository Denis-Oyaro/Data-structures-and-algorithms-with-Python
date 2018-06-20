"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    QUICKSORT(array, 0, len(array) - 1)
    return array

def QUICKSORT(array, p, r):
    if p < r:
        q = PARTITION(array, p, r)
        QUICKSORT(array, p, q-1)
        QUICKSORT(array, q+1, r)

def PARTITION(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p,r):
        if array[j] <= x:
            i = i + 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    array[r] = array[i+1]
    array[i+1] = x
    return i+1

def main():
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quicksort(test))

if __name__ == "__main__":
    main()   