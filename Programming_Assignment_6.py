1. Python Program to Display Fibonacci Sequence Using Recursion:

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

2. Python Program to Find Factorial of Number Using Recursion:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
```

3. Python Program to Calculate Body Mass Index (BMI):

```python
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your Body Mass Index (BMI) is:", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
```

4. Python Program to Calculate the Natural Logarithm of a Number:

```python
import math

num = float(input("Enter a number: "))
result = math.log(num)

print("The natural logarithm of", num, "is", result)
```

5. Python Program for Cube Sum of First n Natural Numbers:

```python
def cube_sum(n):
    if n == 0:
        return 0
    else:
        return n**3 + cube_sum(n-1)

n = int(input("Enter the value of n: "))
result = cube_sum(n)
print("The cube sum of the first", n, "natural numbers is:", result)
```