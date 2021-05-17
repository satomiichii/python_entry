from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler!')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150,
                                                 125,
                                                 width=280,
                                                 text='Quiz text here',
                                                 font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score = Label(text='Score:0', bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score.grid(column=1, row=0)
        check_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=check_image, highlightthickness=0, command=lambda: self.check_answer('True'))
        self.right_button.grid(column=0, row=2)
        cross_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=cross_image, highlightthickness=0, command=lambda: self.check_answer('False'))
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.right_button.config(state='disable')
            self.wrong_button.config(state='disable')

    def check_answer(self, answer):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)
