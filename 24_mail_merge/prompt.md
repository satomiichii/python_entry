# Day 24 : Mail Merge Project

Write a program that generate invitation letters for the people on the guest list.
Each letter has to be individual file and has to have guest's name on it.

## My Solution

https://github.com/satomiichii/python_entry/blob/master/24_mail_merge/Mail%20Merge%20Project%20Start/main.py

## Today's Takeaway

- To access a file with in the same directory.
```buildoutcfg
# If you only pass file name as a argument, the file mode will be read only
with open('file_name.txt') as file:
    content = file.read()
    
# mode='w' will overwrite the contents of the file.
with open('file_name.txt', mode='w') as file:
    file.write('this will overwrite the contents in the file')

# mode='a' will append the content to the original contents in the file.
with open('file_name.txt', mode='a') as file:
    file.write(\nThis will be appended to the original contents in the file.')
```

- Absolute pass / Relative pass 
- with 'w' mode, you can create new file if it doesn't exist yet
- str.replace('original_word', 'the word that you want to replace with')
- file.readlines() extract all the line of the file and store them as list
- str.strip() remove all the white space around the string