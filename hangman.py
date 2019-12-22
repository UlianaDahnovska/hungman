# Problem Set 2, hangman.py
# Name: Dahnovska Uliana
# Collaborators:
# Time spent: 6 hours

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    found = True
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            found = False
            break
    return found


def get_guessed_word(secret_word, letters_guessed):
    user_row = list('_'*len(secret_word))
    for i in range(len(secret_word)):
        for j in range(len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                user_row[i] = secret_word[i]
                break
    return ''.join(user_row)

def check_input(letters_guessed, warnings, guesses_remaining, is_with_hints=False):
    input_user = input('Please guess a letter: ').lower()
    while len(input_user)!=1 or not input_user.isalpha() or input_user in letters_guessed:

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if input_user == "*" and is_with_hints:
            show_possible_matches(guessed_word)
            input_user = input('Please guess a letter: ').lower()
            continue

        warnings -= 1

        if warnings!=0:
            if input_user in letters_guessed:
                print('Oops! You already guessed that letter. You have '+ str(warnings) + ' warnings left: '+str(guessed_word))
            else:
                print('Oops! That is not a valid letter. You have '+str(warnings)+' warnings left: '+str(guessed_word))
        else:
            guesses_remaining-=1
            print('You have no warnings left so you lose one guess. '+str(guesses_remaining)+' guesses left: '+str(guessed_word))

            if guesses_remaining == 0:
                return 'stop', warnings, guesses_remaining
        input_user = input('Please guess a letter: ').lower()
    return input_user, warnings, guesses_remaining

def get_available_letters(letters_guessed):
    letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        for alp_letter in letters:
            if alp_letter == letter:
                letters.remove(alp_letter)
    return ''.join(letters)
    

def hangman(secret_word):
    warnings=3
    guesses_remaining=6
    letters_guessed=[]
    dec = '-'*11
    vow='aeiou'
    print('Welcome to the game Hangman!\nI am thinking of a word that is '+str(len(secret_word))+' letters long\n'+dec+'\nYou have '+str(warnings)+' warnings left.')

    while not is_word_guessed(secret_word, letters_guessed):
        if guesses_remaining > 0:
            print('You have '+str(guesses_remaining)+' guesses left.\nAvailable letters: '+get_available_letters(letters_guessed))
            input_letter, warnings, guesses_remaining = check_input(letters_guessed, warnings, guesses_remaining)

            if input_letter == 'stop':
                print('End of the game!\n'+dec)
                break

            letters_guessed.append(input_letter)
            if input_letter in secret_word:
                print('Good guess: '+get_guessed_word(secret_word, letters_guessed))
            else:
                if input_letter in vow:
                    guesses_remaining -=2
                else:
                    guesses_remaining -=1
                print('Oops! That letter is not in my word:'+get_guessed_word(secret_word,letters_guessed))
            print(dec)
        if guesses_remaining <=0:
            print('Sorry, you ran out of guesses. The word was: ' + str(secret_word))
            break

    if guesses_remaining > 0:
        score = guesses_remaining*len(set(secret_word))
        print('Congratulations, you won!\nYour total score for this game is:'+str(score))



# -----------------------------------


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ','')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if (my_word[i] != '_') and (my_word[i] != other_word[i]):
                return False
    else:
        return False
    return True



def show_possible_matches(my_word):
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)

    if matches:
        print(matches)
    print('No matches found')


def hangman_with_hints(secret_word):
    warnings = 3
    guesses_remaining = 6
    letters_guessed = []
    dec = '-' * 11
    vow = 'aeiou'
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + str(len(secret_word)) + ' letters long\n' + dec + '\nYou have ' + str(warnings) + ' warnings left.')

    while not is_word_guessed(secret_word, letters_guessed):
        if guesses_remaining>0:
            print('You have '+str(guesses_remaining)+' guesses left.\nAvailable letters: '+get_available_letters(letters_guessed))
            input_letter, warnings, guesses_remaining = check_input(letters_guessed, warnings, guesses_remaining, is_with_hints=True)

            if input_letter == 'stop':
                print('End of the game!\n' + dec)
                break

            letters_guessed.append(input_letter)
            if input_letter in secret_word:
                print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            else:
                if input_letter in vow:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word:' + get_guessed_word(secret_word, letters_guessed))
            print(dec)
        if guesses_remaining <=0:
            print('Sorry, you ran out of guesses. The word was: ' + str(secret_word))
            break

    if guesses_remaining > 0:
        score = guesses_remaining*len(set(secret_word))
        print('Congratulations, you won!\nYour total score for this game is:'+str(score))



if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    #hangman_with_hints(secret_word)
