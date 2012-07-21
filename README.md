drake
=====
The main reason this program was written to be able to easily generate unique
and secure passwords for any and every website one might need a password for
and to be able to do it on any computer without storing the passwords.
The way this is accomplished is by using a pseudo-random generator to generate
passwords. Pseudo-random generators need an input called 'seeds' or otherwise
they would always return the same number. By combining a master password, such
as 'bingo' and 'gmail' one has the seed 'bingogmail' which can be used to
generate a 16-character long, extremely secure password (95¹⁶ ≈ 4,4 · 10³¹
possible passwords for the default settings). Note that the master password
should be longer than the example given above and it should include uppercase
and lowercase characters, digits and punctuation symbols including empty space
(' ').

The program is fully functional in this respect, but other features have yet to
be implemented.
See [Usage examples](https://github.com/haukurpallh/drake#usage-examples) for
an overview of the currently available features.

Setup
-----
### Linux
Download drake:
    
    git clone git://github.com/haukurpallh/drake.git & cd drake

Install drake:

    python setup.py install

Uninstall drake:

    python setup.py uninstall

Usage examples
--------------
### Basic usage
Type `drake -h` to invoke the help message:

    $ drake -h
    usage: drake.py [-h] [-l [NUM]] [-n [NUM]] [-S [NUM]] [-s [STR]] [-i] [-c] [-C]

    drake - password and encryption utilities

    optional arguments:
      -h, --help                   show this help message and exit
      -l [NUM], --length [NUM]     Password length. The default is 16.
      -n [NUM], --number [NUM]     Number of passwords. The default is 1.
      -S [NUM], --seeds [NUM]      Number of seeds. The default is 1.
      -s [STR], --seed [STR]       The seed for the pseudo-random generator.
      -i, --interactive            Enter the necessary data interactively. By default all data is entered via the options.
      -c, --clipboard              Save the password(s) to the clipboard. This option is unnecessary with -C or --cloak.
      -C, --cloak                  Hide the input and the output. The password(s) are saved to the clipboard.
      -g, [STR], --gauge [STR]     Gauge the strength of an input password.
      -o, [STR], --obfuscate [STR] Obfuscate an input password. If not used with the interactive flag (-i) use the form
                                   "string,alignment" where alignment can be either left or right.

This message lists all the available options at this time. The brackets mean
that what's inside them is optional. If you run `drake -l` for example, the
`-l` flag is ignored because it doesn't have a value (as opposed to `drake -l
16`). However, `drake -il` will assume interactive mode and ask for a value. If
no option is specified, the output is a 16-character long password containing
all printable characters and space (95 characters total):

    $ drake
    R&Kp$A/>plqe]c<j

To control the number of passwords and their length, use the `-n` and `-l`
flags:

    $ drake -n 3
    o`'O=tq0K&{jUCzI
    3X0E>[#ksNO[%4Jg
    Of%W32q)5O,<n~2V

Or if you want a 20-character long password:
    
    $ drake -l 20
    ".@|,1/MWCbRozd[%T7g

Or combining these two options:

    $ drake -l 3 -l 20
    lE32MZvL:PfT2TG ]@1b
    JH=8Ib|*;5L_J<r>(_f1
    H-#,vGm_Ki %4[ha^{Sg


### Advanced features
The main point of the program is to generate passwords based on seeds. Let's
explore various methods to generate a password for your Gmail account:

    $ drake -iS
    Enter the number of seeds: 2
    Enter seed #1: MASTER_PASSWORD
    Enter seed #2: GMAIL_ACCOUNT
    uYHx}t5;SKmtl{![

Where the first seed is your master password, to be used with each and every
password you want to generate and the second seed is your Gmail address. You
can also specify the number of seeds directly (`drake -iS 2`) to skip entering
the number of seeds after the command. Note that if you combine options (`-iS`
instead of `-i -S`) only the last one may accept a value. For example, `-Si`
would not work as `-S` can accept a value. Anyway, a faster way to do the same
thing would be the following (note that the seed is the same as the two above
joined together, it's the same thing, since any number of seeds are just joined
together):

    $ drake -s MASTER_PASSWORDGMAIL_ACCOUNT
    uYHx}t5;SKmtl{![

By skipping the `-i` option the seed is visible in your bash history but if
that is not a problem this method is faster. Also note the difference between
`-S` and `-s`, the second of which was used here. In the previous example we
didn't need to enter a `-s` flag because it's implied with `-S` (if there is a
number of seeds, there must be a seed). If you want to enter the seed in this
way, you may need to surround the seed with quotes if it contains characters
such as $ (which are interpreted by the shell). A more secure method (nothing
visible in the history) would be:

    $ drake -is
    Enter the seed: MASTER_PASSWORDGMAIL_ACCOUNT
    uYHx}t5;SKmtl{![

However, this method requires user input, unlike the previous one, so it can't
be included in a separate program (for example, a web app). These three
different methods produce the same output because in effect they're equivalent.
But as mentioned earlier, some are secure while others are quick or can be used
non-interactively.

Now, all the previous methods have ended by printing everything you enter on
the screen, which might be a problem. To avoid this, use the `-C` option:

    $ drake -iCs
    Enter the seed:

Note that `drake -isC` would not work since, as explained earlier, if you
combine option flags (`-iCs` vs. `-i -C -s`) at most one can be a non-boolean
option, and it must be specified last (thus `-iCs` since `-s` is non-boolean).
The only boolean options are `-i`, `-c` and `-C`.
In any case, now the password `uYHx}t5;SKmtl{![` is on the clipboard, because
the same seed as in the previous example was entered even though it is not
visible. If you only want to save the password to the clipboard directly, you
could also do the following:

    $ drake -cs 'MASTER_PASSWORDGMAIL_ACCOUNT'

This method, just like the previous method, saved the password to the
clipboard.

To gauge the strength of a password the `-g` flag can be used:

    $ drake -ig
    Enter the password: 3/~i36GAq=-NfaW9
    Entropy (assuming a cardinality of 95): 105.12 bits
    Cracking time (worst case scenario): 22006333432588288000 seconds

The worst case scenario is a million parallel cracking attempts at a billion
passwords per second. This is a bit too optimistic and shows how strong the
passwords are.

You can obfuscate a simple password with the `-o` flag. For example:

    $ drake -io
    Enter the password: test
    Enter the alignment (left/right): left
    test}5S%hUFfui"h

Or without `-i`:

    $ drake -o test,right
    ZV8G:vY7-'Obtest

More obfuscation options will be added later.

If you don't feel like typing all these options you could add an alias to your
`.bashrc` (bash settings file):
    
    alias drake='drake -i'

Or:

    alias drake='drake -iS 2'

Depending on what you want the default options to be. Note that it would be
wiser to use some other alias than `drake` (such as `cdrake`) since you can't
disable this without removing the alias.

Although all these similar but different options may seem to make the interface
overly complex, they create more possible uses for the program and open
possibilities and make way for features yet to come.
