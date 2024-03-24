#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file, and prints the id"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name"""
        args = shlex.split(arg)
        objs = storage.all()
        if len(args) < 1:
            print([str(obj) for obj in objs.values()])
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        filtered_objs = [str(obj) for key, obj in objs.items() if key.startswith(class_name)]
        print(filtered_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3]
        obj = objs[key]
        try:
            value = eval(value)
        except:
            pass
        setattr(obj, attribute, value)
        storage.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        command, *args = shlex.split(line)
        if len(args) == 2 and command in ["User", "BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            if args[0] == "show" and len(args[1]) > 2 and args[1][0] == '"' and args[1][-1] == '"':
                self.do_show(command + " " + args[1][1:-1])
                return
            elif args[0] == "destroy" and len(args[1]) > 2 and args[1][0] == '"' and args[1][-1] == '"':
                self.do_destroy(command + " " + args[1][1:-1])
                return
        super().default(line)

    def do_count(self, class_name):
        """Counts the number of instances of a class"""
        objs = storage.all()
        count = sum(1 for key in objs.keys() if key.startswith(class_name + "."))
        print(count)

    def do_update_from_dict(self, arg):
        """Updates an instance based on the class name and id with a dictionary"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            update_dict = eval(args[2])
            if not isinstance(update_dict, dict):
                raise ValueError
        except (NameError, ValueError):
            print("** invalid dictionary **")
            return
        obj = objs[key]
        for key, value in update_dict.items():
            setattr(obj, key, value)
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        sys.exit()

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        sys.exit()
