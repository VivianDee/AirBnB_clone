#!/usr/bin/python3
"""The HBNBCommandLine class"""

import cmd
import sys
import inspect
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Simple hbnb command interpreter"""

    prompt = "(hbnb) "
    __my_models = {}
    __classes = ['BaseModel', 'User',
                 'Place', 'State', 'City', 'Amenity', 'Review']

    def precmd(self, arg):
        """stores all object instance in list my_models"""
        storage.reload()
        self.__my_models = storage.all()
        info = arg.split('.')
        info_len = len(info)
        if info[0] in self.__classes and info[1] == 'all()':
            self.all(info[0])
            arg = ''
        elif info[0] in self.__classes and info[1] == 'count()':
            self.count(info[0])
            arg = ''
        elif info_len > 1 and info[1].startswith("show("):
            self.show(info[0], info[1])
            arg = ''
        elif info_len > 1 and info[1].startswith("destroy("):
            self.destroy(info[0], info[1])
            arg = ''
        elif info_len > 1 and info[1].startswith("update("):
            self.update(info[0], info[1])
            arg = ''
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
        arg1 = arg.split()
        if len(arg1) <= 0:
            print("** class name missing **")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            if arg == 'BaseModel':
                model = BaseModel()
            elif arg == 'User':
                model = User()
            elif arg == 'Place':
                model = Place()
            elif arg == 'State':
                model = State()
            elif arg == 'City':
                model = City()
            elif arg == 'Amenity':
                model = Amenity()
            elif arg == 'Review':
                model = Review()
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
            args = arg.split()
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

    def do_update(self, arg, check=False):
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
            attr_name = args[2].strip('"')
            if not check and type(arg[3]) == str:
                attr_value = args[3].strip('["')
            elif check and type(arg[3]) == str:
                attr_value = args[3].strip('"')
            else:
                attr_value = args[3]
            if attr_value.isdigit():
                attr_value = int(attr_value)
            setattr(result, attr_name, attr_value)
            storage.new(result)
            storage.save()

    def check_args(self, arg):
        """Checks all arguments"""
        storage.reload()
        self.__my_models = storage.all()
        if arg:
            info = arg.split()
            count = len(self.__my_models)
            check = 0
            if count and info[0] not in self.__classes:
                print("** class doesn't exist **")
                return
            for key, model in self.__my_models.items():
                count = count - 1
                my_key = key.split('.')
                my_class = my_key[0]
                my_id = my_key[1]
                if info[0] in self.__classes:
                    check = check + 1
                    if len(info) < 2:
                        print("** instance id missing **")
                        break
                    if my_id == info[1]:
                        return model
                    elif info[1] and count == 0:
                        print("** no instance found **")
            if check == 0:
                print("** no instance found **")
        else:
            print("** class name missing **")
        return False

    def all(self, arg):
        """Retrieve all instances of a class"""
        self.do_all(arg)

    def count(self, arg):
        """Retrieve the number of instances of a class"""
        count = 0
        for k, v in self.__my_models.items():
            if k.startswith(arg):
                count = count + 1
        print(count)

    def show(self, arg1, arg2):
        """Retrieve an instance based on its ID"""
        input_string = arg2
        start_index = input_string.find('"') + 1
        end_index = input_string.find('"', start_index)
        my_id = input_string[start_index:end_index]
        arg = ' '.join([str(arg1), my_id])
        self.do_show(arg)

    def destroy(self, arg1, arg2):
        """Destroy an instance based on its id"""
        input_string = arg2
        start_index = input_string.find('"') + 1
        end_index = input_string.find('"', start_index)
        my_id = input_string[start_index:end_index]
        arg = ' '.join([str(arg1), my_id])
        self.do_destroy(arg)

    def update(self, arg1, arg2):
        """Update an instance based on its id"""
        input_string = arg2
        attrs = input_string.split("(")[1].split(")")[0]
        attr_list = [i.strip() for i in attrs.split(",")]
        arg = arg1
        for i in attr_list:
            i = i.strip('"')
            arg = ' '.join([str(arg), i])
        self.do_update(arg, True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
