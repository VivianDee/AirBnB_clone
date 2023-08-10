#!/usr/bin/python3

import cmd
import sys
import json
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """Simple hbnb command interpreter"""


    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = args[0] + '.' + args[1]
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            Print("** no instance found **")
    def do_destroy(self, arg):
        """Delete an Instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = args[0] + '.' + args[1]
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""
        all_objs = storage.all()
        if not arg:
            print([str(v) for v in all_objs.values()])
        elif arg in storage.classes.keys():
            print([str(v) for k, v in all_objs.items() if k.startswith(arg)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = args[0] + '.' + args[1]
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = all_objs[obj_key]
        if hasattr(obj, attr_name):
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
