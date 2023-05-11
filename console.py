import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def parse_arguments(self, args):
        return tuple(map(str, args.split()))
    
    def validate_arguments(self, command, args):
        supported_classes = ('BaseModel')
        args = self.parse_arguments(args)
        if len(args) == 0 and command != 'all':
            print("** class name missing **")
            return False
        if command != 'all' and args[0] not in supported_classes:
            print("** class doesn't exist **")
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
        if self.validate_arguments("create", args):
            new = BaseModel()
            new.save()
            print(new.id)
    
    def do_show(self, args):
        pass
    
    def do_destroy(self, args):
        pass
    
    def do_all(self, args):
        pass
    
    def do_update(self, args):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
