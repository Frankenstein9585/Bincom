from typing import List


def fibonacci_generator(n) -> List[int]:
    fib_list = [0, 1]
    for i in range(2, n):
        next_value = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_value)
    return fib_list


print(fibonacci_generator(10))
