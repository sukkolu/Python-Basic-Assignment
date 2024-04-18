1. A relative path refers to the location of a file or directory relative to the current working directory. It does not start with the root directory.

2. An absolute path starts with the root directory of your operating system, such as `C:\` on Windows or `/` on Unix-based systems.

3. `os.getcwd()` returns the current working directory, while `os.chdir()` changes the current working directory.

4. `.` represents the current directory, and `..` represents the parent directory.

5. In the path `C:\bacon\eggs\spam.txt`, the directory name is `C:\bacon\eggs`, and the base name is `spam.txt`.

6. The three mode arguments that can be passed to the `open()` function are:
   - `'r'` (read mode)
   - `'w'` (write mode)
   - `'a'` (append mode)

7. If an existing file is opened in write mode (`'w'`), the file's contents are truncated (deleted) before the file is opened.

8. The main difference between `read()` and `readlines()` is that `read()` reads the entire file (or a specified number of bytes) as a single string, while `readlines()` reads the file line by line and returns a list of strings, where each string represents a line.

9. A shelf value resembles a dictionary data structure. A shelf is a persistent dictionary-like object, which means that its contents are stored in a file and can be accessed even after the program has been closed and reopened.