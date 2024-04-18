1. Write a Python Program to find sum of array:

```python
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example usage
my_array = [10, 20, 30, 40, 50]
print(sum_of_array(my_array))  # Output: 150
```

2. Write a Python Program to find largest element in an array:

```python
def find_largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage
my_array = [5, 10, 3, 20, 1]
print(find_largest_element(my_array))  # Output: 20
```

3. Write a Python Program for array rotation:

```python
def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d is greater than the length of the array
    return arr[d:] + arr[:d]

# Example usage
my_array = [1, 2, 3, 4, 5]
print(rotate_array(my_array, 2))  # Output: [3, 4, 5, 1, 2]
```

4. Write a Python Program to Split the array and add the first part to the end:

```python
def split_and_add(arr, k):
    n = len(arr)
    first_part = arr[:k]
    second_part = arr[k:]
    return second_part + first_part

# Example usage
my_array = [12, 10, 5, 6, 52, 36]
print(split_and_add(my_array, 2))  # Output: [5, 6, 52, 36, 12, 10]
```

5. Write a Python Program to check if given array is Monotonic:

```python
def is_monotonic(arr):
    is_increasing = True
    is_decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            is_increasing = False
        if arr[i] > arr[i-1]:
            is_decreasing = False
    return is_increasing or is_decreasing

# Example usage
print(is_monotonic([1, 2, 2, 3, 4]))  # Output: True
print(is_monotonic([4, 3, 2, 1]))  # Output: True
print(is_monotonic([1, 2, 3, 4, 2]))  # Output: False
```