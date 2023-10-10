#!/usr/bin/python3
"""Defines a Class HBNBCommand"""

import cmd
import re
import shlex
from datetime import datetime
from models import storage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command processor class."""

    prompt = '(hbnb) '

    allowed_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel."""
        args = shlex.split(line)
        if not args:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = shlex.split(line)
        if not args:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[0], args[1])
            inst_data = storage.all().get(key)
            if not inst_data:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(line)
        if not args:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[0], args[1])
            inst_data = storage.all().get(key)
            if not inst_data:
                print('** no instance found **')
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representations of all
        instances based on the class name."""
        args = shlex.split(line)
        objs = storage.all()
        if not args:
            print([str(objs[obj]) for obj in objs])
        elif args[0] in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute."""
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[0], args[1])
            inst_data = storage.all().get(key)
            if not inst_data:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                storage.save()

    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update."""
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)
        return value

    def get_objects(self, instance=''):
        """Gets the elements created by the console."""
        objects = storage.all()
        if instance:
            return [str(val)
                    for key, val in objects.items()
                    if key.startswith(instance)]
        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """Handles unrecognized commands."""
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]
            if class_name in self.allowed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)

    def emptyline(self):
        """Handles an empty line input."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
