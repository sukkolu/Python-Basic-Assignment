1) Difference between enclosing a list comprehension in square brackets and parentheses:
- Enclosing a list comprehension in square brackets `[ ]` creates a list.
- Enclosing a list comprehension in parentheses `( )` creates a generator expression.
- The key difference is that a list is a collection that is fully evaluated and stored in memory, while a generator expression is an iterator that generates values on-the-fly, consuming less memory.

2) Relationship between generators and iterators:
- Generators are a special type of function that use the `yield` keyword to produce a sequence of values, rather than returning a single value.
- Iterators are any object that implements the iterator protocol, which includes the `__iter__()` and `__next__()` methods.
- Generators are a specific type of iterator, where the iterator logic is encapsulated within the generator function.

3) Signs that a function is a generator function:
- The function contains one or more `yield` statements, instead of using the `return` statement.
- The function is defined using the `def` keyword, just like a regular function.
- When called, the function returns a generator object, not a regular value.

4) Purpose of a `yield` statement:
- The `yield` statement is used in generator functions to produce a value and temporarily suspend the function's execution, allowing it to be resumed from where it left off.
- Each time the generator function is called, it resumes from the last `yield` statement and continues until it reaches the next `yield`.
- This allows the generator to produce a sequence of values, one at a time, without having to store the entire sequence in memory.

5) Comparison and contrast between map calls and list comprehensions:
- Both map calls and list comprehensions are used to transform or filter a sequence of data.
- List comprehensions are more concise and readable, as they allow you to express the transformation or filtering in a single expression.
- Map calls require a separate function or lambda expression to perform the transformation, which can be less readable.
- List comprehensions create a new list, while map calls return a map object, which is a type of iterator.
- List comprehensions are generally more efficient for small to medium-sized data sets, while map calls can be more efficient for large data sets, as they don't require creating a new list in memory.

In summary, the key differences are the syntax, the data structure produced (list vs. iterator), and the relative efficiency for different use cases.