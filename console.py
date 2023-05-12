import cmd
from models.base_model import BaseModel
from models import storage


class ArgumentError(Exception):
    pass


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    existing_objs = storage.all()

    def cmdloop(self):
        try:
            super().cmdloop()
        except ArgumentError:
            self.cmdloop()

    def parse_arguments(self, args):
        return tuple(args.split())

    def validate_argument_class_name(self, command, args):
        supported_classes = ('BaseModel')
        if len(args) == 0 and command != 'all':
            print("** class name missing **")
            raise ArgumentError("class name missing")
        if command != 'all' and args[0] not in supported_classes:
            print("** class doesn't exist **")
            raise ArgumentError("class doesn't exist")

    def validate_argument_id(self, command: str, args: tuple):
        if len(args) < 2:
            print("** instance id missing **")
            raise ArgumentError("instance id missing")
        if f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            raise ArgumentError("no instance found")

    def validate_argument_attribute_name(self, command, args):
        if len(args) < 3:
            print("** attribute name missing **")
            raise ArgumentError("attribute name missing")

    def validate_argument_attribute_value(self, command, args):
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """End of file handler
        """
        return True

    def do_create(self, args):
        args = self.parse_arguments(args)
        self.validate_argument_class_name("create", args)
        new = eval(f"{args[0]}()")
        new.save()
        print(new.id)

    def do_show(self, args):
        args = self.parse_arguments(args)
        self.validate_argument_class_name("show", args)
        self.validate_argument_id("show", args)
        obj = eval(f"{args[0]}(**self.existing_objs['{args[0]}.{args[1]}'])")
        print(obj)

    def do_destroy(self, args):
        args = self.parse_arguments(args)
        self.validate_argument_class_name("destroy", args)
        self.validate_argument_id("destroy", args)
        del self.existing_objs[args[0] + "." + args[1]]
        storage.save()

    def do_all(self, args):
        args = self.parse_arguments(args)
        if len(args) >= 1:
            self.validate_argument_class_name("all", args)
        class_name = "" if len(args) < 1 else args[0]
        instance_list = []
        for key, value in self.existing_objs.items():
            if key.startswith(class_name):
                print(f"{value['__class__']}(**value)")
                instance_list.append(
                    str(
                        eval(f"{value['__class__']}(**value)")
                    )
                )
        print(instance_list)

    def do_update(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
