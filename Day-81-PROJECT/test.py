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

def convert_to_english(morse_code):
    morse_code_words = morse_code.split(' / ')
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


convert_to_english('.... . .-.. .-.. --- / - .-. .. -.-. .. .-')
