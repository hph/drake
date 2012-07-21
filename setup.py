#/usr/bin/python
#coding=utf8

import os
import sys


def authenticate():
    '''Prompt the user for the superuser password if required.'''
    # The euid (effective user id) of the superuser is 0.
    euid = os.geteuid()
    if euid != 0:
        args = ['sudo', '-E', sys.executable] + sys.argv[:] + [os.environ]
        # Replaces the current running process with the sudo authentication.
        os.execlpe('sudo', *args)
    return True


def setup():
    '''Install drake.'''
    authenticate()
    os.system('cp -Rf ../drake/ ~/.drake')
    os.system('chmod +x ~/.drake/drake.py')
    os.system('ln -fs ~/.drake/drake.py /usr/bin/drake')


def remove():
    '''Uninstall drake.'''
    authenticate()
    os.system('rm -rf ~/.drake')
    os.system('rm -f /usr/bin/drake')


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'install':
            setup()
        elif sys.argv[1] == 'uninstall':
            remove()


if __name__ == '__main__':
    main()
