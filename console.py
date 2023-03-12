#!/usr/bin/python3

"""Module implements command line interface for manipulating objects"""

from models.base_model import BaseModel
from models.patients import Patient
from models.drugs import Drug
from models.payments import Payment
from models.engine.file_storage import FileStorage
import cmd
import models

classes = {"Patient": Patient, "Drug": Drug, "Payment": Payment}

class Console(cmd.Cmd):
    """Class Console implements command line interface for manipulating objects"""
    prompt = "HealthBridge$ "

    def do_quit(self, args):
        """Exits cmd interface"""
        print("Bye")
        print("Thank you for using HealthBridge")
        quit()

    def do_help(self, args):
        """renders help to user"""

    def preloop(self):
        print("Hello and Welcome to HealthBridge")
        print("A user-friendly and comprehensive Hospital Management System software solution that can address the needs of hospitals and improve their operations")

    def emptyline(self):
        """Continue to next prompt"""
        pass

    def do_all(self, args):
        """returns all objects in storage"""
        print(models.storage.all())

    def do_create(self, args):
        """creates objects and saves them to storage"""
        try:
            if len(args) == 0:
                print("Please enter Class Name to create Object")
            arguments = args.split(" ")
            if arguments[0] not in classes:
                print("**Invalid Class**")
                return
            if len(arguments) == 1:
                obj = eval(arguments[0])()
                obj.save()
                return
        except Exception:
            pass
    def do_destroy(self, args):
        """Deletes object from storage"""

if __name__ == "__main__":
    Console().cmdloop()
