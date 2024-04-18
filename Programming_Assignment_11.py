1. Write a Python program to find words which are greater than given length k?

```python
def find_long_words(text, k):
    words = text.split()
    long_words = [word for word in words if len(word) > k]
    return long_words

# Example usage
text = "The quick brown fox jumps over the lazy dog"
k = 4
print(find_long_words(text, k))  # Output: ['quick', 'brown', 'jumps', 'over', 'lazy']
```

2. Write a Python program for removing i-th character from a string?

```python
def remove_char(string, i):
    return string[:i] + string[i+1:]

# Example usage
string = "Hello, world!"
i = 7
print(remove_char(string, i))  # Output: "Hello, orld!"
```

3. Write a Python program to split and join a string?

```python
def split_and_join(string, separator):
    words = string.split(separator)
    joined_string = separator.join(words)
    return words, joined_string

# Example usage
string = "Hello-world-Python"
separator = "-"
print(split_and_join(string, separator))
# Output: (['Hello', 'world', 'Python'], 'Hello-world-Python')
```

4. Write a Python to check if a given string is binary string or not?

```python
def is_binary_string(string):
    for char in string:
        if char not in ['0', '1']:
            return False
    return True

# Example usage
print(is_binary_string("10101010"))  # Output: True
print(is_binary_string("101010101a"))  # Output: False
```

5. Write a Python program to find uncommon words from two Strings?

```python
def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    uncommon_words = (words1 ^ words2)
    return list(uncommon_words)

# Example usage
string1 = "apple banana cherry"
string2 = "banana orange grape"
print(find_uncommon_words(string1, string2))  # Output: ['apple', 'cherry', 'grape', 'orange']
```

6. Write a Python to find all duplicate characters in string?

```python
def find_duplicate_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    duplicate_chars = [char for char, count in char_count.items() if count > 1]
    return duplicate_chars

# Example usage
print(find_duplicate_chars("Hello, world!"))  # Output: [',', 'l', 'o']
```

7. Write a Python Program to check if a string contains any special character?

```python
import re

def has_special_char(string):
    pattern = r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]'
    if re.search(pattern, string):
        return True
    else:
        return False

# Example usage
print(has_special_char("Hello, world!"))  # Output: True
print(has_special_char("Helloworld"))  # Output: False
```