from art import logo
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    "/": divide
}

def calculator ():
    print(logo)
    continue_calc = True
    num1_input = float(input('What is the first number?: '))
    for op in operations:
        print(op)

    while continue_calc:
        operation = input('Pick an operation: ')
        if operation not in operations:
            print("Your input is invalid")
            break

        num2_input = float(input('What is the next number?: '))
        answer = operations[operation](num1_input, num2_input)

        print(f"{num1_input} {operation} {num2_input} = {answer}")

        will_continue = input("Type 'y' to continue calculating with 0.6, or type 'n' to start a new calculation:")

        if will_continue == 'y':
            num1_input = answer
        elif will_continue =='n':
            clear()
            calculator()
        else:
            print('Your input is invalid')
            continue_calc = False

calculator()




