
**Question 1:**
```python
def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b+1):
        if num % c == 0:
            total += num
    return total
```
This function takes three arguments `a`, `b`, and `c`, and returns the sum of all numbers in the range `a` to `b` (inclusive) that are evenly divisible by `c`.

**Question 2:**
```python
def correct_signs(expression):
    signs = expression.split()
    for i in range(1, len(signs), 2):
        if signs[i] == '<':
            if float(signs[i-1]) >= float(signs[i+1]):
                return False
        elif signs[i] == '>':
            if float(signs[i-1]) <= float(signs[i+1]):
                return False
    return True
```
This function takes a string `expression` representing an inequality expression, and returns `True` if the expression is correct and `False` otherwise.

**Question 3:**
```python
def replace_vowels(string, char):
    vowels = 'aeiou'
    result = ''
    for letter in string:
        if letter.lower() in vowels:
            result += char
        else:
            result += letter
    return result
```
This function takes a string `string` and a character `char`, and returns a new string with all the vowels in `string` replaced by `char`.

**Question 4:**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
```
This function calculates the factorial of a given number `n` recursively.

**Question 5:**
```python
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance
```
This function takes two strings `str1` and `str2`, and returns the Hamming distance between them, which is the number of characters that differ between the two strings.
