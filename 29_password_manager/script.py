from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = site_input.get()
    email = email_input.get()
    password = pass_input.get()
    info_to_add = f'{website} | {email} | {password}\n'

    can_save = False

    if website == '' or email == '' or password == '':
        messagebox.showinfo(title='Empty field', message="Don't leave any field empty.")
    else:
        can_save = messagebox.askokcancel(title=website, message=f'There are the details entered:'
                                                                 f'\nEmail: {email}\nPassword: {password}\n'
                                                                 f'Is it ok to save?')
    if can_save:
        with open('./data.txt', mode='a') as data:
            data.write(info_to_add)
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
site_input = Entry(width=35)
site_input.focus()
site_input.grid(column=1, row=1, columnspan=2)

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

window.mainloop()
