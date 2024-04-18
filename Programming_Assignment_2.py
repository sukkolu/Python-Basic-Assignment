1. Python program to convert kilometers to miles:

```python
kilometers = float(input("Enter the distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")
```

2. Python program to convert Celsius to Fahrenheit:

```python
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
```

3. Python program to display calendar:

```python
import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(calendar.month(year, month))
```

4. Python program to solve quadratic equation:

```python
import math

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The root of the quadratic equation is: {root}")
else:
    print("The equation has no real roots.")
```

5. Python program to swap two variables without temp variable:

```python
a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))

print(f"Before swapping: a = {a} and b = {b}")

a, b = b, a

print(f"After swapping: a = {a} and b = {b}")
```