#!/usr/bin/python3
"""console module
entry point to the airbnb shell
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Airbnb shell class
    """
    prompt = '(hbnb) '
    existing_objs = storage.all()

    def emptyline(self):
        return False

    def parse_arguments(self, args):
        return shlex.split(args)

    def onecmd(self, line):
        if line.strip().endswith('.all()'):
            return self.do_all(line.split('.')[0])
        if line.strip().endswith('.count()'):
            count = 0
            for key in self.existing_objs:
                if key.startswith(f"{line.split('.')[0]}."):
                    count += 1
            print(count)
            return
        return super().onecmd(line)

    def validate_argument_class_name(self, args):
        supported_classes = (
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review'
            )
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in supported_classes:
            print("** class doesn't exist **")
            return False
        return True

    def validate_argument_id(self, args):
        if len(args) < 2:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return False
        return True

    def validate_argument_attribute_name(self, args):
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        return True

    def validate_argument_attribute_value(self, args):
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """End of file handler
        """
        return True

    def do_create(self, args):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = self.parse_arguments(args)
        if not self.validate_argument_class_name(args):
            return False
        class_name = args[0]
        new = eval(f"{class_name}()")
        new.save()
        print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = self.parse_arguments(args)
        if not self.validate_argument_class_name(args):
            return False
        if not self.validate_argument_id(args):
            return False
        class_name, id = args
        obj = self.existing_objs[f'{class_name}.{id}']
        print(obj)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = self.parse_arguments(args)
        if not self.validate_argument_class_name(args):
            return False
        if not self.validate_argument_id(args):
            return False
        class_name, id = args
        del self.existing_objs[f"{class_name}.{id}"]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        args = self.parse_arguments(args)
        if len(args) >= 1:
            if not self.validate_argument_class_name(args):
                return False
        class_name = "" if len(args) < 1 else args[0]
        instance_list = []
        for key, value in self.existing_objs.items():
            if key.startswith(class_name):
                instance_list.append(str(value))
        print(instance_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = self.parse_arguments(args)
        if not self.validate_argument_class_name(args):
            return False
        if not self.validate_argument_id(args):
            return False
        if not self.validate_argument_attribute_name(args):
            return False
        if not self.validate_argument_attribute_value(args):
            return False
        class_name, id, attribute_name, attribute_value = args
        obj = self.existing_objs[f"{class_name}.{id}"]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
