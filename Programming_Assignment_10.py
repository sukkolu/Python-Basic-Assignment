1. Write a Python program to find the sum of elements in a list:

```python
def sum_of_elements(lst):
    return sum(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
result = sum_of_elements(my_list)
print(result)  # Output: 15
```

2. Write a Python program to multiply all numbers in a list:

```python
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
my_list = [2, 3, 4, 5]
result = multiply_elements(my_list)
print(result)  # Output: 120
```

3. Write a Python program to find the smallest number in a list:

```python
def find_smallest(lst):
    return min(lst)

# Example usage
my_list = [10, 5, 8, 2, 7]
result = find_smallest(my_list)
print(result)  # Output: 2
```

4. Write a Python program to find the largest number in a list:

```python
def find_largest(lst):
    return max(lst)

# Example usage
my_list = [12, 45, 23, 67, 32]
result = find_largest(my_list)
print(result)  # Output: 67
```

5. Write a Python program to find the second-largest number in a list:

```python
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])
    
    for i in range(2, len(lst)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    
    return second_largest

# Example usage
my_list = [10, 5, 8, 20, 7]
result = find_second_largest(my_list)
print(result)  # Output: 10
```

6. Write a Python program to find the N largest elements from a list:

```python
def find_n_largest(lst, n):
    return sorted(lst, reverse=True)[:n]

# Example usage
my_list = [12, 45, 23, 67, 32, 89, 78]
n = 3
result = find_n_largest(my_list, n)
print(result)  # Output: [89, 78, 67]
```

7. Write a Python program to print even numbers in a list:

```python
def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_even_numbers(my_list)
print(result)  # Output: [2, 4, 6, 8, 10]
```

8. Write a Python program to print odd numbers in a list:

```python
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_odd_numbers(my_list)
print(result)  # Output: [1, 3, 5, 7, 9]
```

9. Write a Python program to remove empty lists from a list:

```python
def remove_empty_lists(lst):
    return [sub_list for sub_list in lst if sub_list]

# Example usage
my_list = [[1, 2], [], [3, 4], [], [5]]
result = remove_empty_lists(my_list)
print(result)  # Output: [[1, 2], [3, 4], [5]]
```

10. Write a Python program to clone or copy a list:

```python
def clone_list(lst):
    return lst.copy()

# Example usage
my_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(my_list)
print(cloned_list)  # Output: [1, 2, 3, 4, 5]
```

11. Write a Python program to count the occurrences of an element in a list:

```python
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5, 2]
result = count_occurrences(my_list, 2)
print(result)  # Output: 4
```