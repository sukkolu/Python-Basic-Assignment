
1. **Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.**

```python
def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    lst.append(num)
    return lst[1:]
```

2. **Create the function that takes a list of dictionaries and returns the sum of people's budgets.**

```python
def get_budgets(people):
    total_budget = 0
    for person in people:
        total_budget += person["budget"]
    return total_budget
```

3. **Create a function that takes a string and returns a string with its letters in alphabetical order.**

```python
def alphabet_soup(string):
    return ''.join(sorted(string))
```

4. **Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. What will be the value of your investment at the end of the 10 year period? Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.**

```python
import math

def compound_interest(p, t, r, n):
    return round(p * (1 + r/n)**(n*t), 2)
```

5. **Write a function that takes a list of elements and returns only the integers.**

```python
def return_only_integer(lst):
    return [item for item in lst if isinstance(item, int)]
```
