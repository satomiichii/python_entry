from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def run_caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar (type, original_text, num_shift):
        result_text = ''
        for letter in original_text:
            if letter in alphabet:
                index = alphabet.index(letter)
                if type == 'encode':
                    shifted = index + num_shift
                    if shifted >= len(alphabet) - 1:
                        shifted -= len(alphabet)
                elif type == 'decode':
                    shifted = index - num_shift
                    if shifted < 0:
                        shifted += len(alphabet) 
                else:
                    print('You entered invalid input.')
                    return
                result_text += alphabet[shifted]
            else:
                result_text += letter
        print(f"Your {type}d text is {result_text}")
    caesar(direction,text,shift)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if repeat == 'yes':
        run_caesar()

run_caesar()
