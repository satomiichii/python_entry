import turtle
import pandas

IMAGE = 'blank_states_img.gif'
STATE = 'state'
X = 'x'
Y = 'y'

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(700, 550)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv('50_states.csv')
state_list = data[STATE].tolist()

score = 0


def check_answer(user_answer):
    state_name = user_answer.title()

    if state_name in state_list:
        state_list.remove(state_name)
        state_x = float(data[data[STATE] == state_name][X])
        state_y = float(data[data[STATE] == state_name][Y])
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(state_x, state_y)
        new_state.write(state_name, align='left', font=('Arial', 10, 'normal'))
        return True


while len(state_list) > 0:
    answer = screen.textinput(title=f'{score}/50 States correct',
                              prompt="What's another state's name?")

    if answer == 'exit':
        new_data = pandas.DataFrame(state_list)
        new_data.to_csv('state_to_learn.csv')
        break

    if check_answer(answer):
        score += 1

    if score == 50:
        game_is_on = False
        complete = turtle.Turtle()
        complete.hideturtle()
        complete.pencolor('red')
        complete.penup()
        complete.goto(0, 250)
        complete.write('Congrats! You completed 50 states!', align='center', font=('Arial', 15, 'normal'))
        break


screen.mainloop()
