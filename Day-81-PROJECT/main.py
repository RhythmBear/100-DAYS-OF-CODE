# BUILDING MY TEXT TO MORSE CODE CONVERTER
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' / ', ',': '--..--',
    ':': '---...', ';': '-.-.-.', '.': '.-.-.-', '"': '.-..-.', '(': '-----.', ')': '.-----', "'": "-.--.-",
    '&': '.-...', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '?': '..--..', '!': '-.-.--', '/': '-..-.'

              }

INPUT_VALID = True

# -------------------------------------- FUNCTIONS ----------------------------------------------------- #


def convert_to_morse(user_words):

    final_morse_code = ""

    list_of_words = user_words.split(' ')
    # for each word in the list of words, I split each word into a list hence creating a nested list.
    words_with_letters = [list(word) for word in list_of_words]

    # convert each letter to a morse version
    morse_list_of_words = [[MORSE_DICT[letter] for letter in word] for word in words_with_letters]

    # Morse list is the list of strings in morse code already
    morse_list = []
    for letter_dict in morse_list_of_words:
        morse_word = ' '.join(letter_dict)
        morse_list.append(morse_word)

    # After getting all the Morse letter in a list we can now join using the Morse space i.e .-.-.-
    final_morse_code = f'{MORSE_DICT[" "]}'.join(morse_list)

    return final_morse_code


def convert_to_english(morse_text):
    morse_code_words = morse_text.split(' / ')
    # print(morse_code_words)

    # Divide the words into letters
    morse_code_letter_list = [word.split(' ') for word in morse_code_words]
    # print(morse_code_letter_list)
    english_word_list = []

    for letter_list in morse_code_letter_list:
        word = ""
        for letter in letter_list:
            # print(letter)
            # A method to retrieve a key from a dictionary through its value
            s = [key for key, value in MORSE_DICT.items() if value == letter][0]
            # print(s)

            word += s
        english_word_list.append(word)

    final_sentence = ' '.join(english_word_list)
    return final_sentence.title()


# ----------------------------------------------------------------------------------------------------- #

# CODE BEGINS HERE
print("WELCOME TO EMMANUEL's MORSE CODE CONVERTER")

session_is_active = True
while session_is_active:
    mode = ''

    request_not_valid = True
    while request_not_valid:
        # Get the User's Request
        request = input("\nType 'M' for 'English --> Morse' and 'E' for 'Morse --> English': ").upper()

        # check to ensure that the User's request is valid
        if request == 'M' or request == 'E':
            if request == 'E':
                print("Please make sure the space text i.e ' ' is represented "
                      "with '/' and not '.-.-.-.-' to get accurate results ")
                mode = 'Morse --> English'
            elif request == 'M':

                mode = 'English --> Morse'
            request_not_valid = False
        else:
            print("Invalid input! Please try again")

    user_input = input(f"Your {mode.split(' ')[0]} Text 👇: \n").upper()

    # Check to make sure the characters in the english sentence are characters in our dictionary
    if mode == 'English --> Morse':
        for i in user_input:
            if i not in MORSE_DICT:
                INPUT_VALID = False

    # Check to make sure the morse code values are valid
    if INPUT_VALID:
        if mode == "English --> Morse":
            morse_code = convert_to_morse(user_input)
            print(f"\nYour {mode} Output 👇 : \n{morse_code}")
        elif mode == "Morse --> English":
            english_code = convert_to_english(user_input)
            print(f"\nYour {mode} Output 👇 : \n{english_code}")
    else:
        print("Your Input is not valid")

    restart = input("Thank you for using my service. \nType 'Y' to perform another conversion, "
                    "\nPress any other key to exit.").upper()

    if restart == 'N':
        session_is_active = False
