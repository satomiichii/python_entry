# Day 5: Password Generator

Imprement a password generator that returns a random set of letters, numbers, and symbols based on the user's preference for each category.

ex.

User's preference:
number of letters > 3
number of numbers > 2
number of symbols > 1

Your password is: Ne2!l9

## My Solution

https://github.com/satomiichii/python_entry/blob/master/05_password_generator/script.py

## Today's Takeaway

- sum(list) = arr.reduce(acm, elm => acm + elm, 0)
- max(list) = Math.max(arr)
- min(list) = Math.min(arr)
- You can create for loop like the syntax below:
  for elm in list: or
  for num in range(1,101,2)
- range() option allows you to loop through the number stats from the first argument and end with the second argument - 1 (the num it self isn't include. like for (let i = 1; i < 101; i++))
  The third argument defince how much to increment the num for each loop like i++ i += 2 etc.
- random.shuffle(list) > returns a list with the element from original list with shuffled order.
- ''.join(list) = arr.join('')
- random.sample(initial_sequence, list length) > returns a list of the number (lest length) of elements that randomly picked from the initial_sequence(like string).
