morse_dictionary = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

def morse_to_latin(morse_code):
    latin_text = ''
    morse_code = morse_code.strip()

    if morse_code:
        words = morse_code.split('  ')
        for word in words:
            letters = word.split(' ')
            for letter in letters:
                if letter in morse_dictionary:
                    latin_text += morse_dictionary[letter]
            latin_text += ' '

    return latin_text.strip()

def latin_to_morse(latin_text):
    morse_code = ''
    latin_text = latin_text.upper()

    for char in latin_text:
        if char == ' ':
            morse_code += ' '
        elif char in morse_dictionary.values():
            for key, value in morse_dictionary.items():
                if value == char:
                    morse_code += key + ' '

    return morse_code.strip()


text = input("Enter a sentence in Morse code or Latin characters: ")

if text.startswith('-') or text.startswith('.'):
    result = morse_to_latin(text)
    print("Translated to Latin:", result)
else:
    result = latin_to_morse(text)
    print("Translated to Morse code:", result)
