
```python
# Question 1
def list_operation(x, y, n):
    result = []
    for i in range(x, y+1):
        if i % n == 0:
            result.append(i)
    return result

# Question 2
def simon_says(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(1, len(lst1)):
        if lst1[i-1] != lst2[i]:
            return False
    return True

# Question 3
def society_name(names):
    society = ''.join([name[0].upper() for name in sorted(names)])
    return society

# Question 4
def is_isogram(string):
    return len(set(string.lower())) == len(string)

# Question 5
def is_in_order(string):
    return string == ''.join(sorted(string))
```

Explanations:

1. **list_operation(x, y, n)**: This function takes three parameters: `x` (the start of the range), `y` (the end of the range), and `n` (the divisor to be checked against). It creates an empty list `result`, and then iterates through the range `x` to `y+1` (inclusive), checking if each number is divisible by `n`. If it is, the number is added to the `result` list. Finally, the function returns the `result` list.

2. **simon_says(lst1, lst2)**: This function takes two lists as input and checks if the second list follows the first list by one element. It first checks if the two lists have the same length, and returns `False` if they don't. Then, it iterates through the second list, starting from the second element, and checks if the current element of the second list is the same as the previous element of the first list. If any of these checks fail, the function returns `False`. If all checks pass, the function returns `True`.

3. **society_name(names)**: This function takes a list of names as input and returns the name of the secret society, which is the first letter of each name in the list, sorted in alphabetical order. It uses a list comprehension to get the first letter of each name, converts them to uppercase, and then joins them together to form the society name.

4. **is_isogram(string)**: This function takes a string as input and returns `True` if the string is an isogram (a word with no duplicate letters), and `False` otherwise. It converts the string to lowercase and then checks if the length of the set of characters in the string is equal to the length of the string, which means there are no duplicate letters.

5. **is_in_order(string)**: This function takes a string as input and returns `True` if the characters in the string are in order, and `False` otherwise. It simply checks if the string is equal to the string created by sorting the characters in the original string.