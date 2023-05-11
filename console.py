import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, args):
        """End of file handler
        """
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()