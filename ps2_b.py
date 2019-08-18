#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
@collaborators: 
"""

import random
import string

# Here is some helper code. You don't need to understand or modify this helper code,
# but you will need to call the functions, so it's worth looking at the docstrings
# of the functions to see what they do

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    wordlist = list()
    wordlist_filename = 'words.txt'
    print('Loading word list from file: {}'.format(wordlist_filename))
    with open(wordlist_filename, 'r') as f:
        for line in f.readlines():
            if 4 <= len(line.rstrip('\n')):  # don't read in words less than 4 chars long
                wordlist.append(line.rstrip('\n'))
    print('{} words loaded'.format(len(wordlist)))
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

def is_word_guessed(secret_word, letters_guessed):
    """
    This function accepts the secret word, as well as a string of letters which the
    user has guessed, and returns False unless all letter in the secret word
    have been guessed.

    :param str secret_word: A string representation of the secret word
    :param str letters_guessed: A string containing all of the letters
      that the user has guessed (e.g. 'aei')
    :return: True if all letters have been guessed otherwise False
    :rtype: bool
    """
    return None

def print_secret_word_with_letters_guessed(secret_word, letters_guessed):
    """
    This function takes the secret word, as well as a string containing letters
    which the user has guessed, and prints the secret word showing the letters 
    guessed and underscores for unguessed letters.

    For example, if the secret word is apple and the user has guessed a and e, then
    the secret_word would be 'apple', letters_guessed would be 'ae', and this
    function would print: a _ _ _ e

    :param str secret_word: A string representation of the secret word
    :param str letters_guessed: A string containing the letters that the user 
      has guessed
    :return: Nothing
    :rtype: None
    """
    return None

def get_available_letters(letters_guessed):
    """
    This function accepts a string containing the letters the user has guessed so far, and
    returns a string of letters the user hasn't guessed.

    Hint: use string.ascii_lowercase to get all the lowercase letters.

    :param str letters_guessed: A string containing the letters that the user has guessed
    :return: A string containing all of the letters the user hasn't guessed yet
    :rtype: str
    """
    return None


def hangman(secret_word):
    """
    Starts an interactive game of hangman using `secret_word` as the word the user is
    trying to guess.

    At the start of the game, this function lets the user know how many letters
    secret_word contains.

    The user starts with a number of guesses equal to the number of letters in the word
    plus 4.

    Each round, the function tells the user how many guesses they have left, prints the
    possible letters the user can guess by calling `get_available_letters`,  and asks the user
    to guess a letter. The function checks that the user actually entered a letter (not
    another character, or nothing), and that the letter hasn't been guessed yet.
    Hint: you should convert entered characters to lowercase before handling them.

    Then the function then tells the user whether or not that letter was in the secret word,
    and prints the guessed letters in the secret word by calling
    `print_secret_word_with_letters_guessed`.

    The function then calls `is_word_guessed` to determine whether or not the word has been
    guessed. If the word was guessed, tell the user they have won! If the word has not been
    guessed, decrement the remaining guesses by 1, and continue play if guesses remain.

    :param str secret_word: The secret word to guess
    :return: Nothing
    :rtype: None
    """
    return None

if __name__ == '__main__':
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
