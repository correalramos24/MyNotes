
import cmd
from domain.transactions import *
from utils.utils import *

class NoteShell(cmd.Cmd):
    intro = 'Welcome to the MyNotes CLI. Type help or ? to list commands.\n'
    prompt = '(MyNotes) '
    file = None

    def preloop(self) -> None:
        init_domain()
        return super().preloop()

    def do_list_notes(self,arg):
        list_notes()

    def do_list_tasks(self, args):
        list_tasks()

    def do_create_note(self, args):
        print(args)

    def do_create_note_from_file(self, args):
        'create_note_from_file <file_path>'
        if len(args.split()) != 1:
            self.do_help('create_note_from_file')
        else:
            create_note_from_file(Path(args))    

    def do_exit(self, args):
        'Finish the CLI'
        return True

    def do_enable_verbose(self, args):
        'Disable verbose'
        setLogging(False)
    
    def do_enable_verbose(self, args):
        'Enable verbose'
        setLogging(True)

if __name__ == '__main__':
    NoteShell().cmdloop()