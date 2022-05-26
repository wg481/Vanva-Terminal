#I get it. Lots of imports.
import time
from multiprocessing import Process, Queue
from datetime import datetime
from Tkinter import *
import os
import sys
from getpass import getpass
#Unneeded loading screen. Intended to simulate actual loading.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print "Welcome to Vanva Terminal v.1.1"
print "Copyright (c) 2021-2022 WG481"
print "Provided under license."
print "Unpacking files..."
print ''
time.sleep(2)
print "Reading through files..."
print ''
time.sleep(1)
print "Files ready."
print ''
print "Please wait while Vanva loads..."
time.sleep(3)
clear()
def logo():
    print " ___      ___ ________  ________   ___      ___ ________      "
    print "|\  \    /  /|\   __  \|\   ___  \|\  \    /  /|\   __  \     "
    print "\ \  \  /  / | \  \|\  \ \  \\ \  \ \  \  /  / | \  \|\  \    "
    print " \ \  \/  / / \ \   __  \ \  \\ \  \ \  \/  / / \ \   __  \   "
    print "  \ \    / /   \ \  \ \  \ \  \\ \  \ \    / /   \ \  \ \  \  "
    print "   \ \__/ /     \ \__\ \__\ \__\\ \__\ \__/ /     \ \__\ \__\ "
    print "    \|__|/       \|__|\|__|\|__| \|__|\|__|/       \|__|\|__| "
    print " _________  _______   ________  _____ ______   ___  ________   ________  ___            "
    print "|\___   ___\\  ___ \ |\   __  \|\   _ \  _   \|\  \|\   ___  \|\   __  \|\  \           "
    print "\|___ \  \_\ \   __/|\ \  \|\  \ \  \\\__\ \  \ \  \ \  \\ \  \ \  \|\  \ \  \          "
    print "     \ \  \ \ \  \_|/_\ \   _  _\ \  \\|__| \  \ \  \ \  \\ \  \ \   __  \ \  \         "
    print "      \ \  \ \ \  \_|\ \ \  \\  \\ \  \    \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \        "
    print "       \ \  \ \ \  \_|\ \ \  \\  \\ \  \    \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \____   "
    print "        \ \__\ \ \_______\ \__\\ _\\ \__\    \ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\ "
    print "         \|__|  \|_______|\|__|\|__|\|__|     \|__|\|__|\|__| \|__|\|__|\|__|\|_______| "
    print ""
logo()
# This ungodly mixture of code you see here is an attempt at savefile.txt activation. Basically, a product key activation system designed to create a savefile.
# The biggest issue is that the activation could always be fudged via savefile.txt having a 1 written to it by itself, so I'm deciphering other methods like
# saving a string of numbers unique to the product itself. I wish myself good luck with that.
def main():
    file_path = "savefile.txt"
    global file_path
    if check_activation(file_path):
        while True:
            terminal()
        pass
    else:
        prod_key = raw_input('Enter product key: ')
        if prod_key == "18333792D1CF9":
            with open(file_path, "w") as f:
                f.write("SSdg61Daj6bghLd1Wyxu")
            print "Product activation successful!"
            print ''
            main()
        else:
            print "Failed. Try again."
            print ''
            main()
#This does what it says. Checks savefile.txt for important data.
def check_activation(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f: 
            return f.read(20) == "SSdg61Daj6bghLd1Wyxu"
    return False
#This is the basic terminal function. 
def terminal():
    input1 = raw_input("Ready for command >>>: ")
    if input1 == "help":
        print " "
        print "                   ~~~Vanva Help Command~~~"
        print " "
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "+ CHANGELOG - Prints update notes.                            +"
        print "+ ECHO - Echoes some text that is inputted into a window.     +"
        print "+ END - Ends your Vanva session.                              +"
        print "+ HELP - Prints help text.                                    +"
        print "+ HELP OPEN - Prints OPEN syntax.                             +"
        print "+ OPEN - Allows you to open a file by entering a path.        +"
        print "+ OPEN WINDOW - Opens a sample window.                        +"
        print "+ TIME - Prints the time.                                     +"
        print "+ VER INFO - Prints the version info of your build.           +"
        print "+ CLS - Clears the screen. Add argument /nl for no logo.      +"
        print "+ OSC - Runs an OS level command.                             +"
        print "+ HELP OSC - Prints information for OSC.                      +"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    elif input1 == "changelog":
        print "~~~Changes have been made to Vanva since your last installation.~~~"
        print "The not long awaited 1.1 build comes to the official Terminal release!"
        print "This build includes the new OSC feature, which allows the user to run"
        print "operating system level commands (bash, batch, or zsh) with the terminal!"
        print ""
        print "This build also supports CLS, a new command to clear the screen,"
        print "which utilizes the same framework as OSC."
        print ""
        print "The long time deprecated VanvaX feature has been removed. Commands"
        print "like NSIS are planned for future installations of Vanva, but"
        print "VanvaX will remain removed from Vanva Terminal officially."
    elif input1 == "time":
        print strftime("%Y-%m-%d %H:%M:%S", localtime())
    elif input1 == "open window":
        root = Tk()
        root.geometry("500x500")
        root.title('Vanva Terminal')
        btn1 = Button(root, text="Pointless Button", command=root.destroy).pack()
    elif input1 == "end":
        print "Ending Vanva processes..."
        time.sleep(1)
        print "Closing Vanva files and windows..."
        time.sleep(2)
        print "\    /  _____"
        print " \  /     | "
        print "  \/ anva |erminal closing..."
        time.sleep(3)
        quit()
    elif input1 == "help osc":
        print "~~~ OSC HELP ~~~"
        print "OSC is a command used to run OS-level commands directly through the terminal."
        print "As of now, and command using SUDO is not supported nor reccommended."
        print "This feature is used at your own risk, and we are not responsible for any"
        print "damages caused by running OS-level commands."
        print " "
    elif input1 == "osc":
        oscinput = raw_input('Enter OS command: ')
        os.system(oscinput)
    elif input1 == "cls":
        clear()
        logo()
    elif input1 == "cls /nl":
        clear()
    elif input1 == "open":
        inputopen = raw_input("Path to the file? >>>: ")
        os.startfile(inputopen)
    elif input1 == "help open":
        print "An example of how to use open: open *click enter* c:/program files/VXZLTD/terminal/terminal.exe"
        print "Make sure you know the file path, make it lowercase, and use / instead of \, ok?"
    elif input1 == "ver info":
        print "~~~Vanva Terminal v.1.1 Update~~~"
        print "Created in Notepad++, a free source code editor and Notepad replacement that supports several languages."
        print "Coded in Python 2.7."
        print "Coded, Edited, and Tested by WG481."
        print "Installer compiled to .EXE by NSIS and zip2exe."
        print ".PY file Compiled to .EXE by auto-py-to-exe."
        print "This is an official Vanva Terminal build. This is not part of any Beta program."
    elif input1 == "echo":
        inputecho = raw_input("Echo what? >>>:")
        root = Tk()
        root.title('Vanva Terminal Tkinter Window')
        text1 = Text(root)
        text1.insert(INSERT, inputecho)
        text1.pack()
    else:
        print "Invalid command. Type 'help' for command list or try again."
#This loops the code forever until quit() is ran.
while True:
    main()
