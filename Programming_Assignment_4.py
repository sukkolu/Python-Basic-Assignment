1. Write a Python Program to Find the Factorial of a Number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
```

2. Write a Python Program to Display the multiplication Table:

```python
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
```

3. Write a Python Program to Print the Fibonacci sequence:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
```

4. Write a Python Program to Check Armstrong Number:

```python
num = int(input("Enter a number: "))
original_num = num
result = 0
while num > 0:
    digit = num % 10
    result += digit ** len(str(original_num))
    num //= 10

if original_num == result:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")
```

5. Write a Python Program to Find Armstrong Number in an Interval:

```python
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print("Armstrong numbers in the given interval are:")
for num in range(start, end+1):
    original_num = num
    result = 0
    while num > 0:
        digit = num % 10
        result += digit ** len(str(original_num))
        num //= 10
    if original_num == result:
        print(original_num)
```

6. Write a Python Program to Find the Sum of Natural Numbers:

```python
num = int(input("Enter a number: "))
sum_of_numbers = (num * (num + 1)) // 2
print(f"The sum of first {num} natural numbers is {sum_of_numbers}")
```