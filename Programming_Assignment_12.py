1. **Write a Python program to Extract Unique values dictionary values?**

```python
def extract_unique_values(dictionary):
    return list(set(dictionary.values()))

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique_values = extract_unique_values(my_dict)
print(unique_values)  # Output: [1, 2, 3]
```

2. **Write a Python program to find the sum of all items in a dictionary?**

```python
def sum_dictionary_values(dictionary):
    return sum(dictionary.values())

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
total_sum = sum_dictionary_values(my_dict)
print(total_sum)  # Output: 15
```

3. **Write a Python program to Merging two Dictionaries?**

```python
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

4. **Write a Python program to convert key-values list to flat dictionary?**

```python
def list_to_dictionary(key_value_list):
    return {key: value for key, value in key_value_list}

# Example usage
key_value_pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = list_to_dictionary(key_value_pairs)
print(flat_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

5. **Write a Python program to insertion at the beginning in OrderedDict?**

```python
from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    ordered_dict = OrderedDict([(key, value)] + list(ordered_dict.items()))
    return ordered_dict

# Example usage
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
updated_dict = insert_at_beginning(my_dict, 'x', 4)
print(updated_dict)  # Output: OrderedDict([('x', 4), ('a', 1), ('b', 2), ('c', 3)])
```

6. **Write a Python program to check order of character in string using OrderedDict()?**

```python
from collections import OrderedDict

def check_character_order(string):
    char_count = OrderedDict()
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
my_string = "Hello World"
char_order = check_character_order(my_string)
print(char_order)  # Output: OrderedDict([('H', 1), ('e', 1), ('l', 3), ('o', 2), (' ', 1), ('W', 1), ('r', 1), ('d', 1)])
```

7. **Write a Python program to sort Python Dictionaries by Key or Value?**

```python
def sort_dictionary_by_key(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[0]))

def sort_dictionary_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

# Example usage
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_by_key = sort_dictionary_by_key(my_dict)
print(sorted_by_key)  # Output: {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_by_value = sort_dictionary_by_value(my_dict)
print(sorted_by_value)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3, 'date': 4}
```