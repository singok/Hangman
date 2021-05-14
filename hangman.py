# Hangman Game

import random
import string
WORDLIST_FILENAME = "words.txt"

responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]

def choose_random_word(all_words):
    return random.choice(all_words)

def load_words(): 
    try:
        input_file = open(WORDLIST_FILENAME,'r')
        file = input_file.read()
        x = file.split()
        print("Loading word list from file...\n{} words loaded.".format(len(x)))
        input_file.close()
    except IOError:
        print("File open error\n")
    return x

wordlist = load_words()

def is_word_guessed(word, letters_guessed):
    word_list = list(word)
    check = all(item in letters_guessed for item in word_list)
    return check
   
def get_guessed_word(word, letters_guessed):
    word_string = ''
    for item in word:
        if item in letters_guessed:
            word_string += item
        else:
            word_string += '_ '
    return word_string
   
def get_remaining_letters(letters_guessed):
    alphabet_list = list(string.ascii_lowercase)
    for element in letters_guessed:
        alphabet_list.remove(element)
    alphabet_string =''.join(alphabet_list)
    return alphabet_string

def hangman(word):
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    allowed_errors = 6
    letters_guessed = []
    vowel_list = ['a','e','i','o','u']
    while allowed_errors > 0:
        print("------------------------------------")
        result = get_guessed_word(word, letters_guessed)
        if is_word_guessed(word,letters_guessed) == True:
            score = allowed_errors * len(word)
            print(responses[1])
            print(responses[2].format(score))
            break
        else:
            print(responses[4].format(allowed_errors))
            avail = get_remaining_letters(letters_guessed)
            print(responses[5].format(avail))
            guess = str(input('Please guess a letter: ')).lower()
            if guess in letters_guessed:
                print(responses[8].format(result))
            elif guess in word:
                letters_guessed.append(guess)
                result1 = get_guessed_word(word, letters_guessed)
                print(responses[6].format(result1))            
            elif guess in vowel_list:   
                letters_guessed.append(guess)
                result2 = get_guessed_word(word, letters_guessed)
                print(responses[7].format(result2))
                allowed_errors -= 2 
            else:
                letters_guessed.append(guess)
                result3 = get_guessed_word(word, letters_guessed)
                print(responses[7].format(result3))
                allowed_errors -= 1   
    if allowed_errors <= 0:     
        print(responses[3].format(word))

if __name__ == "__main__":
    word = choose_random_word(wordlist)
    hangman(word)
