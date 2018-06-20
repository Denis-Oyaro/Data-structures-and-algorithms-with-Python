"""Implement a function recursively to get the desired
Fibonacci sequence value."""

def get_fib(position):
    # base case
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fib(position - 2) + get_fib(position - 1)


def main():
    # Test cases
    print(get_fib(9))
    print(get_fib(11))
    print(get_fib(0))

if __name__ == "__main__":
    main()