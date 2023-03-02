from preloaded import MORSE_CODE


def decode_morse(morse_code):
    words = []
    for word in morse_code.strip().split("   "):
        symbol = (''.join(MORSE_CODE[i] for i in word.split(' ')))
        words.extend([symbol])
    return (" ".join(words))
