from tkinter import *

FONT = ('Arial', 16)

window = Tk()
window.title('My first GUI program')
window.minsize(width=300, height=200)
window.config(padx=50, pady=55)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles = Label(text='Miles', font=FONT)
miles.grid(column=2, row=0)

equal = Label(text='is equal to', font=FONT)
equal.grid(column=0, row=1)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)

km = Label(text='Km', font=FONT)
km.grid(column=2, row=1)


def calc():
    kilometers = round(float(miles_input.get()) * 1.6, 1)
    result.config(text=kilometers)


button = Button(text='Calculate', command=calc)
button.grid(column=1, row=2)

# def button_click():
#     user_input = my_input.get()
#     my_label.config(text=user_input)
#
#
# my_button = Button(command=button_click)
# my_button.config(text='click me!')
# my_button.grid(column=1, row=1)
#
# my_input = Entry()
# my_input.config(width=10)
# my_input.grid(column=4, row=3)
#
# button_second = Button(text='new button!')
# button_second.grid(column=2, row=0)


window.mainloop()
