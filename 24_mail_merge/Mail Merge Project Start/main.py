# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


class Letter:
    def __init__(self):
        with open('./Input/Names/invited_names.txt') as names:
            self.name_list = names.readlines()
        self.generate_letters()

    def content_generator(self, name):
        with open('./Input/Letters/starting_letter.txt') as original:
            original_letter = original.read()
            new_letter = original_letter.replace('[name]', name)
            return new_letter

    def generate_letters(self):
        for guest in self.name_list:
            guest_name = guest.strip()
            with open(f'./Output/ReadyToSend/{guest_name}.txt', mode='w') as file:
                content = self.content_generator(guest_name)
                file.write(content)


letter = Letter()
