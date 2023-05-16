#!/usr/bin/python3
"""
Module that dontains the entry point of the command interpreter
"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    def __init__(self, **kwargs):
        """
        initialiazation
        """
        super().__init__()
        self.prompt = "(hbnb)"
        self.classes = ["BaseModel"]
        self.do_quit = self.do_quit
        self.EOF = self.do_quit
        self.help = self.help
        self.do_create = self.do_create
        self.do_show = self.do_show
        self.do_all = self.do_all
        self.do_destroy = self.do_destroy
        self.do_update = self.do_update

    def do_quit(self, *args):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        print("EOF")
        exit()

    def help(self, *args):
        """Prints the help message."""
        print("Available commands:")
        for cmd in self.commands.keys():
            print("  " + cmd)

    def emptyline(self):
        """Do nothing on an empty line."""
        return

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON)
        and prints the id
        """
        if len(args) == 1:
            print("** class name missing **")
        else:
            try:
                new_obj = eval(args)()
                models.storage.new(new_obj)
                models.storage.save()
                print(new_obj.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, *args):
        """
        print the string representation of an instance
        based on the class name and id
        """
        arguments = str(args[0]).split()
        if len(args) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        key = arguments[0] + "." + arguments[1]
        try:
            obj = (models.storage.all())[key]
            print(obj.__str__())
        except KeyError:
            print("** no instance found **")

    def do_all(self, *args):
        """
        print all string representation of all instances based or
        not on the class name
        """
        objects = models.storage.all()
        arguments = str(args[0]).split()
        list_obj = []
        if len(args) == 0:
            for key, value in objects.items():
                list_obj.append(value.__str__())
        elif arguments:
            if arguments[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for key, value in objects.items():
                if type(value) is arguments[0]:
                    list_obj.append(value.__str__())

    def do_update(self, *args):
        """
        update
        """
        arguments = str(args[0]).split()
        if len(args) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        elif len(arguments) < 3:
            print("** attribute name missing **")
            return
        elif len(arguments) < 4:
            print("** value missing **")
            return
        key = arguments[0] + "." + arguments[1]
        try:
            objects = models.storage.all()[key]
            setattr(objects, arguments[2], arguments[3])
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, *args):
        """
        destroy
        """
        arguments = str(args[0]).split()
        if len(args) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        key = arguments[0] + "." + arguments[1]
        try:
            models.storage.remove(key)
            models.storage.save()
        except KeyError:
            print("** no instance found **")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
