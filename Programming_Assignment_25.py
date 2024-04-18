
Question1:
```python
def equal(a, b, c):
    count = 0
    if a == b == c:
        count = 3
    elif a == b or b == c or a == c:
        count = 2
    return count
```

Question2:
```python
def dict_to_list(dictionary):
    return sorted(list(dictionary.items()), key=lambda x: x[0])
```

Question3:
```python
def mapping(letters):
    return {letter: letter.upper() for letter in letters}
```

Question4:
```python
def vow_replace(string, vowel):
    return ''.join(vowel if char in 'aeiou' else char for char in string)
```

Question5:
```python
def ascii_capitalize(string):
    result = ''
    for char in string:
        if char.isalpha():
            if ord(char) % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result
```