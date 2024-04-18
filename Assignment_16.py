1. Create a list called `years_list`, starting with the year of your birth, and each year thereafter until the year of your fifth birthday.

```python
years_list = [1990, 1991, 1992, 1993, 1994, 1995]  # Assuming you were born in 1990
```

2. In which year in `years_list` was your third birthday? Remember, you were 0 years of age for your first year.

Your third birthday was in 1992, since you were 0 years old in 1990, 1 year old in 1991, and 2 years old in 1992.

3. In the `years_list`, which year were you the oldest?

In the `years_list`, the year you were the oldest was 1995, since that was the year of your fifth birthday.

4. Make a list called `things` with these three strings as elements: "mozzarella", "cinderella", and "salmonella".

```python
things = ["mozzarella", "cinderella", "salmonella"]
```

5. Capitalize the element in `things` that refers to a person and then print the list. Did it change the element in the list?

```python
things = ["mozzarella", "Cinderella", "salmonella"]
print(things)
```

Yes, the element in the list was changed.

6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

```python
surprise_list = ["Groucho", "Chico", "Harpo"]
```

7. Lowercase the last element of the `surprise_list`, reverse it, and then capitalize it.

```python
surprise_list = ["Groucho", "Chico", "oprAH"]
```

8. Make an English-to-French dictionary called `e2f` and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

```python
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)
```

9. Write the French word for walrus in your three-word dictionary `e2f`.

The French word for walrus in `e2f` is "morse".

10. Make a French-to-English dictionary called `f2e` from `e2f`. Use the `items()` method.

```python
f2e = {v: k for k, v in e2f.items()}
```

11. Print the English version of the French word `chien` using `f2e`.

```python
print(f2e["chien"])
```

12. Make and print a set of English words from the keys in `e2f`.

```python
english_words = set(e2f.keys())
print(english_words)
```

13. Make a multilevel dictionary called `life`. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

```python
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {}
    },
    "plants": {},
    "other": {}
}
```

14. Print the top-level keys of `life`.

```python
print(list(life.keys()))
```

15. Print the keys for `life['animals']`.

```python
print(list(life["animals"].keys()))
```

16. Print the values for `life['animals']['cats']`.

```python
print(life["animals"]["cats"])
```