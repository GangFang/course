# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/gang_fang/documents/stem/course/mitx-intro-to-cs/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            ans += '_ '
        else:
            ans += letter
    
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # create an empty string that store the result
    ans = ''
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            ans += letter
    return ans
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    #let the user know how many letters the secretWord contains
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'

    # initialize useful variables
    mistakesMade = 0
    lettersGuessed = []
    lettersGuessed_lag = []
    
    # loop over the whole process
    while mistakesMade < 8:
        print '-----------'
        print 'You have ' + str(8 - mistakesMade) + ' guesses left'
        
        # print all available letters
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        
        # Ask the user to supply one guess
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        # add the guessed letter to the list lettersGuessed
        # here lettersGuessed gets updated fisrt becuase updated status is needed
        # in order to print it out after guessing
        lettersGuessed.append(guess)
        status = getGuessedWord(secretWord, lettersGuessed)
        
        # Provide immediate feedback
        # here lettersGuessed_lag is used so as to avoid the situation that the word
        # guessed is always in lettersGuessed which has been appended the guessed word
        if guess not in lettersGuessed_lag:     
            if guess in secretWord:
                print 'Good guess: ' + status
            else: 
                print "Oops! That letter is not in my word: " + status
                mistakesMade += 1
        else:
            print "Oops! You've already guessed that letter: " + status
        
        lettersGuessed_lag.append(guess)
        
        # if win
        if '_' not in status:
            print '-----------'
            return 'Congratulations, you won!'
        
    print '-----------'
    return 'Sorry, you ran out of guesses. The word was ' + secretWord






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print hangman(secretWord)
