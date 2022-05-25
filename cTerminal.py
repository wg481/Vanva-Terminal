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
clear()
errorthrown = 0
print "Welcome to Vanva Terminal v.1.0b"
print "Copyright (c) 2021 WG481"
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
    print " ___      ___  _____    _____  ________     "
    print "|\  \    /  /|/ __  \  / __  \|\   __  \    "
    print "\ \  \  /  / /\/_|\  \|\/_|\  \ \  \|\ /_   "
    print " \ \  \/  / /\|/ \ \  \|/ \ \  \ \   __  \  "
    print "  \ \    / /__    \ \  \ __\ \  \ \  \|\  \ "
    print "   \ \__/ /\__\    \ \__\\__\ \__\ \_______\ "
    print "    \|__|/\|__|     \|__\|__|\|__|\|_______|"
    print ""
    print ""
    print 'Github Beta Warning: This is a beta version downloaded from Github. Features may crash.'
    print 'Codec Warning: Requires a Codec and two Codec Identifiers.'
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
def check_codecs():
    try:
        cdec1 = "codec1.txt"
        with open(cdec1, 'r') as f:
            global cdec1
            global codec1
            codec1 = f.read(20)
        in_cdec1 = "codec1inv.txt"
        with open(in_cdec1, 'r') as f:
            global in_cdec1
            global invokecodec1
            invokecodec1 = f.read(20)
    except:
        global errorthrown
        if errorthrown == 0:
            global invokecodec1
            invokecodec1 = "null"
            print "An error occured!"
            print "Codecs could not be loaded."
            errorthrown += 1
#This is the basic terminal function. 
def terminal():
    global cdec1
    global codec1
    global invokecodec1
    global in_cdec1
    check_codecs()
    input1 = raw_input("Ready for command >>>: ")
    if input1 == "help":
        print " "
        print "                   ~~~Vanva Help Command~~~"
        print " "
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "+ CHANGELOG - Prints update notes.                            +"
        print "+ ECHO - Echoes some text that is inputted into a window.     +"
        print "+ HELP - Prints help text.                                    +"
        print "+ HELP OPEN - Prints OPEN syntax.                             +"
        print "+ OPEN - Allows you to open a file by entering a path.        +"
        print "+ OPEN WINDOW - Opens a sample window.                        +"
        print "+ TIME - Prints the time.                                     +"
        print "+ VER INFO - Prints the version info of your build.           +"
        print "+ DEACTIVATE - Deactivates the software for testing purposes. +"
        print "+ CLS - Clears the screen. Add argument /nl for no logo.      +"
        print "+ OSC - Runs an OS level command.                             +"
        print "+ HELP OSC - Prints information for OSC.                      +"
        print "+ CODECS - Prints available Codecs.                           +"
        print "+ VANVAX - Run a depricated developer mode.                   +"
        print "+ END - Ends your Vanva session.                              +"
        print "+                                                             +"
        print "+ You may also type a Codec Invocation command to run a       +"
        print "+ specific Codec in your installation folder.                 +"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    elif input1 == "changelog":
        print "~~~Changes have been made to Vanva since your last installation.~~~"
        print "New version! Version 1.1b is available as part of a Beta software progam made available by Vanva."
        print "Added a new feature: Codecs! A Codec is file which can be natively ran by the software. For more"
        print "information, type 'help codecs'."
        print "Codecs can now be run using a single line command, and are pre-read and set up as commands the"
        print "moment you start Vanva Terminal."
    elif input1 == "codecs":
        try:
            global codec1
            global invokecodec1
            print "Indexing Codecs..."
            time.sleep(2)
            print " "
            print " " 
            print " The following Codec files have been found:"
            print "~~~~"
            print " "
            print codec1, "invoked with", invokecodec1, "command."
            print " "
            print "~~~~"
        except:
            print "An error occured while checking your Codecs. A Codec may be broken, missing, or nonexistent."
            print "Please make sure all Codecs are installed the same directory as the Terminal itself."
            print " "
    elif input1 == invokecodec1:
        global codec1
        os.startfile(codec1)
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
        print "~~~Vanva Terminal v.1.1b Codec Update~~~"
        print "Created in Notepad++, a free source code editor and Notepad replacement that supports several languages."
        print "Coded in Python 2.7."
        print "Coded, Edited, and Tested by WG481."
        print "Your build was developed as part of a program. This version still"
        print "is incompleted and requires you, the tester, to give support and rating"
        print "to determine how to better the program for the future. Insider testing"
        print "reports should be sent via email to wg481official@gmail.com. We thank you"
        print "for being a part of the Vanva Terminal Insider testing group."
    elif input1 == "deactivate":
        os.remove(file_path)
        print "The activation file has been deleted. Restart the software for it to take effect."
    elif input1 == "echo":
        inputecho = raw_input("Echo what? >>>:")
        root = Tk()
        root.title('Vanva Terminal Tkinter Window')
        text1 = Text(root)
        text1.insert(INSERT, inputecho)
        text1.pack()
    #VanvaX. The (currently deprecated) developer process, has been deleted.
    else:
        print "Invalid command. Type 'help' for command list or try again."
#This loops the code forever until quit() is ran.
while True:
    main()
