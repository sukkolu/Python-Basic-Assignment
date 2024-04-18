1. **Question 1: Filter out the list of strings**

```python
def filter_list(lst):
    return [item for item in lst if isinstance(item, int)]
```

**Explanation:**
The function `filter_list` takes a list as an argument and returns a new list containing only the integer elements from the original list. It uses a list comprehension to iterate through the input list and check if each item is an instance of the `int` class using the `isinstance` function. If the condition is true, the item is included in the new list.

2. **Question 2: Add indexes to the list elements**

```python
def add_indexes(numbers):
    return [num + i for i, num in enumerate(numbers)]
```

**Explanation:**
The function `add_indexes` takes a list of numbers as an argument and returns a new list where each element is the sum of the original number and its index in the list. It uses a list comprehension to iterate through the input list, getting the index `i` and the corresponding number `num` using the `enumerate` function. The expression `num + i` adds the index to the number, and the resulting value is included in the new list.

3. **Question 3: Calculate the volume of a cone**

```python
import math

def cone_volume(height, radius):
    volume = (1/3) * math.pi * (radius ** 2) * height
    return round(volume, 2)
```

**Explanation:**
The function `cone_volume` takes the height and radius of a cone as arguments and calculates the volume of the cone using the formula `(1/3) * pi * (radius^2) * height`. The calculated volume is then rounded to the nearest hundredth using the `round` function and returned.

4. **Question 4: Find the number of dots in a triangular number sequence**

```python
def triangle(n):
    return (n * (n + 1)) // 2
```

**Explanation:**
The function `triangle` takes an integer `n` as an argument and calculates the number of dots in the `n`-th triangle of the triangular number sequence. The formula used is `(n * (n + 1)) // 2`, which is the mathematical formula for the `n`-th triangular number.

5. **Question 5: Find the missing number in a list**

```python
def missing_num(numbers):
    expected_sum = sum(range(1, 11))
    actual_sum = sum(numbers)
    return expected_sum - actual_sum
```

**Explanation:**
The function `missing_num` takes a list of numbers between 1 and 10 (excluding one number) as an argument and returns the missing number. It calculates the expected sum of the numbers from 1 to 10 using the formula `sum(range(1, 11))`. Then, it calculates the actual sum of the numbers in the input list using the `sum` function. Finally, it subtracts the actual sum from the expected sum to find the missing number.