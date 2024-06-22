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
        if len(args.split()) != 4:
            self.do_help('create_note')
        print(args)

    def do_create_task(self, args):
        if len(args.split()) != 4:
            self.do_help('create_task')
        print(args)

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
