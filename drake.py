#!/usr/bin/python
#coding=utf8

import random
import string


CHAR_SETS = [string.lowercase, string.uppercase, string.digits,
             string.punctuation, ' ']


def generate_password(base=None, seed=None, length=16, char_sets=CHAR_SETS,
                      min_objects=None, max_objects=None, include=None,
                      exclude=None):
    '''Generate a password based on various options.'''
    password = ''
    if base:
        length -= len(base[0])
        base_string = base[0]
        base_length = len(base_string)
        base_alignment = base[1]
    while len(password) < length:
        if include:
            char_sets[4] += include
        if exclude:
            for char in exclude:
                for i, char_set in enumerate(char_sets):
                    if char in char_set:
                        char_sets[i] = char_set.replace(char, '')
        if min_objects:
            for i, item in enumerate(min_objects):
                for _ in xrange(item):
                    password += random.choice(char_sets[i])
            # If the following two lines were ommitted the output would have an
            # equal number of characters from each character set if the length
            # of the generated password is a multiple of the sum of the items 
            # in min_objects.
            extra_length = length - sum(min_objects) 
            password += generate_password(length=extra_length)
        else:
            for _ in xrange(length):
                password += random.choice(''.join(char_sets))
        if max_objects:
            count = {}
            for char in password:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            for char in count:
                if count[char] >= max_objects:
                    # TODO Find a way to handle this outcome. Following line
                    # for testing purposes.
                    print char, count[char]
    # Shuffle the characters if necessary (depends on the options).
    password = ''.join(random.sample(password, length))
    if base:
        if base_alignment == 'left':
            password = base_string + password
        elif base_alignment == 'right':
            password += base_string
        # TODO Write something to change "example" into "$ex.am-2ple" or
        # something similar (randomly select the lenght of each part).
        elif base_alignment == 'split':
            pass
        elif base_alignment == 'random':
            pos = random.randrange(0, length + base_length - 1)
            password = password[:pos] + base_string + password[pos:]
    return password


def generate_wordlike_strings():
    '''Used with generate_password() to generate an easier to remember
    password.'''
    pass


def list_characters():
    '''According to phonetic alphabet tables or common words.'''
    pass


def gauge_password_strength():
    '''Gauge the strength of the input password. Output could be boolean,
    numeric or verbose depending on the options.'''
    pass


def main():
    # TODO Add argparse commands. Current code only for testing purposes.
    print 'Example output with the default options:'
    print generate_password(max_objects=2)


if __name__ == '__main__':
    main()
