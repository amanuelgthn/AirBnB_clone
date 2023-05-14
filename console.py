#!/usr/bin/python3
"""
Module that dontains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb)"

        # Define the commands
        self.do_quit = self.do_quit
        self.EOF = self.do_quit
        self.help = self.help

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
