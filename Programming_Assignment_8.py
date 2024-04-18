1. Write a Python Program to Add Two Matrices:

```python
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
result = add_matrices(matrix1, matrix2)
print(result)
```

2. Write a Python Program to Multiply Two Matrices:

```python
def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
result = multiply_matrices(matrix1, matrix2)
print(result)
```

3. Write a Python Program to Transpose a Matrix:

```python
def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix(matrix)
print(result)
```

4. Write a Python Program to Sort Words in Alphabetic Order:

```python
def sort_words(text):
    words = text.split()
    words.sort()
    return ' '.join(words)

# Example usage
text = "The quick brown fox jumps over the lazy dog."
result = sort_words(text)
print(result)
```

5. Write a Python Program to Remove Punctuation From a String:

```python
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Example usage
text = "Hello, world! How are you?"
result = remove_punctuation(text)
print(result)
```