"""Implement bubble sort algorithm.
Note: In each iteration, largest element bubbles to the top."""

def bubble_sort(arr):
    n = len(arr) - 1
    # loop through iterations
    for i in range(n):
        m = n - i
        # bubble up the largest element
        for j in range(m):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] =  arr[j]
                arr[j] = temp
        iter_print(i, arr)


def iter_print(iter, arr):
    print('Iteration #{}: '.format(iter + 1),arr)


def main():
    arr1 = [21,4,1,3,9,20,25,6,21,14]
    bubble_sort(arr1)

if __name__ == "__main__":
    main()

