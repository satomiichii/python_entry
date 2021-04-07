# Day 12 : Guessing Game

Create a game that gives user secret number between 1 - 100 and make user to guess the number. Users can make 10 guesses in easy mode and 5 guesses in hard mode. Each time user make a guess, the app returns a hint that tells the guessed number is either 'Too high' or 'Too low'.

Target behavior: https://replit.com/@appbrewery/guess-the-number-final?embed=1&output=1#main.py

## My Solution

https://github.com/satomiichii/python_entry/blob/master/12_guessing game/script.py

## Today's Takeaway

- Python doesn't have block scope: which means IF statements don't make a local scope. So as JavaScript
- To modify a glocal variable from local scope, you have to use 'global' key. ex)
  ```
    num = 2
    def local ():
        global num
        num = 3
        print(num)
    local()
    print(num)
  ```
- Modifying global variables from local scope is not encouraged to do it.
- Global variables are better for making a global constant, which won't be modified.
- The convention of the name for global constants is all uppercase with underscore. ex) SUNNY_DAY
