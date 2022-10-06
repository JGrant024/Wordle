import random
from turtle import position


def processGuess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G"
        elif letter in theAnswer:
            clue += "Y"
        else:
            clue += "_"
        position += 1
    print(clue)
    return clue == "GGGGG"


# Where the words are stored in a list
word_list = []
word_file = open('wordlist.txt')
for word in word_file:
    word_list.append(word.strip())

# Choose a random word
answer = random.choice(word_list)

num_of_guesses = 0
guessed_corretly = False

# start of while loop
while num_of_guesses < 6 and not guessed_corretly:
    # get guess from player
    guess = input('Enter a 5 letter word and press enter: ')
    print('You have guess', guess)
    num_of_guesses += 1

    # process the guess from the player
    guessed_corretly = processGuess(answer, guess)
