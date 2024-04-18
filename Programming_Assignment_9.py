1. Check if a number is a Disarium Number:

```python
def is_disarium(num):
    num_str = str(num)
    total = 0
    for i, digit in enumerate(num_str):
        total += int(digit) ** (i + 1)
    return total == num

print(is_disarium(518))  # True
print(is_disarium(466))  # False
print(is_disarium(8))    # True
```

2. Print all Disarium numbers between 1 and 100:

```python
def is_disarium(num):
    num_str = str(num)
    total = 0
    for i, digit in enumerate(num_str):
        total += int(digit) ** (i + 1)
    return total == num

print("Disarium numbers between 1 and 100:")
for i in range(1, 101):
    if is_disarium(i):
        print(i)
```

3. Check if a number is a Happy Number:

```python
def is_happy(num):
    seen = set()
    while num != 1:
        if num in seen:
            return False
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return True

print(is_happy(19))  # True
print(is_happy(7))   # True
print(is_happy(400)) # False
```

4. Print all Happy numbers between 1 and 100:

```python
def is_happy(num):
    seen = set()
    while num != 1:
        if num in seen:
            return False
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return True

print("Happy numbers between 1 and 100:")
for i in range(1, 101):
    if is_happy(i):
        print(i)
```

5. Check if a number is a Harshad Number:

```python
def is_harshad(num):
    num_sum = sum(int(digit) for digit in str(num))
    return num % num_sum == 0

print(is_harshad(18))  # True
print(is_harshad(21))  # True
print(is_harshad(12))  # True
print(is_harshad(6))   # True
print(is_harshad(10))  # True
print(is_harshad(7))   # False
```

6. Print all Pronic numbers between 1 and 100:

```python
def is_pronic(num):
    i = 0
    while i * (i + 1) < num:
        i += 1
    return i * (i + 1) == num

print("Pronic numbers between 1 and 100:")
for i in range(1, 101):
    if is_pronic(i):
        print(i)
```