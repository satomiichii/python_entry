# Day 34 : Quiz App

Create a GUI quiz App by using Trivia API

## My Solution

https://github.com/satomiichii/python_entry/blob/master/34_quiz_app/main.py

## Today's Takeaway

- If you want to call other class's method in the class, you can pass the other class as an argument
```buildoutcfg
class OriginalClass:
    def __init__(self):
        self.name = 'This is the original class'
    
    def get_name:
        return self.name

class SecondClass:
    def __init__(self, original : OriginalClass) >> after : is optional
        self.original = original
        self.name = 'This is the second class'
    
    def get_name:
        print(self.original.get_name()) >> 'This is the original class'
        
```
- You can specify the data type of arguments
```buildoutcfg
def check_age(age : int):  >> Only int type can be passed
    if age > 12:
        print('You can go to school without gardian)
        return True
    else:
        print('You need gardian to go to school)
        return False
```
- You can also specify the output of the function
```buildoutcfg
def check_age(age : int) -> bool:
    if age > 12:
        print('You can go to school without gardian)
        return True
    else:
        print('You need gardian to go to school)
        return False
```
- The concept above is called 'Type Hints'