1. Write a Python Program to Find LCM:

```python
def find_lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
```

2. Write a Python Program to Find HCF:

```python
def find_hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    while smaller != 0:
        temp = num2 % num1
        num1 = num2
        num2 = temp
        smaller = temp

    return num1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The HCF of", num1, "and", num2, "is", find_hcf(num1, num2))
```

3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal:

```python
decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("The binary representation is:", binary)
print("The octal representation is:", octal)
print("The hexadecimal representation is:", hexadecimal)
```

4. Write a Python Program To Find ASCII value of a character:

```python
char = input("Enter a character: ")
ascii_value = ord(char)
print("The ASCII value of", char, "is", ascii_value)
```

5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations:

```python
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid input")

calculator()
```