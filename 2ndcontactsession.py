import os
import re

# Extraction of my full name from text file
with open('name.txt', 'r') as file:
    name = file.read()

first_name = name.split()[0]
middle_name = name.split()[1]
last_name = name.split()[2]

print(first_name, middle_name, last_name)

# Printing local file path
current_directory = os.getcwd()

print(current_directory)

# Extraction of baby names from html file
pattern = r"<td>([a-zA-Z]+)</td>"

with open('baby2008.html', 'r') as baby_file:
    file_content = baby_file.read()

baby_names = re.findall(pattern, file_content)

print(baby_names)


# Implementation of binary search
def binary_search(haystack: list[int], needle: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2

    if haystack[mid] == needle:
        return mid

    elif haystack[mid] < needle:
        return binary_search(haystack, needle, mid + 1, right)

    else:
        return binary_search(haystack, needle, left, mid - 1)


# Implementation of a sort algorithm
def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

