#!/usr/bin/python3

import cmd
import sys
import json
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """Simple hbnb command interpreter"""


    prompt = "(hbnb) "
    __my_models = {}
    __classes = ['BaseModel']

    def precmd(self, arg):
        """stores all object instance in list my_models"""
        storage.reload()
        self.__my_models = storage.all()
        return arg

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
        arg1 = arg.split( )
        if len(arg1) <= 0:
            print("** class name missing **")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            if arg == 'BaseModel':
                model = BaseModel()
            model.save()
            print(model.id)
            storage.reload()
            self.__my_models = storage.all()

    def do_show(self, arg):
        """Print the string representation of an instance"""
        result = self.check_args(arg)
        if result:
            print(result)

    def do_destroy(self, arg):
        """Delete an Instance"""
        result = self.check_args(arg)
        if result:
            args = arg.split( )
            all_objs = storage.all()
            obj_key = args[0] + '.' + args[1]
            if obj_key in all_objs:
                del all_objs[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""
        storage.reload()
        all_objs = storage.all()
        if not arg:
            print([str(v) for v in all_objs.values()])
        elif arg in self.__classes:
            print([str(v) for k, v in all_objs.items() if k.startswith(arg)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute"""
        result = self.check_args(arg)
        if result:
            args = arg.split()
            all_objs = storage.all()
            obj_key = args[0] + '.' + args[1]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(result, attr_name, attr_value)
            result.save()
            storage.reload()
            self.__my_models = storage.all()

    def check_args(self, arg):
        """Checks all arguments"""
        if arg:
            info = arg.split( )
            check = 0
            count = len(self.__my_models)
            for key, model in self.__my_models.items():
                count = count - 1
                my_key = key.split('.')
                my_class = my_key[0]
                my_id = my_key[1]
                if my_class == info[0]:
                    check = check + 1
                    if len(info) < 2:
                        print("** instance id missing **")
                        break
                    if my_id == info[1]:
                        return model
                    elif info[1] and count == 0:
                        print("** no instance found **")
            if check == 0:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
