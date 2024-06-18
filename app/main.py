#!/bin/python3

from utils.utils import *
from domain.transactions import *


def main():
    init_persistance("/home/vcorreal/MyNotes")
    create_note('MyMeetingNote', "Nan", "plain")
    list_notes()



if __name__ == "__main__":
    setLogging(True)
    log[0]("MAIN START\n")
    main()
    log[0]("MAIN END\n")