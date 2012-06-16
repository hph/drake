#!/usr/bin/python
#coding=utf8

import argparse
import getpass
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
        # A substring of the password.
        base_string = base[0]
        base_length = len(base_string)
        length -= base_length
        # The location of the substring in the password (various options).
        base_alignment = base[1]
    # NOTE Perhaps necessary to move this.
    if seed:
        random.seed(seed)
    while len(password) < length:
        if include:
            # The fifth character set is intended for the space character and
            # all other characters that the user wants to be included in the
            # characters sets. Only add characters if they are not present in
            # any other set.
            chars = ''.join(char_sets)
            for char in include:
                if char not in chars:
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
            # No special requirements, simply generate the password.
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
    # Shuffle the characters in case it's necessary (depends on the options).
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
    #print 'Example output with the default options:'
    #print generate_password()
    parser = argparse.ArgumentParser(description='Drake - password generation')

    # Obfuscate a string - used with generate_password() and the base option.
    # XXX See formatter_class in the argparse documentation.
    parser.add_argument('-c', '--cloak', action='store_true',
                        help='''Cloak the user input if (prying eyes will not
                        see what you type).''')
    parser.add_argument('-o', '--obfuscate', nargs='?', metavar='STR',
                        default=False,
                        help='''Obfuscate a string with random
                        characters.''')
    parser.add_argument('-s', '--seed', nargs='?', metavar='STR',
                        default=False,
                        help='''Enter a seed manually. The passwords will
                        always be the same if the same seed is used.''')
    parser.add_argument('-l', '--length', nargs='?', metavar='NUM',
                        type=int, default=16,
                        help='''Password length.''')
    parser.add_argument('-n', '--number', nargs='?', metavar='NUM',
                        type=int, default=1,
                        help='''Number of passwords.''')
    parser.add_argument('-i', '--include', nargs='?', metavar='CHARS',
                        default=False,
                        help='''Include specified characters in the character
                        pool.''')
    parser.add_argument('-e', '--exclude', nargs='?', metavar='CHARS',
                        default=False,
                        help='''Exclude specified characters in the character
                        pool.''')
    # TODO Add arguments for minimum and maximum objects.
    args = parser.parse_args()

    if args.cloak:
        global raw_input
        raw_input = getpass.getpass
    if args.length == None:
        args.length = int(raw_input('Enter the length of the password: '))
    if args.number == None:
        args.number = int(raw_input('Enter the number of passwords: '))
    if args.include == None:
        args.include = raw_input('Enter characters to be included: ')
    if args.exclude == None:
        args.exclude = raw_input('Enter characters to be excluded: ')
    if args.obfuscate:
        # Parse the obfuscate option into something generate_password()
        # understands.
        args.obfuscate = args.obfuscate.split(',') 
    elif args.obfuscate == None:
        align = raw_input('Enter an alignment for the obfuscated string (left '
                          + 'or right): ')
        # XXX The string has to be shorter than the length of the password.
        args.obfuscate = [raw_input('Enter a string to obfuscate: '), align]
    if args.seed == None:
        args.seed = raw_input('Enter a seed: ')

    for _ in xrange(args.number):
        print generate_password(base=args.obfuscate, seed=args.seed,
                                length=args.length, include=args.include,
                                exclude=args.exclude)


if __name__ == '__main__':
    main()
