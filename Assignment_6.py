1. Escape characters are special characters that are used to represent characters that are difficult or impossible to type directly. They are represented by a backslash (`\`) followed by a specific character. For example, `\n` represents a newline character, `\t` represents a tab character, and `\"` represents a double quote character.

2. The escape characters `\n` and `\t` stand for newline and tab, respectively.

3. To include a backslash character in a string, you need to use the escape character `\\`. For example, `"C:\\Users\\username\\Documents"`.

4. The single quote character in the word `Howl's` is not a problem because the string is enclosed in double quotes (`"`). The single quote is not interpreted as the end of the string.

5. To include a string of newlines without using the `\n` character, you can use the triple-quote syntax (`"""` or `'''`). For example:

```python
multiline_string = """
This is a
multi-line
string.
"""
```

6. The values of the given expressions are:

```python
'Hello, world!'[1]  # 'e'
'Hello, world!'[0:5]  # 'Hello'
'Hello, world!'[:5]  # 'Hello'
'Hello, world!'[3:]  # 'lo, world!'
```

7. The values of the given expressions are:

```python
'Hello'.upper()  # 'HELLO'
'Hello'.upper().isupper()  # True
'Hello'.upper().lower()  # 'hello'
```

8. The values of the given expressions are:

```python
'Remember, remember, the fifth of July.'.split()  # ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
'-'.join('There can only one.'.split())  # 'There-can-only-one.'
```

9. The methods for right-justifying, left-justifying, and centering a string are:

```python
# Right-justifying
'hello'.rjust(10)  # '     hello'

# Left-justifying
'hello'.ljust(10)  # 'hello     '

# Centering
'hello'.center(10)  # '   hello  '
```

10. The best way to remove whitespace characters from the start or end of a string is to use the `strip()` method. For example:

```python
'   hello   '.strip()  # 'hello'
```