# from turtle import Turtle, Screen
#
# neko = Turtle()
# my_screen = Screen()
# print(neko)
# print(my_screen.canvheight)
#
#
# neko.shape('turtle')
# neko.color('red')
# neko.forward(100.00)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.field_names = ['sami', 'tama', 'neko']
my_table.add_row(['yes', 'yes', False])
my_table.add_row([True, True, False])
my_table.align = 'l'
print(my_table)
