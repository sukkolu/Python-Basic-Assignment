1. **Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.**

```python
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def get_divisible_by_seven(self):
        for i in range(0, self.n+1):
            if i % 7 == 0:
                yield i

# Example usage
obj = DivisibleBySeven(100)
for num in obj.get_divisible_by_seven():
    print(num)
```

2. **Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.**

```python
def word_frequency(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the dictionary by keys
    sorted_count = dict(sorted(word_count.items()))
    
    # Print the output
    for word, count in sorted_count.items():
        print(f"{word}:{count}")

# Example usage
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_frequency(text)
```

3. **Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.**

```python
class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

# Example usage
male = Male()
female = Female()
male.getGender()  # Output: Male
female.getGender()  # Output: Female
```

4. **Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey", "Football"].**

```python
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}.")
```

5. **Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".**

```python
import zlib

# Compression
text = "hello world!hello world!hello world!hello world!"
compressed = zlib.compress(text.encode())
print("Compressed data:", compressed)

# Decompression
decompressed = zlib.decompress(compressed).decode()
print("Decompressed data:", decompressed)
```

6. **Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.**

```python
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_list, 7))  # Output: 3
print(binary_search(sorted_list, 8))  # Output: -1
```
