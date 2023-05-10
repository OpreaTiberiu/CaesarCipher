import art
import alphabet


def code(text, shift, direction):
    var = 1
    result = ""
    if direction.lower() == "decode":
        var = -1
    shift_value = var * shift
    for letter in text:
        if letter in alphabet:
            nr_of_letters = len(alphabet)
            new_letter_index = (alphabet.index(letter) + shift_value) % nr_of_letters
            result += alphabet[new_letter_index]
        else:
            result += letter

    print(result)


print(art.logo)

alphabet = alphabet.letters
keep_going = True
while keep_going:
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    code(text_input, shift_input, direction_input)

    keep_going_input = input("Do you want to continue? Type 'yes' or 'no':\n").lower()
    if keep_going_input == 'no':
        keep_going = False
