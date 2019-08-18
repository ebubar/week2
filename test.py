import random
import string
import sys
import pytest

import ps2_a
import ps2_b


def test_ps2a_1():
    assert ps2_a.pay_off_in_one_year_bisection(105000, 12) == pytest.approx(9299.017, abs=0.1)


def test_ps2a_2():
    assert ps2_a.pay_off_in_one_year_bisection(2500, 1.5) == pytest.approx(210.018, abs=0.1)


def test_ps2a_3():
    assert ps2_a.pay_off_in_one_year_bisection(500000, 18) == pytest.approx(45523.189, abs=0.1)


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


@pytest.fixture(scope="module")
def words():
    random.seed(0)
    words = load_words()
    return [random.choice(words) for i in range(10)]


def test_is_word_guessed(words):
    random.seed(0)
    for word in words:
        shuffled_word = ''.join(random.sample(word,len(word)))
        assert ps2_b.is_word_guessed(word, shuffled_word), f'{word} not reported as guessed for {shuffled_word}'
        letter_to_remove = shuffled_word[-1]
        shuffled_word = shuffled_word.replace(letter_to_remove, '')
        assert not ps2_b.is_word_guessed(word, shuffled_word), f'{word} incorrectly reported as guessed for {shuffled_word}'


def test_print_secret_word_with_letters_guessed(words, capsys):
    correct = [
        '_ _ _ _ _ _',
        '_ a _ _ _ a _ _ _',
        '_ a _ _',
        '_ _ a _ _ _ _',
        '_ _ _ _ _ _ _ _',
        '_ _ _ _ _ _',
        '_ _ _ _ _',
        '_ _ _ _ _',
        '_ _ _ _',
        '_ _ a _ _ _',
    ]
    for word, correct in zip(words, correct):
        ps2_b.print_secret_word_with_letters_guessed(word, 'a')
        out, err = capsys.readouterr()
        assert correct.replace(' ', '').replace('\n', '') == out.replace(' ', '').replace('\n', '').strip('SecretWord:'), f'Output of print_secret_word_with_letters_guessed for {word} should be {correct}, not {out}'


def test_get_available_letters():
    correct =   [
        ('m', 'abcdefghijklnopqrstuvwxyz'), 
        ('yn', 'abcdefghijklmopqrstuvwxz'), 
        ('biq', 'acdefghjklmnoprstuvwxyz'), 
        ('pmzj', 'abcdefghiklnoqrstuvwxy'), 
        ('plsgq', 'abcdefhijkmnortuvwxyz'), 
        ('ejeydt', 'abcfghiklmnopqrsuvwxz'), 
        ('zirwzte', 'abcdfghjklmnopqsuvxy'), 
        ('jdxcvkpr', 'abefghilmnoqstuwyz'), 
        ('dlnktugrp', 'abcefhijmoqsvwxyz'), 
        ('oqibzracxm', 'defghjklnpstuvwy')
    ]

    for letters_guessed, available_letters in correct:
        assert available_letters == ps2_b.get_available_letters(letters_guessed).replace(' ', '').replace('\'', '').replace(',', '').replace('[', '').replace(']', '')


class GuessFunc:
    def __init__(self, guess_list):
        self.guess_list = guess_list
        self.cnt = 0

    def get_guess(self):
        guess = self.guess_list[self.cnt]
        self.cnt += 1
        return guess


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def test_hangman(capsys, monkeypatch):
    guesses = 'aiiml'
    word = 'mill'
    correct_reponses = ['sorry', 'got one', 'already guessed', 'got one', 'got one', 'congratulations']
    
    guesser = GuessFunc(guesses)
    monkeypatch.setattr('builtins.input', lambda x: guesser.get_guess())
    ps2_b.hangman(word)
    out, err = capsys.readouterr()
    
    game_begins_ix = out.lower().index('available')
    game_str = out[game_begins_ix:].lower()
    sorry_pos = list(find_all(game_str, 'sorry'))
    got_one_pos = list(find_all(game_str, 'got one'))
    already_guessed_pos = list(find_all(game_str, 'already guessed'))
    congratulations_pos = list(find_all(game_str, 'congratulations'))
    sequence = [(i, 'sorry') for i in sorry_pos] + \
        [(i, 'got one') for i in got_one_pos] + \
        [(i, 'already guessed') for i in already_guessed_pos] + \
        [(i, 'congratulations') for i in congratulations_pos]
    sequence = [i[1] for i in sorted(sequence, key=lambda x: x[0])]

    assert sequence == correct_reponses, f'Incorrect sequence of game responses, for guesses {guesses} and word {word}, the correct sequence of game responses is {correct_reponses}'
