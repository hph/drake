drake
=====
Various password and encryption utilities with a command-line interface.

See [Usage examples](https://github.com/haukurpallh/drake#usage-examples) for
an overview of the features.

![image](http://i.imgur.com/some-image.png)

Setup
-----
### Linux
Copy and paste the following commands into a terminal window:
    
    git clone git://github.com/haukurpallh/drake.git
    cp drake/ ~/.drake
    chmod +x ~/.drake/drake.py
    sudo ln -s ~/.drake/drake.py /usr/bin/drake

Usage examples
--------------
### Basic usage
Open a new terminal window (changes won't take effect on the window you used to
install the program) and type `drake -h` to invoke the help message:

    $ drake -h
    usage: drake.py [-h] [-l [NUM]] [-n [NUM]] [-S [NUM]] [-s [STR]] [-i] [-c]
                    [-C]

    drake - password and encryption utilities

    optional arguments:
      -h, --help               show this help message and exit
      -l [NUM], --length [NUM] Password length. The default is 16.
      -n [NUM], --number [NUM] Number of passwords. The default is 1.
      -S [NUM], --seeds [NUM]  Number of seeds. The default is 1.
      -s [STR], --seed [STR]   The seed for the pseudo-random generator.
      -i, --interactive        Enter the necessary data interactively. By
                               default all data is entered via the options.
      -c, --clipboard          Save the password(s) to the clipboard. This
                               option is unnecessary with -C or --cloak.
      -C, --cloak              Hide the input and the output. The password(s)
                               are saved to the clipboard.

This message lists all the available options at this time. If no option is
specified, the output is a 16-character long password containing all printable
characters and space (95 characters total):

    $ drake
    R&Kp$A/>plqe]c<j

The main point of the program is to generate passwords based on seeds. Let's
explore various methods to generate a password for your Gmail account:

    $ drake -iS
    Enter the number of seeds: 2
    Enter seed #1: MASTER_PASSWORD
    Enter seed #2: GMAIL_ACCOUNT
    uYH`}t5;SKmtl{![

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
    uYH`}t5;SKmtl{![

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
    uYH`}t5;SKmtl{![

However, this method requires user input, unlike the previous one, so it can't
be included in a separate program (for example, a web app). These three
different methods produce the same output because in effect they're equivalent.
But as mentioned earlier, some are secure while others are quick or can be used
non-interactively.

Now, all the previous methods have ended by printing everything you enter on
the screen, which might be a problem. To avoid this, use the `-C` option:

    $ drake -iCs
    Enter the seed:

Now the password `uYH`}t5;SKmtl{![` is on the clipboard, because the same seed
was entered even though it is not visible. If you only want to save the
password to the clipboard directly, you could also do the following:

    $ drake -cs 'MASTER_PASSWORDGMAIL_ACCOUNT'

