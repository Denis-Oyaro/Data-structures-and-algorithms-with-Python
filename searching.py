"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    lower_indx = 0
    upper_indx = len(input_array) - 1
    while lower_indx <= upper_indx:
        middle_indx = lower_indx + (upper_indx - lower_indx) // 2
        if input_array[middle_indx] == value:
            return middle_indx
        elif value > input_array[middle_indx]:
            lower_indx = middle_indx + 1
        else:
            upper_indx = middle_indx - 1
    return -1

def main():
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))

if __name__ == "__main__":
    main()