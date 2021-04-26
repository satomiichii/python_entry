# with open('weather_data.csv') as data:
#     contents = data.readlines()
#     print(contents)
#
# import csv
#
# with open('weather_data.csv') as data_file:
#     temp = []
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data['day'])
#
# print(data['temp'].max())
#
# print(data[data.temp == data['temp'].max()])
#
# monday = data[data.day == 'Monday']
# print("fahrenheit", ((monday.temp * 9/5) + 32))
#
# data_dict = {
#     'student': ['Sami', 'Tama', 'Neko'],
#     'score': [80, 95, 100]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_data = data.groupby('Primary Fur Color').count()['Unique Squirrel ID']
color_data.to_csv('sq_color.csv')
