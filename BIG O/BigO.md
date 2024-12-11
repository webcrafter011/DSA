# Big O Notation Overview

Big O Notation is a mathematical notation used to describe the time complexity and space complexity of algorithms. It provides an upper bound on the growth rate of a function as the input size increases.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Common Big O Notations](#common-big-o-notations)
3. [How to Calculate Big O](#how-to-calculate-big-o)
4. [Examples](#examples)
5. [Key Rules](#key-rules)
6. [Resources](#resources)

---

## Introduction

Big O Notation focuses on **worst-case scenarios**, helping to estimate the time or space required for an algorithm as the input size (`n`) grows. It provides a framework to compare algorithm efficiency.

---

## Common Big O Notations

### 1. Constant Time - O(1)
- **Description**: The runtime does not depend on the input size.
- **Example**: Accessing an array element by index.
```python
arr = [1, 2, 3]
print(arr[0])  # O(1)
```

### 2. Logarithmic Time - O(log n)
- **Description**: The runtime increases logarithmically as the input size grows.
- **Example**: Binary Search.
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### 3. Linear Time - O(n)
- **Description**: The runtime grows linearly with the input size.
- **Example**: Iterating through an array.
```python
arr = [1, 2, 3]
for num in arr:
    print(num)  # O(n)
```

#### 4. Linearithmic Time - O(n log n)
- **Description**: The runtime is proportional to n times log n.
- **Example**: Merge Sort, Quick Sort (average case).
```python
# Pseudocode for Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Merging logic
```

### 5. Quadratic Time - O(n^2)
- **Description**: The runtime is proportional to the square of the input size.
- **Example**: Nested loops.
```python
arr = [1, 2, 3]
for i in arr:
    for j in arr:
        print(i, j)  # O(n^2)
```

### 6. Cubic Time - O(n^3)
- **Description**: The runtime is proportional to the cube of the input size.
- **Example**: Triple nested loops.

### 7. Exponential Time - O(2^n)
- **Description**: The runtime doubles with each additional input.
- **Example**: Recursive algorithms like solving the Tower of Hanoi.

### 8. Factorial Time - O(n!)
- **Description**: The runtime grows factorially with the input size.
- **Example**: Generating all permutations of a list.

#### How to Calculate Big O
- Identify the basic operations performed by the algorithm.
- Find the dominant term (the term that grows the fastest as n increases).
- Drop constants and non-dominant terms.

### Examples
### Example 1: Simple Loop
```python
for i in range(n):
    print(i)  # O(n)
```
### Example 2: Nested Loop
```python
for i in range(n):
    for j in range(n):
        print(i, j)  # O(n^2)
```
### Example 3: Recursive Function
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # O(2^n)
```

## Key Rules
- Drop constants: O(2n) becomes O(n).
- Drop non-dominant terms: O(n + n^2) becomes O(n^2).
- Multiplication rule: O(n) * O(log n) becomes O(n log n).
- Focus on the worst-case scenario.

## Contributing
- Feel free to contribute by adding more examples or enhancing the explanations.

