import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --------- Flash Card Data ---------- #
try:
    words_data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    words_data = pandas.read_csv('./data/french_words.csv')

word_dict = words_data.to_dict(orient='records')

random_word = {}


def pick_random_word():
    global flip, random_word
    window.after_cancel(flip)
    random_word = random.choice(word_dict)
    canvas.itemconfig(card_image, image=card_image_front)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=random_word['French'], fill='black')

    flip = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_image_back)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=random_word['English'], fill='white')


# --------- Remove a word you already remember ---------- #

def word_remembered():
    word_dict.remove(random_word)
    save_data = pandas.DataFrame(word_dict)
    save_data.to_csv('./data/words_to_learn.csv', index=False)
    pick_random_word()
# --------- Create UI ---------- #


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, flip_card)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image_back = PhotoImage(file='./images/card_back.png')
card_image_front = PhotoImage(file='./images/card_front.png')
card_image = canvas.create_image(400,263, image=card_image_front)

language = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_random_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=word_remembered)
right_button.grid(column=1, row=1)

pick_random_word()


window.mainloop()
