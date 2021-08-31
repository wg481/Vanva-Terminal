#I get it. Lots of imports.
import time
from multiprocessing import Process, Queue
from datetime import datetime
from Tkinter import *
import os
import sys
import msvcrt
from getpass import getpass
#Unneeded loading screen. Intended to simulate actual loading.
print "Welcome to Vanva Terminal v.1.0b"
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
print ''
print "+++++++++++++++++++++++++++++"
print "+ \    /  _____             +"
print "+  \  /     |               +"
print "+   \/ anva |erminal v.1.0b +"
print "+++++++++++++++++++++++++++++"
print''
# This ungodly mixture of code you see here is an attempt at savefile.txt activation. Basically, a product key activation system designed to create a savefile.
# The biggest issue is that the activation could always be fudged via savefile.txt having a 1 written to it by itself, so I'm deciphering other methods like
# saving a string of numbers unique to the product itself. I wish myself good luck with that.
def main():
    file_path = "savefile.txt"
    if check_activation(file_path):
        while True:
            terminal()
        pass
    else:
        prod_key = getpass('Enter product key: ')
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
        print "CHANGELOG ~~~ Prints update notes."
        print "ECHO ~~~ Echoes some text that is inputted into a window."
        print "END ~~~ Ends your Vanva session."
        print "HELP ~~~ Prints help text."
        print "HELP OPEN ~~~ Prints OPEN syntax."
        print "OPEN ~~~ Allows you to open a file by entering a path."
        print "OPEN WINDOW ~~~ Opens a sample window."
        print "TIME ~~~ Prints the time."
        print "VER INFO ~~~ Prints the version info of your build."
        print "Quick note, don't type in CAPITALS. All of them are lowercase."
    elif input1 == "changelog":
        print "Bug fixes. Added extended developer support. Imported new modules. More bug fixes."
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
    elif input1 == "open":
        inputopen = raw_input("Path to the file? >>>: ")
        os.startfile(inputopen)
    elif input1 == "help open":
        print "An example of how to use open: open *click enter* c:/program files/VXZLTD/terminal/terminal.exe"
        print "Make sure you know the file path, make it lowercase, and use / instead of \, ok?"
    elif input1 == "ver info":
        print "~~~Vanva Terminal v.1.0b Github Update~~~"
        print "Created in Notepad++, a free source code editor and Notepad replacement that supports several languages."
        print "Coded in Python 2.7."
        print "Coded, Edited, and Tested by Van M. Russell."
        print "Installer compiled to .EXE by NSIS and zip2exe."
        print ".PY file Compiled to .EXE by auto-py-to-exe."
        print "Your build was developed as part of a program. This version still"
        print "is incompleted and requires you, the tester, to give support and rating"
        print "to determine how to better the program for the future. Insider testing"
        print "reports should be sent via email to wg481official@gmail.com. We thank you"
        print "for being a part of the Vanva Terminal Insider testing group."
    elif input1 == "echo":
        inputecho = raw_input("Echo what? >>>:")
        root = Tk()
        root.title('Vanva Terminal Tkinter Window')
        text1 = Text(root)
        text1.insert(INSERT, inputecho)
        text1.pack()
    #VanvaX. The developer process.
    elif input1 == "VanvaX":
        usernameX = ''
        print "Username: "
        while True:
            y = msvcrt.getch()
            if y == '\r':
                break;
            sys.stdout.write('~')
            usernameX +=y
        passwordX = ''
        print ''
        print 'Password: '
        while True:
            x = msvcrt.getch()
            if x == '\r':
                break;
            sys.stdout.write('~')
            passwordX +=x
        if passwordX == "Gypsy" and usernameX == "Developer":
            print ''
            print "Welcome to VanvaX Beta v.0.5"
            while True:
                input2 = raw_input("Enter your VanvaX command >>>: ")
                if input2 == "help":
                    #VanvaX is odd. I haven't put much work into it.
                    print "~~~VanvaX Commands~~~"
                    print "HELP ~~~ Shows help for commands."
                    print "VXVER ~~~ Shows VanvaX version."
                    print "NSIS ~~~ Opens NSIS. (Requires NSIS Installed)"
                    print "EXIT ~~~ Ends your VanvaX session."
                elif input2 == "NSIS":
                    os.startfile('c:/program files/nsis/nsis.exe')
                elif input2 == "exit":
                    print "Ending VanvaX session..."
                    time.sleep(2)
                    print "Closing VanvaX files..."
                    time.sleep(2)
                    print "Exiting VanvaX..."
                    time.sleep(2)
                    break;
                elif input2 == "vxver":
                    print "\    /" 
                    print " \  /    \/"
                    print "  \/ anva/\  Version Beta 0.5"
                    print "The Vanva Terminal Developer Mode"
                    print "Coded in Python 2.7"
                    print "Coded, Edited, and Tested by Van M. Russell"
                else:
                    print "Unrecognized command."
        else:
            print "Password incorrect."
    #This else took for ever to get the placement.
    else:
        print "Invalid command. Type 'help' for command list or try again."
#This loops the code forever until quit() is ran.
while True:
    main()
    
