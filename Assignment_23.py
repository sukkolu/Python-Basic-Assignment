1. What is the result of the code, and why?
```python
>>> def func(a, b=6, c=8):
    print(a, b, c)

>>> func(1, 2)
```
The output will be:
```
1 2 8
```
This is because the function `func` has three parameters: `a`, `b`, and `c`. When `func(1, 2)` is called, the value `1` is assigned to `a`, the value `2` is assigned to `b`, and the default value `8` is assigned to `c`.

2. What is the result of this code, and why?
```python
>>> def func(a, b, c=5):
    print(a, b, c)

>>> func(1, c=3, b=2)
```
The output will be:
```
1 2 3
```
In this case, the function `func` has three parameters: `a`, `b`, and `c`. When `func(1, c=3, b=2)` is called, the value `1` is assigned to `a`, the value `2` is assigned to `b`, and the value `3` is assigned to `c` because the arguments are passed by keyword.

3. How about this code: what is its result, and why?
```python
>>> def func(a, *pargs):
    print(a, pargs)

>>> func(1, 2, 3)
```
The output will be:
```
1 (2, 3)
```
The `*pargs` parameter in the function `func` allows it to accept an arbitrary number of positional arguments. These arguments are collected into a tuple named `pargs`. In this case, the value `1` is assigned to `a`, and the values `2` and `3` are collected into the `pargs` tuple.

4. What does this code print, and why?
```python
>>> def func(a, **kargs):
    print(a, kargs)

>>> func(a=1, c=3, b=2)
```
The output will be:
```
1 {'c': 3, 'b': 2}
```
The `**kargs` parameter in the function `func` allows it to accept an arbitrary number of keyword arguments. These arguments are collected into a dictionary named `kargs`. In this case, the value `1` is assigned to `a`, and the key-value pairs `'c': 3` and `'b': 2` are collected into the `kargs` dictionary.

5. What gets printed by this, and explain?
```python
>>> def func(a, b, c=8, d=5):
    print(a, b, c, d)

>>> func(1, *(5, 6))
```
The output will be:
```
1 5 6 5
```
In this case, the `*(5, 6)` is used to unpack the tuple `(5, 6)` and assign the values to the `b` and `c` parameters of the `func` function. The value `1` is assigned to `a`, the value `5` is assigned to `b`, the value `6` is assigned to `c`, and the default value `5` is assigned to `d`.

6. What is the result of this, and explain?
```python
>>> def func(a, b, c):
    a = 2
    b[0] = 'x'
    c['a'] = 'y'

>>> l=1; m=[1]; n={'a':0}
>>> func(l, m, n)
>>> l, m, n
```
The output will be:
```
(1, ['x'], {'a': 'y'})
```
In this case:
- The `a` parameter is assigned the value of `l`, which is `1`. However, inside the `func` function, `a` is reassigned to `2`. This does not affect the original `l` value, which remains `1`.
- The `b` parameter is assigned the value of `m`, which is the list `[1]`. Inside the `func` function, the first element of the list is updated to `'x'`, so `m` is now `['x']`.
- The `c` parameter is assigned the value of `n`, which is the dictionary `{'a': 0}`. Inside the `func` function, a new key-value pair `'a': 'y'` is added to the dictionary, so `n` is now `{'a': 'y'}`.

Therefore, the final result is `(1, ['x'], {'a': 'y'})`.