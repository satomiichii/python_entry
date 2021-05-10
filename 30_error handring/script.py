# import pandas

# Modify Nato alphabet program to catch invalid input like number.

# data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
#
# def nato_converter():
#     try:
#         user_input = input('Enter a word: ').upper()
#         code_list = [data_dict[letter] for letter in user_input]
#     except KeyError:
#         print('Sorry, only letters in alphabet please.')
#         nato_converter()
#     else:
#         print(code_list)
#
#
# nato_converter()


# Modify Password manager
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_letter = [random.choice(letters) for _ in range(8, 11)]
    password_number = [random.choice(numbers) for _ in range(2, 5)]
    password_symbol = [random.choice(symbols) for _ in range(2, 5)]

    password_list = password_letter + password_number + password_symbol

    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    pass_input.insert(0, generated_password)

    pyperclip.copy(generated_password)

# ---------------------------- SEARCH INFO ------------------------------- #


def search_info():
    site_name = site_input.get()
    if len(site_name) == 0:
        messagebox.showerror(title='Empty field', message='Please input site name to search.')
    else:
        try:
            with open('data.json', mode='r') as data:
                existing_data = json.load(data)

        except FileNotFoundError:
            messagebox.showerror(title='File not found', message='No data file found.')

        else:
            if site_name in existing_data:
                info_detail = existing_data[site_name]
                messagebox.showinfo(title=site_name, message=f'email: {info_detail["email"]}\n'
                                                             f'password: {info_detail["password"]}')
            else:
                messagebox.showerror(title=site_name, message='No password for the website found.')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = site_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}

    if website == '' or email == '' or password == '':
        messagebox.showinfo(title='Empty field', message="Don't leave any field empty.")
    else:
        try:
            with open('data.json', mode='r') as data:
                file_data = json.load(data)
        except FileNotFoundError:
            with open('data.json', mode='w') as data:
                json.dump(new_data, data, indent=4)
        else:
            file_data.update(new_data)
            with open('data.json', mode='w') as data:
                json.dump(file_data, data, indent=4)
        finally:
            site_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 98, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
site_label = Label(text='Website:')
site_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

# Inputs
site_input = Entry(width=21)
site_input.focus()
site_input.grid(column=1, row=1)

email_input = Entry(width=35)
email_input.insert(0, 'test@email.com')
email_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

# Buttons
pass_button = Button(text='Generate password', command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=14, command=search_info)
search_button.grid(column=2, row=1)

window.mainloop()
