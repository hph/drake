drake
=====
### [Features](https://github.com/haukurpallh/drake#features) ‒ [Setup](https://github.com/haukurpallh/drake#setup) ‒ [FAQ](https://github.com/haukurpallh/drake#faq) ‒ [Examples](https://github.com/haukurpallh/drake#usage-examples)

With drake you can easily generate strong and unique passwords for every
website. The passwords are not stored anywhere and can be algorithmically
generated on any computer. All you need to remember is a single master
password, which you will use for every website; and something that identifies
the account, such as the website itself or an email address. For example,
to generate a password for my Gmail account I might do something like this*:

    $ drake -iS 2
    Enter seed #1: my master password
    Enter seed #2: gmail
    78u+%oQ&A0M9tBXy

The output, `78u+%oQ&A0M9tBXy`, will always be the same if the same seeds ("my
master password" and "gmail" in this case) are entered. The output will be
completely different when the second seed is changed, for example:
    
    $ drake -iS 2
    Enter seed #1: my master password
    Enter seed #2: facebook
    F#,Oqe0\;-L@WTw=

With the default settings you will generate a sixteen-character combination of
95 possible characters. This means that the number of possible passwords is
95¹⁶ ≃ 4.4·10³¹.

Please take note that this is a programming exercise and in no way a
cryptologically secure program, at least for the time being.

**For a non-interactive invocation use* `drake -s "my master passwordgmail"`*,
which returns the password directly. Also, the space in* `-iS 2` *is unnecessary
and used here only for clarity.* `drake -iS2` *is completely equivalent.*

Features
--------
* Manage passwords as explained above
* Every option can be entered both interactively and directly
* Options to control:
  * Password length
  * Number of passwords
  * Password seed
  * Included character sets to be selected from (lowercase, uppercase, digits
    and punctuation)
  * Save the password(s) to the clipboard
  * Hide input from prying eyes
  * Gauge password strength (entropy, cracking time, etc)
  * Obfuscate a simple password into a more complex one
  * Roll dice: randomly select an item from a list
* Future features include:
  * Text and file encryption with bcrypt and other algorithms
  * Encrypted password databases
  * Password hashing and salting functions

The various features are explained in detail in the
[usage examples](https://github.com/haukurpallh/drake#usage-examples) section
below.

Please report bugs or suggest features on the
[issues page](https://github.com/haukurpallh/drake/issues).

Setup
-----
### Linux
Download drake and change to its directory:
    
    git clone git://github.com/haukurpallh/drake.git; cd drake

Install drake:

    python setup.py install

This will overwrite existing program files if any so it can be used to update as well.

Execute `python setup.py uninstall` to uninstall drake.

FAQ
---
* [How do I list all the commands?](https://github.com/haukurpallh/drake#invoking-the-help-message)
* [How can I generate a password?](https://github.com/haukurpallh/drake#generating-a-one-time-password-without-a-seed)
* [How can I control the length and number of passwords?](https://github.com/haukurpallh/drake#controlling-the-number-of-passwords-and-password-length)
* [How can I generate a password without symbols?](https://github.com/haukurpallh/drake#controlling-which-character-sets-are-available)
* [How do the seeds work?](https://github.com/haukurpallh/drake#generating-a-password-from-a-seed)
* [What if someone is looking over my shoulder while I enter seeds and options?](https://github.com/haukurpallh/drake#hiding-the-input-and-saving-the-output-to-the-clipboard)
* [How do I save the password to the clipboard](https://github.com/haukurpallh/drake#hiding-the-input-and-saving-the-output-to-the-clipboard)
* [What is the --obfuscate option?](https://github.com/haukurpallh/drake#obfuscating-a-password)
* [How can I know if the password is strong?](https://github.com/haukurpallh/drake#gauging-the-strength-of-a-password)
* [How does the --roll command work?](https://github.com/haukurpallh/drake#rolling-dice)
* [Do I have to enter all these options every time?](https://github.com/haukurpallh/drake#saving-commonly-used-commands-as-aliases)

Usage examples
--------------
### Invoking the help message
Type `drake -h` to invoke the help message:

    usage: drake [-h] [-v] [-l [NUM]] [-n [NUM]] [-S [NUM]] [-s [STR]] [-i]
                 [-c] [-C] [-g [STR]] [-o [STR]] [-x [STR]] [-r [STR]]

    drake - password management utilities

    optional arguments:
    -h, --help                        show this help message and exit
    -v, --version                     show program's version number and exit
    -l [NUM], --length [NUM]          Password length. The default is 16.
    -n [NUM], --number [NUM]          Number of passwords. The default is 1.
    -S [NUM], --seeds [NUM]           Number of seeds. The default is 1.
    -s [STR], --seed [STR]            The seed for the pseudo-random generator.
    -i, --interactive                 Enter the necessary data interactively.
                                      By default all data is entered via the
                                      options.
    -c, --clipboard                   Save the password(s) to the clipboard.
                                      This option is unnecessary with -C or
                                      --cloak.
    -C, --cloak                       Hide the input and the output. The
                                      password(s) are saved to the clipboard.
    -g [STR], --gauge [STR]           Gauge the strength of an input password.
    -o [STR], --obfuscate [STR]       Obfuscate an input password. If not used
                                      with the interactive flag (-i) use the
                                      form "string,alignment" where alignment
                                      can be either left or right.
    -x [STR], --character-sets [STR]  Control which character sets are used in
                                      the generator. Available character sets
                                      are lowercase and uppercase characters,
                                      digits and all punctuation symbols. This
                                      constitutes all the printable characters,
                                      95 including whitespace (' '). The option
                                      can contain one or all of the initials of
                                      the character sets, for example, use
                                      'lud' for an alphanumeric password.
    -r [STR], --roll [STR]            Select any of a comma-separated list of
                                      values or strings.

    drake returns 0 if there was no error

This message lists all the available options at this time. The brackets mean
that what's inside them is optional. If you run `drake -l` for example, the
`-l` flag is ignored because it doesn't have a value (as opposed to `drake -l
16`). However, `drake -il` will assume interactive mode and ask for a value.

### Generating a one-time password without a seed
If no seed is specified the output will be a 16-character long password
containing lowercase and uppercase characters, digits and punctuation symbols
including space (95 characters total). Currently Python's `random` module is
used but it will be raplaced by `os.urandom`, which is cryptologically
secure, as soon as possible.

    $ drake
    R&Kp$A/>plqe]c<j

### Controlling the number of passwords and password length
To control the number of passwords and their length, use the `-n` and `-l`
flags:

    $ drake -n 3
    o`'O=tq0K&{jUCzI
    3X0E>[#ksNO[%4Jg
    Of%W32q)5O,<n~2V

Or if you want a 20-character long password (the `-i` flag is unnecessary):
    
    $ drake -il
    Enter the length of the password(s): 20
    ".@|,1/MWCbRozd[%T7g

Or combining these two options:

    $ drake -n 3 -l 20
    lE32MZvL:PfT2TG ]@1b
    JH=8Ib|*;5L_J<r>(_f1
    H-#,vGm_Ki %4[ha^{Sg

### Controlling which character sets are available
If you don't want or can't use all the 95 printable characters used by default
(some websites have stupid password policies), you can use the `-x` option.
You need to specify the initial(s) (in lowercase) of the character set(s) you
want to include, l for lowercase, u for uppercase, d for digits and p for
punctuation and symbols. For an alphanumeric password you would do the
following:

    $ drake -x lud
    LkxaotIS6s7vQXBe

Or with the `-i` flag:

    $ drake -ix
    Available character sets:
    Lowercase: abcdefghijklmnopqrstuvwxyz
    Uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Digits: 0123456789
    Punctuation symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    Enter the initials of each character set: dul
    Ek7qSCWijAT8rZrg

### Generating a password from a seed
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

### Hiding the input and saving the output to the clipboard
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

### Obfuscating a password
You can obfuscate a simple password with the `-o` flag. For example:

    $ drake -io
    Enter the password: test
    Enter the alignment (left/right): left
    test}5S%hUFfui"h

Or without `-i`:

    $ drake -o test,right
    ZV8G:vY7-'Obtest

More obfuscation options will be added later.

### Gauging the strength of a password
To gauge the strength of a password the `-g` flag can be used:

    $ drake -ig
    Enter the password: 3/~i36GAq=-NfaW9
    Entropy (assuming a cardinality of 95): 105.12 bits
    Cracking time (worst case scenario): 22006333432588288000 seconds

The worst case scenario is a million parallel cracking attempts at a billion
passwords per second. This is a bit too optimistic and shows how strong the
passwords are.

### Rolling dice
There's a feature similar to rolling dice. Call `drake -ir` to select any of a
comma-separated list of values or strings, for example:

    $ drake -ir
    Enter the choices: 1,2,3,4,5,6
    5

Or:

    $ drake -r black,grey,white
    black

### Saving commonly used commands as aliases
If you don't feel like typing all these options you could add an alias to your
`.bashrc` (bash settings file):
    
    alias drake='drake -i'

Or:

    alias drake='drake -iS 2'

Depending on what you want the default options to be. Note that it would be
wiser to use some other alias than `drake` (such as `cdrake`) since you can't
disable this without removing the alias.

Although all these similar but different options may seem to make the interface
overly complex, the fact that most of them can be used in combination is
enough to justify it.
