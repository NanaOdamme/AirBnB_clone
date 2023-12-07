#!/usr/bin/python3
"""command line interpreter for modules."""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """main class for cmd"""

    prompt = "(hbnb) "

    def default(self, arg):
        """defaults if the commands isn't found."""
        self._precmd(arg)

    def do_EOF(self, arg):
        """Handles EOF character."""
        print()
        return True

    def do_quit(self, arg):
        """quits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def _precmd(self, arg):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        className = match.group(1)
        method = match.group(2)
        args = match.group(3)
        found_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if found_uid_and_args:
            uid = found_uid_and_args.group(1)
            attr_dict = found_uid_and_args.group(2)
        else:
            uid = args
            attr_dict = False

        attr_value = ""
        if method == "update" and attr_dict:
            found_dict = re.search('^({.*})$', attr_dict)
            if found_dict:
                self.update_dict(className, uid, found_dict.group(1))
                return ""
            found_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_dict)
            if found_attr_and_value:
                attr_value = (found_attr_and_value.group(
                    1) or "") + " " + (found_attr_and_value.group(2) or "")
        comm = method + " " + className + " " + uid + " " + attr_value
        self.onecmd(comm)
        return comm

    def update_dict(self, className, uid, string_dict):
        """method for update() with a dictionary."""
        s = string_dict.replace("'", '"')
        data = json.loads(s)
        if not className:
            print("** class name missing **")
        elif className not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(className, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[className]
                for attribute, value in data.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_create(self, arg):
        """method to create an instance."""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """shows the string representation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance using class name and id."""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if arg != "":
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instance_list = [str(obj) for key, obj in storage.all().items()
                                 if type(obj).__name__ == args[0]]
                print(instance_list)
        else:
            instance_list = [str(obj) for key, obj in storage.all().items()]
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute."""
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        className = match.group(1)
        uid = match.group(2)
        attr = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif className not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(className, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attr:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                patch = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        patch = float
                    else:
                        patch = int
                else:
                    value = value.replace('"', '')
                attribute = storage.attributes()[className]
                if attr in attribute:
                    value = attribute[attr](value)
                elif patch:
                    try:
                        value = patch(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attr, value)
                storage.all()[key].save()

    def do_count(self, arg):
        """method to count the instances of a class."""
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            found = [
                key for key in storage.all() if key.startswith(
                    args[0] + '.')]
            print(len(found))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
