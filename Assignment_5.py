1. An empty dictionary's code looks like this: `{}`.

2. The value of a dictionary with the key 'foo' and the value 42 is `42`.

3. The most significant distinction between a dictionary and a list is that a dictionary is an unordered collection of key-value pairs, while a list is an ordered collection of elements.

4. If you try to access `spam['foo']` when `spam` is `{'bar': 100}`, you will get a `KeyError` exception, as the key 'foo' does not exist in the dictionary.

5. The expression `'cat' in spam` checks if the string 'cat' is a key in the dictionary `spam`, while `'cat' in spam.keys()` does the same thing, but explicitly checks the dictionary's keys.

6. The expression `'cat' in spam` checks if the string 'cat' is a key in the dictionary `spam`, while `'cat' in spam.values()` checks if the string 'cat' is a value in the dictionary.

7. The shortcut for the following code:

   ```python
   if 'color' not in spam:
       spam['color'] = 'black'
   ```

   is `spam.setdefault('color', 'black')`.

8. To "pretty print" dictionary values, you can use the `pprint` module and its `pprint()` function. For example:

   ```python
   import pprint
   my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
   pprint.pprint(my_dict)
   ```

   This will output the dictionary in a more readable format:

   ```
   {'age': 30, 'city': 'New York', 'name': 'Alice'}
   ```