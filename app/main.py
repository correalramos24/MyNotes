#!/bin/python3

from utils.utils import *
from domain.transactions import *
from frontend.NotesShell import *


def main():
    
    #create_note('MyMeetingNote', "Nan", "plain")
    #list_notes()
    NoteShell().cmdloop()




if __name__ == "__main__":
    setLogging(True)
    log[0]("MAIN START\n")
    main()
    log[0]("MAIN END\n")