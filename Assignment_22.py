1. What is the result of the code, and explain?

```python
>>> X = 'iNeuron'
>>> def func():
    print(X)
>>> func()
```

Output: `iNeuron`

Explanation:
- The variable `X` is defined in the global scope and has the value `'iNeuron'`.
- The function `func()` simply prints the value of `X`, which is the global variable.
- When `func()` is called, it prints the value of the global variable `X`, which is `'iNeuron'`.

2. What is the result of the code, and explain?

```python
>>> X = 'iNeuron'
>>> def func():
    X = 'NI!'
>>> func()
>>> print(X)
```

Output: `iNeuron`

Explanation:
- The variable `X` is defined in the global scope and has the value `'iNeuron'`.
- The function `func()` defines a local variable `X` and assigns it the value `'NI!'`.
- When `func()` is called, it modifies the local `X` variable, but it does not affect the global `X` variable.
- After `func()` is called, the `print(X)` statement still prints the global `X` variable, which is `'iNeuron'`.

3. What does this code print, and why?

```python
>>> X = 'iNeuron'
>>> def func():
    X = 'NI'
    print(X)
>>> func()
>>> print(X)
```

Output:
```
NI
iNeuron
```

Explanation:
- The variable `X` is defined in the global scope and has the value `'iNeuron'`.
- The function `func()` defines a local variable `X` and assigns it the value `'NI'`. It then prints the value of this local `X`.
- When `func()` is called, it prints the value of the local `X`, which is `'NI'`.
- After `func()` is called, the `print(X)` statement prints the value of the global `X`, which is `'iNeuron'`.

4. What output does this code produce? Why?

```python
>>> X = 'iNeuron'
>>> def func():
    global X
    X = 'NI'
>>> func()
>>> print(X)
```

Output: `NI`

Explanation:
- The variable `X` is defined in the global scope and has the value `'iNeuron'`.
- The function `func()` uses the `global` keyword to access the global `X` variable. It then assigns the value `'NI'` to the global `X`.
- When `func()` is called, it modifies the global `X` variable.
- After `func()` is called, the `print(X)` statement prints the new value of the global `X`, which is `'NI'`.

5. What about this code---what's the output, and why?

```python
>>> X = 'iNeuron'
>>> def func():
    X = 'NI'
    def nested():
        print(X)
    nested()
>>> func()
>>> X
```

Output:
```
NI
'iNeuron'
```

Explanation:
- The variable `X` is defined in the global scope and has the value `'iNeuron'`.
- The function `func()` defines a local variable `X` and assigns it the value `'NI'`. It then defines a nested function `nested()`, which prints the value of `X`.
- When `func()` is called, it executes the `nested()` function, which prints the value of the local `X`, which is `'NI'`.
- After `func()` is called, the expression `X` evaluates to the global `X`, which is still `'iNeuron'`.

6. How about this code: what is its output in Python 3, and explain?

```python
>>> def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)
>>> func()
```

Output:
```
Spam
```

Explanation:
- The function `func()` defines a local variable `X` and assigns it the value `'NI'`. It then defines a nested function `nested()`.
- Inside `nested()`, the `nonlocal` keyword is used to access the local `X` variable from the enclosing `func()` scope.
- The nested function `nested()` then assigns the value `'Spam'` to the local `X` variable from the `func()` scope.
- When `func()` is called, it executes the `nested()` function, which modifies the local `X` variable from the `func()` scope.
- Finally, `print(X)` inside `func()` prints the updated value of `X`, which is `'Spam'`.

