#!/usr/bin/python3
"""
Module that dontains the entry point of the command interpreter
"""


import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


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
        self.classes = ["BaseModel", "User", "Amenity",
                        "City", "Place", "Review", "State"]
        self.do_quit = self.do_quit
        self.EOF = self.do_quit
        self.help = self.help
        self.do_create = self.do_create
        self.do_show = self.do_show
        self.do_all = self.do_all
        self.do_destroy = self.do_destroy
        self.do_update = self.do_update
        self.do_count = self.do_count

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

    def do_create(self, *args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON)
        and prints the id
        """
        arguments = str(args[0]).split(" ")
        if arguments[0] == "":
            print("** class name missing **")
            return
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            key = eval(arguments[0])()
            models.storage.new(key)
            models.storage.save()
            print(key.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """
        print the string representation of an instance
        based on the class name and id
        """
        arguments = str(args[0]).split(" ")
        if arguments[0] == "":
            print("** class name missing **")
            return
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
        arguments = str(args[0]).split(" ")
        if arguments[0] not in self.classes and len(arguments[0]) > 0:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        list_obj = []
        if len(arguments[0]) == 0:
            for key, value in objects.items():
                list_obj.append(value.__str__())
        else:
            for key, value in objects.items():
                if value.__class__.__name__ == arguments[0]:
                    list_obj.append(value.__str__())
        print(list_obj)

    def do_update(self, *args):
        """
        update
        """
        arguments = str(args[0]).split(" ")
        if arguments[0] == "":
            print("** class name missing **")
            return
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
        arguments = str(args[0]).split(" ")
        if arguments[0] == "":
            print("** class name missing **")
            return
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
    def do_count(self, *args):
        """
        count
        """
        count = 0
        arguments = str(args[0]).split(" ")
        if arguments[0] == "":
            print("** class name missing **")
            return
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        for key, value in objects.items():
            if value.__class__.__name__ == arguments[0]:
                count +=1
        print(count)
    def default(self, *args):
        """
        when the command line prefix id not recognized
        """
        arguments = str(args[0]).split(".")
        argument = str(arguments[1]).split("(")
        command = ""
        id = ""
        pass_arg = ""
        command = arguments[0] + " " + argument[0]
        if argument[0] in ['show','destroy']:
            id = str(re.findall(r'"(.*?)"', argument[1])[0])
            pass_arg = arguments[0] + " " + id
            eval('self.do_' + argument[0] + '(pass_arg)')
        else:
            eval('self.do_' + argument[0] + '(arguments[0])')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
