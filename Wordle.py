import random
from colorama import Fore, Back, Style
from word_list import words

random_word = random.choice(words).upper()
num_of_guesses = 0

while num_of_guesses < 5:
    num_of_guesses += 1
    guess = input('Enter a 5 letter word and press enter: ').upper()
    # guess = 'CHEAP'
    # ['C', 'L', 'O', 'T', 'H']
    random_word_list = [letter for letter in random_word]
    display_values = []

    for index, letter in enumerate(guess):
        if random_word_list[index] == letter:
            display_values.append(letter.upper())
            random_word_list[index] = '_'  # ['_', 'L', 'O', 'T', 'H']
        elif letter in random_word_list:
            display_values.append(letter.lower())
            index = random_word_list.index(letter)
            random_word_list[index] = '_'  # ['_', 'L', 'O', 'T', '_']
        else:
            display_values.append('*')

    display = " ".join(display_values)
    print(display)

    if guess == random_word:
        print('Congratulations! You won!')
        break

    if num_of_guesses == 5:
        print('You lose. You ran out of guesses!')
        print(f'The word was {random_word}.')
