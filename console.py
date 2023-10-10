#!/usr/bin/python3
"""Defines a Class HBNBCommand"""
import cmd
"""import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review"""


class HBNBCommand(cmd.Cmd):
    """ Defines the class HBNBCommand"""
    intro = 'Welcome to HOlberton BNB, type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exits the Console by typing 'quit'"""
        return True

    def do_EOF(self, arg):
        """Exits the Console by typing 'ctr + d'"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
