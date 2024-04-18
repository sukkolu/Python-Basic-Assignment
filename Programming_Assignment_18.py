
**Question 1:**

```python
def filter_list(lst):
    return [item for item in lst if isinstance(item, int)]
```

The `filter_list` function takes a list as input and returns a new list containing only the non-negative integers from the original list.

**Question 2:**

```python
def reverse(txt):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in txt[::-1])
```

The `reverse` function takes a string as input and returns a new string with the characters in reverse order and the case of each character flipped.

**Question 3:**

```python
lst = [1, 2, 3, 4, 5, 6]
first, *middle, last = lst
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4, 5]
print(last)  # Output: 6
```

The solution uses destructuring assignment to unpack the list `lst` into the variables `first`, `middle`, and `last`. The `*middle` syntax collects all the elements between the first and last into the `middle` list.

**Question 4:**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

The `factorial` function uses recursion to calculate the factorial of a given number `n`. If `n` is 0 or 1, the function returns 1. Otherwise, it returns the product of `n` and the factorial of `n - 1`.

**Question 5:**

```python
def move_to_end(lst, elem):
    return [item for item in lst if item != elem] + [item for item in lst if item == elem]
```

The `move_to_end` function takes a list `lst` and an element `elem` as input, and returns a new list with all occurrences of `elem` moved to the end of the list.