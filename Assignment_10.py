1. **How do you distinguish between `shutil.copy()` and `shutil.copytree()`?**
   - `shutil.copy()` is used to copy a single file from one location to another.
   - `shutil.copytree()` is used to copy an entire directory tree (including all files and subdirectories) from one location to another.

2. **What function is used to rename files?**
   - The `os.rename()` function is used to rename files in Python.

3. **What is the difference between the delete functions in the `send2trash` and `shutil` modules?**
   - The `send2trash` module sends files to the system's trash/recycle bin, so they can be easily restored if needed.
   - The `shutil` module's `rmtree()` function permanently deletes the files and directories.

4. **ZipFile objects have a `close()` method just like File objects' `close()` method. What ZipFile method is equivalent to File objects' `open()` method?**
   - The equivalent of the `open()` method for File objects is the `ZipFile()` constructor for ZipFile objects.

5. **Create a program that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.**

```python
import os
import shutil

# Specify the source and destination directories
source_dir = "/path/to/source/directory"
dest_dir = "/path/to/destination/directory"

# Specify the file extension to search for
file_extension = ".pdf"

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Walk through the source directory tree
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(file_extension):
            # Construct the full source and destination paths
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dest_dir, file)
            
            # Copy the file to the destination directory
            shutil.copy2(src_path, dst_path)
            print(f"Copied {file} to {dest_dir}")
```

This program uses the `os.walk()` function to recursively traverse the source directory tree, and the `shutil.copy2()` function to copy any files with the specified file extension to the destination directory.