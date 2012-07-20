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

This message lists all the available options.
