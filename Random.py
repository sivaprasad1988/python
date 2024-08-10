import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word) - 1
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
guessCharacters = []
while length:
    placeholder += '_'
    length -= 1
doRun = True
while doRun:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessCharacters.append(guess)
        elif letter in guessCharacters:
            display += letter
        else:
            display += '_'

    print(display)

    if "_" not in display:
        doRun = False

    print(guessCharacters)