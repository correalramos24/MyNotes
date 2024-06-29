import cmd
from app.domain.transactions import *
from app.utils.my_logging import *

class NoteShell(cmd.Cmd):
    intro = 'Welcome to the MyNotes CLI. Type help or ? to list commands.\n'
    prompt = '(MyNotes) '
    file = None

    def preloop(self) -> None:
        init_domain()
        return super().preloop()

    @staticmethod
    def do_list_tasks(args):
        list_tasks()

    @staticmethod
    def do_list_notes(args):
        list_notes()

    def do_create_note(self, args):
        log[0](f"create note with args {args}\n")
        if len(args.split()) != 4:
            self.do_help('create_note')
            return

    def do_create_task(self, args):
        """
        create_task name;description[;deadline;init_state;priority]
        - It is mandatory to set the name, you can leave empty the others
        """
        log[0](f"create note with args {args}\n")
        arg_list = args.split(';')
        if len(arg_list) < 3 or len(arg_list) > 7 or arg_list[0] == '':
            self.do_help('create_task')
            return
        try:
            create_task(*args.split(';'))
        except Exception as e:
            print(e)

    def do_create_note_from_file(self, args):
        """create_note_from_file <file_path>"""

        if len(args.split()) != 1:
            self.do_help('create_note_from_file')
        else:
            create_note_from_file(Path(args))

    @staticmethod
    def do_exit(args):
        """Finish the CLI"""
        return True

    @staticmethod
    def do_disable_verbose(args):
        """Disable verbose"""
        setLogging(False)

    @staticmethod
    def do_enable_verbose(args):
        """Enable verbose"""
        setLogging(True)


if __name__ == '__main__':
    NoteShell().cmdloop()
