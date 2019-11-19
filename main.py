#!/usr/bin/env python3

from os import chdir
from subprocess import call

def reorder_menu():

    print("Reorder Menu:\n\n [1] Reorder Desktop\n [2] Reorder Documents\n [3] Reorder Downloads\n [4] Back")
    command = int(input("\nOperation# "))

    if (command == 1):
        import reorder
        reorder.Reorder(1)
    elif (command == 2):
        import reorder
        reorder.Reorder(1)
    elif (command == 3):
        import reorder
        reorder.Reorder(1)
    else:
        intro()

def intro():

    call('clear', shell=True)
    print("\n<==============================>")
    print("<====== Files Automation ======>")
    print("<==============================>\n")

    selection = int(input("Menù:\n\n (1) Reorder\n (2) Settings\n (3) Exit \n\nOperation# "))

    if (selection == 1):
        reorder_menu()
        call('clear', shell=True)
        intro()
    elif (selection == 2):
        print("\n<====== Settings Documentation ======>")
        print("\nIf you want to change a variable the process is really simple. \nOpen the Projects Folder and edit the config.py file, afther that select the value that you want to change and write the new value .\nWhen you finish the modification, save the file and close it.")

        command = int(input("\nClick Any Number for Exit# "))
        if (command == 1):
            intro()
        else:
            intro()

    else:
        exit(0)

if __name__ == "__main__":
	intro()
