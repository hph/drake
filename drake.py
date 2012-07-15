#!/usr/bin/python
#coding=utf8

import argparse
import getpass
import gtk
import hashlib
import os
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


def get_clipboard():
    '''Return the current contents of the clipboard.'''
    return gtk.clipboard_get().wait_for_text()

def set_clipboard(contents):
    '''Saves contents to the clipboard.'''
    clipboard = gtk.clipboard_get()
    clipboard.set_text(contents)
    clipboard.store()


def generate_salt(bits=128):
    '''Generate a salt using a cryptologically secure pseudorandom number
    generator.'''
    bytes = int(bits / 8.0)
    return os.urandom(bytes).encode('hex')


def hash_password(password, salt):
    '''Hash the password and save it in the database.'''
    return hashlib.sha256(salt + password).hexdigest()


def save_hash(data, filename='.pwdhashes'):
    '''Save the hash to a file.'''
    with open(filename, 'w') as file:
        file.write(' '.join([salt, hashed]))


def validate(password, filename='.pwdhashes'):
    '''Validate the password entered with the salt and hash in the file.'''
    with open(filename, 'r') as file:
        for line in file:
            salt, hashed_password = line.split()
            new_hash = hash_password(password, salt=salt)
            if new_hash == hashed_password:
                return True


def generate_wordlike_strings():
    '''Used with generate_password() to generate an easier to remember
    password.'''
    pass


def list_characters():
    '''List characters according to phonetic alphabet tables or common
    words.'''
    pass


def gauge_password_strength():
    '''Gauge the strength of the input password. Output could be boolean,
    numeric or verbose depending on the options.'''
    pass


def main():
    parser = argparse.ArgumentParser(description='Drake - password utilities')

    # TODO Merge -c and -C, unecessary to have two options (and it makes little
    # sense).
    parser.add_argument('-c', '--cloak', action='store_true',
                        help='''Cloak the user input and the program's output
                        (input/output is not printed to the screen). Used with
                        -C/--clipboard.''')
    # Obfuscate a string - used with generate_password() and the base option.
    # XXX See formatter_class in the argparse documentation.
    parser.add_argument('-o', '--obfuscate', nargs='?', metavar='STR',
                        default=False,
                        help='''Obfuscate a string with random
                        characters.''')
    # TODO Perhaps merge -s and -S.
    parser.add_argument('-s', '--seed', nargs='?', metavar='STR',
                        default=False,
                        help='''Enter a seed manually. The passwords will
                        always be the same if the same seed is used.''')
    parser.add_argument('-S', '--seeds', nargs='?', metavar='NUM',
                        type=int, default=False,
                        help='''Number of seeds.''')
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
    parser.add_argument('-C', '--clipboard', action='store_true',
                        help='''Save the password to the clipboard.''')
    parser.add_argument('len', nargs='?', metavar='length',
                        type=int, default=None,
                        help='''Password length.''')
    parser.add_argument('num', nargs='?', metavar='number',
                        type=int, default=None,
                        help='''Number of passwords.''')
    # TODO Add arguments for minimum and maximum objects.
    args = parser.parse_args()

    if args.cloak:
        global raw_input
        raw_input = getpass.getpass
    if args.len:
        args.length = args.len
    elif args.length == None:
        args.length = int(raw_input('Enter the length of the password: '))
    if args.num:
        args.number = args.num
    elif args.number == None:
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
    if args.seeds == None:
        args.seeds = int(raw_input('Enter number of seeds: '))
    if args.seeds:
        seeds = []
        for i in xrange(args.seeds):
            seeds.append(raw_input('Enter seed #%s: ' % str(i + 1)))
        args.seed = ''.join(seeds)
    elif args.seed == None:
        args.seed = raw_input('Enter a seed: ')

    passwords = []
    for _ in xrange(args.number):
        passwords.append(generate_password(base=args.obfuscate,
                                           seed=args.seed,
                                           length=args.length,
                                           include=args.include,
                                           exclude=args.exclude))
    passwords = '\n'.join(passwords)
    if args.clipboard:
        set_clipboard(passwords)
    # NOTE This is pointless ... at the moment passwords can only be printed or
    # saved to the clipboard so these options should be merged. The following
    # case is ridiculous and pointless, but exists at the moment to prevent the
    # password from being printed if the cloak option was used.
    elif not args.cloak:
        print passwords


if __name__ == '__main__':
    main()
