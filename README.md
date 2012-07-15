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
install the program) and type `drake`:

    $ drake
    NGM'${yrKJd,31&&

The `$` symbol is just the prompt, do not type it. The second line contains a
random sixteen-character password. To print control the length of the password
and the number of printed passwords, you could do something like `drake 20 5`
for five twenty-character passwords:

    $ drake 20 5
    vDT/x9Zi(U67aPR:<C8^
    G'A*x1pasYKUG$/Qz0"H
    9j]o49mT`d]@3HbcFq82
    `r"fS}.>x2\U;"IO>RVb
    ;!fPRV(Q0H=B'`A]hCxC

There are more options which will be documented later. Type `drake -h` to see
all the options.
