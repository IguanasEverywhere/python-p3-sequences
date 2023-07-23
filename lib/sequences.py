#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length == 1:
        fib_list.append(0)
    elif length == 2:
        fib_list.append(0)
        fib_list.append(1)
    elif length != 0:
        fib_list.append(0)
        fib_list.append(1)
        for x in range(2, length):
            fib_list.append(fib_list[x-1] + fib_list[x-2])

    print(fib_list)

