#!/usr/bin/python3
"""Defines a Class HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the class HBNBCommand"""
    intro = 'Welcome to HOlberton BNB, type help or ? to list commands.\n'
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exits the Console by typing 'quit'"""
        exit()

    def do_EOF(self, arg):
        """Exits the Console by typing 'ctr + d'"""
        exit()

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
