#!/usr/bin/python3

import cmd
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
