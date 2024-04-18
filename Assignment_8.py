1. No, the Python Standard Library is not included with PyInputPlus. PyInputPlus is a separate library that provides additional functionality beyond the built-in input() function in Python.

2. PyInputPlus is commonly imported as `import pyinputplus as pypi` to provide a more concise and convenient way to use the library's functions, such as `pypi.inputInt()` instead of `pyinputplus.inputInt()`.

3. The main distinction between `inputInt()` and `inputFloat()` is that `inputInt()` expects and returns an integer value, while `inputFloat()` expects and returns a floating-point value.

4. To ensure that the user enters a whole number between 0 and 99 using PyInputPlus, you can use the `inputInt()` function with the `min` and `max` keyword arguments:

```python
import pyinputplus as pypi

user_input = pypi.inputInt(min=0, max=99)
```

5. The `allowRegexes` and `blockRegexes` keyword arguments in PyInputPlus functions accept regular expression patterns. `allowRegexes` specifies a list of patterns that are allowed as valid input, while `blockRegexes` specifies a list of patterns that are not allowed as valid input.

6. If blank input is entered three times with `inputStr(limit=3)`, the function will raise a `RetryLimitException` because the default behavior is to raise an exception when the retry limit is reached.

7. If blank input is entered three times with `inputStr(limit=3, default='hello')`, the function will return the specified default value of `'hello'` instead of raising an exception, as the `default` keyword argument provides a fallback value.