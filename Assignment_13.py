1. Advantages of Excel spreadsheets over CSV spreadsheets:
- Excel spreadsheets can store more data types, such as formulas, charts, and formatting. CSV files are limited to just plain text data.
- Excel spreadsheets provide more features and functionality for data analysis, visualization, and manipulation.
- Excel has built-in functions and tools that make it easier to work with and analyze data.
- Excel files can be password-protected and have other security features, while CSV files are just plain text.

2. To create reader and writer objects, you pass the following to `csv.reader()` and `csv.writer()`:
- `csv.reader(file_obj)`: You pass the file object of the CSV file you want to read from.
- `csv.writer(file_obj)`: You pass the file object of the CSV file you want to write to.

3. File objects for reader and writer objects need to be opened in the following modes:
- For reading: `'r'` (read mode)
- For writing: `'w'` (write mode)

4. The `writerow()` method of the `csv.writer` object takes a list argument and writes it as a row to the CSV file.

5. The `delimiter` keyword argument specifies the character used to separate values in each row (default is a comma `,`). 
The `lineterminator` keyword argument specifies the character(s) used to terminate each row (default is a newline `\n`).

6. The `json.loads()` function takes a string of JSON data and returns a Python data structure (e.g. dict, list, etc.).

7. The `json.dumps()` function takes a Python data structure and returns a string of JSON data.