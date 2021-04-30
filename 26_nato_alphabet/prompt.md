# Day 26 : NATO Alphabet

Create a program that takes user's string input and print the corresponding words to each phonetic letter in the string.
Use list/dict comprehension and csv manipulation with pandas.

## My Solution

https://github.com/satomiichii/python_entry/blob/master/26_nato_alphabet/script.py

## Today's Takeaway

- List Comprehension > generate a new list by using the items from other sequences.

```buildoutcfg
new_list = [new_item for item in original_list]

numbers = [1, 2, 3]
new_numbers  = [n + 1 for n in numbers] >> [2, 3, 4]
nums = [n * 2 for n in range(1, 5)] >> [2, 4, 6, 8]

#list comprehension with condition
#only elements that meets the condition will be in the new list
names = ['Otamaboya', 'sato', 'Nekonekofantasia']
long_names = [name.upper() for name in names if len(name) >= 5]
```

- Python sequences
  list, range, tuple, string
  
- Dictionary comprehension > generate a new dictionary by using the key/value pair from other dictionaries or using the element in the other list
```buildoutcfg
#generate a dict out of list
new_dictionary = {item: new_value for item in original_list }

names = ['Tama', 'Sato', 'Neko']
import random
student_score = {student:random.randint(1,100) for student in names}
# student_score >> {'Tama': 56, 'Sato': 30, 'Neko': 100}

new_dictionary = {new_key:new_item for (key, value) in original_dictionary.items()}
```
- Pandas method data_frame.iterrows() will loop through the data frame by row
```buildoutcfg
for (index, row) in data_frame.iterrows():
    print(row)
```
