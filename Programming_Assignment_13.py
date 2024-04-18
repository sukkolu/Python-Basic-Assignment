Question 1:
```python
import math

C = 50
H = 30

def calculate_Q(D_values):
    result = []
    for D in D_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(int(Q))
    return result

D_values = [int(x) for x in input("Enter comma-separated D values: ").split(",")]
print(", ".join(map(str, calculate_Q(D_values))))
```

Question 2:
```python
X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

arr = [[i * j for j in range(Y)] for i in range(X)]
print(arr)
```

Question 3:
```python
words = input("Enter comma-separated words: ").split(",")
print(",".join(sorted(words)))
```

Question 4:
```python
words = input("Enter whitespace-separated words: ").split()
unique_words = sorted(set(words))
print(" ".join(unique_words))
```

Question 5:
```python
sentence = input("Enter a sentence: ")
letters = 0
digits = 0
for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("LETTERS", letters)
print("DIGITS", digits)
```

Question 6:
```python
import re

def validate_password(passwords):
    valid_passwords = []
    for password in passwords:
        if (
            len(password) >= 6
            and len(password) <= 12
            and any(char.isalpha() and char.islower() for char in password)
            and any(char.isalpha() and char.isupper() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in "$#@" for char in password)
        ):
            valid_passwords.append(password)
    return valid_passwords

passwords = input("Enter comma-separated passwords: ").split(",")
valid_passwords = validate_password(passwords)
print(",".join(valid_passwords))
```