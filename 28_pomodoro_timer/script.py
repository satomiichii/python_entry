import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_mark.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(num):
    global timer
    num_min = math.floor(num / 60)
    num_sec = num % 60
    if num_sec < 10:
        num_sec = f'0{num_sec}'
    canvas.itemconfig(timer_text, text=f"{num_min}:{num_sec}")
    if num > 0:
        timer = window.after(1000, count_down, num - 1)
    else:
        check_str = ''
        for n in range(math.floor(reps / 2)):
            check_str += '✓'
        check_mark.config(text=check_str)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0)

tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
