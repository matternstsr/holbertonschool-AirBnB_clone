#!/usr/bin/python3
"""Defines a Class HBNBCommand"""
import cmd
from models import BaseModel
from models import User
from models import State
from models import City
from models import Amenity
from models import Place
from models import Review

class HBNBCommand(cmd.Cmd):
    """ Defines the class HBNBCommand"""
    intro = 'Welcome to HOlberton BNB, type help or ? to list commands.\n'
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exits the Console by typing 'quit'"""
        return True

    def do_EOF(self, arg):
        """Exits the Console by typing 'ctr + d'"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""

        splarg = arg.split()
        if len(splarg) == 0:
            print("**class name missing**")
        elif splarg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            for key, value in HBNBCommnad.__classes.items():
                if splarg[0] == key:
                    splarg[0] = value
            print(eval(splarg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints a string represention of class and id"""

        splarg = arg.split()
        saved_inst = storage.all()
        if len(splarg) == 0:
            print("**class name missing**")
        elif len(splarg) < 2:
            print("** instance id missing **")
        elif splarg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        for key, value in HBNBCommnad.__classes.items():
                if splarg[0] == key:
                    splarg[0] = value
        if "{}.{}".format(splarg[0], splarg[1]) not in saved_inst.keys:
            print("** no instance found **")
        else:
            print(saved_inst[{}.{}.format(splarg[0], splarg[1])])

    def do_destroy(self, arg):
        """Deletes a specified instance of an Object"""

        splarg = arg.split()
        saved_inst = storage.all()
        if len(splarg) == 0:
            print("**class name missing**")
        elif len(splarg) < 2:
            print("** instance id missing **")
        elif splarg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        for key, value in HBNBCommnad.__classes.items():
                if splarg[0] == key:
                    splarg[0] = value
        if "{}.{}".format(splarg[0], splarg[1]) not in saved_inst.keys:
            print("** no instance found **")
        else:
            del saved_inst[{}.{}.format(splarg[0], splarg[1])]
            storage.save()

    def do_all(self, arg):
        """Prints a list of all instances of all classes, or all
            instances of a specified class"""

    splarg = arg.split()
    inst_list = []
    if len(splarg) > 0:
        if splarg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:





if __name__ == '__main__':
    HBNBCommand().cmdloop()
