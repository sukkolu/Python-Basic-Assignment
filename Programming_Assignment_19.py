
**Question 1:**
```python
def double_char(string):
    return ''.join(char * 2 for char in string)
```
The function `double_char` takes a string as input and returns a new string where each character in the original string is repeated once.

**Question 2:**
```python
def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"
```
The function `reverse` takes a value and checks if it is a boolean. If it is, it returns the opposite boolean value. If it is not a boolean, it returns the string "boolean expected".

**Question 3:**
```python
def num_layers(n):
    thickness = 0.0005 * (2 ** n)
    return f"{thickness:.3f}m"
```
The function `num_layers` takes an integer `n` as input and returns a string representing the thickness of the paper in meters after it has been folded `n` times. The initial thickness of the paper is 0.5mm, and it doubles in thickness after each fold.

**Question 4:**
```python
def index_of_caps(string):
    return [i for i, char in enumerate(string) if char.isupper()]
```
The function `index_of_caps` takes a string as input and returns a list of indices where the uppercase letters are located in the string.

**Question 5:**
```python
def find_even_nums(n):
    return [i for i in range(2, n+1, 2)]
```
The function `find_even_nums` takes an integer `n` as input and returns a list of all even numbers from 2 to `n` (inclusive) using a list comprehension.