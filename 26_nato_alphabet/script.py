# TODO 1. Create a dictionary in this format:

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input('Enter a word: ').upper()
code_list = [data_dict[letter] for letter in user_input]

print(code_list)
