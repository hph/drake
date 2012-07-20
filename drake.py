#!/usr/bin/python
#coding=utf8

import argparse
import getpass
import gtk
import hashlib
import os
import random
import string
import sys


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


def get_input(query, type='str'):
    '''Return input as a string or an integer.'''
    try:
        if type == 'str':
            return raw_input(query)
        elif type == 'int':
            return int(raw_input(query))
    except ValueError:
        print 'Integer required.'
        return get_input(query, 'int')
    except (KeyboardInterrupt, EOFError):
        sys.exit()


def obfuscate(password):
    '''Return obfuscated password.'''
    pass


def gauge_password_strength(password):
    '''Gauge the strength of the input password. Output could be boolean,
    numeric or verbose depending on the options.'''
    pass


def parse_args():
    '''Return parsed arguments.'''
    parser = argparse.ArgumentParser(description='drake - password and '
                                                 'encryption utilities')
    parser.add_argument('-l', '--length', nargs='?', metavar='NUM',
                        default=False, type=int,
                        help='''Password length. The default is 16.''')
    parser.add_argument('-n', '--number', nargs='?', metavar='NUM',
                        default=False, type=int,
                        help='''Number of passwords. The default is 1.''')
    parser.add_argument('-S', '--seeds', nargs='?', metavar='NUM',
                        default=False, type=int,
                        help='''Number of seeds. The default is 1.''')
    parser.add_argument('-s', '--seed', nargs='?', metavar='STR',
                        default=False,
                        help='''The seed for the pseudo-random generator.''')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='''Enter the necessary data interactively. By
                        default all data is entered via the options.''')
    parser.add_argument('-c', '--clipboard', action='store_true',
                        help='''Save the password(s) to the clipboard. This
                        option is unnecessary with -C or --cloak.''')
    parser.add_argument('-C', '--cloak', action='store_true',
                        help='''Hide the input and the output. The password(s)
                        are saved to the clipboard.''')
    parser.add_argument('-g', '--gauge', nargs='?', metavar='STR',
                        default=False,
                        help='''Gauge the strength of an input password.''')
    parser.add_argument('-o', '--obfuscate', nargs='?', metavar='STR',
                        default=False,
                        help='''Obfuscate an input password.''')
    return parser.parse_args()


def generate_wordlike_strings():
    '''Used with generate_password() to generate an easier to remember
    password.'''
    pass


def list_characters():
    '''List characters according to phonetic alphabet tables or common
    words.'''
    pass


def main():
    # XXX There are patterns in the following code, such that it could be
    # structured as a function. This will do for now, but it would be better to
    # do something as it is very cluttered, even though only the basic features
    # are present.
    args = parse_args()
    if args.cloak:
        global raw_input
        # Use getpass instead of raw_input to hide the input from prying eyes.
        raw_input = getpass.getpass
        # For obvious reasons we don't want to print the password in plaintext.
        args.clipboard = True
    # The -o and -g options are not supposed to interact with any options, thus
    # we exit the program.
    if any([args.obfuscate is None, args.obfuscate is not False]):
        if args.interactive:
            args.obfuscate = get_input('Enter the password to obfuscate: ')
        obfuscate(args.obfuscate)
        sys.exit()
    if any([args.gauge is None, args.gauge is not False]):
        if args.interactive:
            args.gauge = get_input('Enter the password: ')
        gauge_password_strength(args.gauge)
        sys.exit()
    if args.length is None:
        if args.interactive:
            args.length = get_input('Enter the length of the password(s): ',
                                    'int')
    if args.number is None:
        if args.interactive:
            args.number = get_input('Enter the number of passwords: ', 'int')
    if args.seeds is None:
        if args.interactive:
            args.seeds = get_input('Enter the number of seeds: ', 'int')
    if args.seed is None or args.seeds is not False:
        if args.interactive:
            if args.seeds is False or args.seeds == 1:
                args.seed = get_input('Enter the seed: ')
            else:
                seeds = []
                for i in xrange(args.seeds):
                    seeds.append(get_input('Enter seed #%s: ' % str(i + 1)))
                args.seed = ''.join(seeds)
    # Setting defaults.
    if not args.length:
        args.length = 16
    if not args.number:
        args.number = 1
    if not args.seed:
        args.seed = None
    passwords = []
    # Necessary here if there are more than one passwords. Fix later.
    random.seed(args.seed)
    for _ in xrange(args.number):
        passwords.append(generate_password(length=args.length))
    passwords = '\n'.join(passwords)
    if args.clipboard:
        set_clipboard(passwords)
    elif not args.cloak:
        print passwords


if __name__ == '__main__':
    main()
