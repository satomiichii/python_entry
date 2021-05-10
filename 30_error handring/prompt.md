# Day 30 : Error and Exception handling

## My solution

## Today's Takeaway

- try, except, else, finally
```buildoutcfg
try:
    Do this first. This might cause some error
except ErrorType:
    If the code in the try block cause the specified type error, then do this.
else:
    If the code in the try block is excuted without error, do this.
finally:
    Do this no matter what happenes
```
- You can have multiple except clause, but only the first except clause is called when multiple error occur
- raise error = throw error
```buildoutcfg
raise error_type('This is the error raised')
>> in the console >> error_type:This is the error raised
```
- If you can handle the potential error with if/else statement, you should do it with them instead of using try/except