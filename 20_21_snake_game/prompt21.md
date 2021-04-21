# Day 21 : Snake Game Part2

Create a snake game with the Python turtle module.
For part1, implement the following features.

- Detect collision with food
- Create a score board
- Detect collision with wall
- Detect collision with tail

## My Solution

https://github.com/satomiichii/python_entry/blob/master/20_21_snake_game/script.py

## Today's Takeaway

- Class inheritance syntax
```buildoutcfg
class ClassName (SuperClass_Name):
    def __init__(self):
        # set same attribute that SuperClass has.
        super().__init__()
    
    def SuperClass_Function_Name(self):
        # inherit the functionarity from SuperClass
        super().SuperClass_Function_Name()
        # Add child class original functionarity
        print('this is only for child class)x
        
        
```
- You can access the last element in a list with list[-1]
- To slice a list or tuple > list[startIdx: endIdx: steps]
```buildoutcfg
my_list = ['a', 'b', 'c', 'd', 'e']
print (my_list[1:3]) >> ['b','c']
```
