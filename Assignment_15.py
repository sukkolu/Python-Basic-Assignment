1. How many seconds are in an hour?
```python
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)  # Output: 3600
```

2. Assign the result from the previous task (seconds in an hour) to a variable called `seconds_per_hour`.
```python
seconds_per_hour = 3600
```

3. How many seconds do you think there are in a day?
```python
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)  # Output: 86400
```

4. Calculate seconds per day again, but this time save the result in a variable called `seconds_per_day`.
```python
seconds_per_day = 86400
```

5. Divide `seconds_per_day` by `seconds_per_hour` using floating-point (/) division.
```python
result = seconds_per_day / seconds_per_hour
print(result)  # Output: 24.0
```

6. Divide `seconds_per_day` by `seconds_per_hour` using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final `.0`?
```python
result = seconds_per_day // seconds_per_hour
print(result)  # Output: 24
# Yes, the integer division result agrees with the floating-point division, aside from the final ".0".
```

7. Write a generator, `genPrimes`, that returns the sequence of prime numbers on successive calls to its `next()` method: 2, 3, 5, 7, 11, ...
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def genPrimes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Usage
primes_gen = genPrimes()
for _ in range(10):
    print(next(primes_gen))
```
This will output the first 10 prime numbers: `2, 3, 5, 7, 11, 13, 17, 19, 23, 29`.

The `genPrimes()` function is a generator that yields prime numbers one by one. It uses the `is_prime()` helper function to check if a given number is prime or not. The generator starts at 2 and yields the prime numbers as it iterates through the numbers.