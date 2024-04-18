
**Question 1**:
```python
def amplify(num):
    result = []
    for i in range(1, num+1):
        if i % 4 == 0:
            result.append(i * 10)
        else:
            result.append(i)
    return result
```

**Question 2**:
```python
def unique(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
```

**Question 3**:
```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return round(math.pi * self.radius ** 2)
        
    def getPerimeter(self):
        return round(2 * math.pi * self.radius)
```

**Question 4**:
```python
def sort_by_length(lst):
    return sorted(lst, key=len)
```

**Question 5**:
```python
def is_triplet(a, b, c):
    # Find the largest number
    largest = max(a, b, c)
    
    # Check if the sum of squares of the two smallest numbers
    # is equal to the square of the largest number
    return a**2 + b**2 == largest**2 or \
           a**2 + c**2 == largest**2 or \
           b**2 + c**2 == largest**2
```