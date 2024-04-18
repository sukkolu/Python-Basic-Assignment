
```python
import os
import time
import random
from datetime import date, datetime
import multiprocessing

# 1. Add the current date to the text file today.txt as a string.
with open("today.txt", "w") as file:
    file.write(str(date.today()))

# 2. Read the text file today.txt into the string today_string
with open("today.txt", "r") as file:
    today_string = file.read()

# 3. Parse the date from today_string.
today = datetime.strptime(today_string, "%Y-%m-%d").date()

# 4. List the files in your current directory
print("Files in current directory:")
for filename in os.listdir():
    print(filename)

# 5. Create a list of all of the files in your parent directory (minimum five files should be available)
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("\nFiles in parent directory:")
parent_files = os.listdir(parent_dir)
for filename in parent_files[:5]:
    print(filename)

# 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
def worker():
    wait_time = random.uniform(1, 5)
    time.sleep(wait_time)
    print(f"Current time: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

# 7. Create a date object of your day of birth.
your_birthdate = date(1990, 5, 15)

# 8. What day of the week was your day of birth?
weekday_name = your_birthdate.strftime('%A')
print(f"Your day of birth was a {weekday_name}.")

# 9. When will you be (or when were you) 10,000 days old?
days_old = (date.today() - your_birthdate).days
ten_thousand_days = your_birthdate + datetime.timedelta(days=10000)
print(f"You will be 10,000 days old on {ten_thousand_days.strftime('%B %d, %Y')}.")
```

This solution addresses all the requirements of the Python question:

1. Adds the current date to the `today.txt` file as a string.
2. Reads the `today.txt` file and parses the date from the string.
3. Lists the files in the current directory.
4. Creates a list of the first 5 files in the parent directory.
5. Uses multiprocessing to create 3 separate processes, each of which waits a random number of seconds between 1 and 5, prints the current time, and then exits.
6. Creates a date object for the day of birth.
7. Prints the day of the week for the day of birth.
8. Calculates when the person will be (or was) 10,000 days old.