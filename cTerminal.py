#I get it. Lots of imports.
import time
from multiprocessing import Process, Queue
from datetime import datetime
from Tkinter import *
import os
import sys
import subprocess
from getpass import getpass
try:
    import speedtest
    print "Speedtest imported."
except:
    print "Could not import speedtest."
#Unneeded loading screen. Intended to simulate actual loading.
devfile = "devsettings.txt"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
errorthrown = 0
print "Welcome to Vanva Terminal v.1.3c"
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
    print 'Github Canary Warning: This is a build of canaryTerminal, which has features that are not wholeheartedly tested.'
    print 'Codec Warning: This build features Codecs.'
    global devfile
    if os.path.exists(devfile):
        with open(devfile, "r") as f:
            if f.read(1) == "1":
                print "Development Settings are enabled due to Development Bypass."  
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
        elif prod_key == "Devpass":
            with open(file_path, "w") as f:
                f.write("SSdg61Daj6bghLd1Wyxu")
            global devfile
            with open(devfile, "w") as f:
                f.write("1")
            print "Development bypass enabled."
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
        print "+ DEACTIVATE - Deactivates the software for testing purposes, +"
        print "+ and can run alone or with two arguments: DEVPASS and ALL,   +"
        print "+ which deactivate Development Bypass, or everything.         +"
        print "+ CLS - Clears the screen. Add argument /nl for no logo.      +"
        print "+ OSC - Runs an OS level command.                             +"
        print "+ HELP OSC - Prints information for OSC.                      +"
        print "+ INTERNET - Prints internet download and upload.             +"
        print "+ CODECS - Prints available Codecs.                           +"
        print "+ END - Ends your Vanva session.                              +"
        print "+                                                             +"
        print "+ You may also type a Codec Invocation command to run a       +"
        print "+ specific Codec in your installation folder.                 +"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    elif input1 == "changelog":
        print "~~~Changes have been made to Vanva since your last installation.~~~"
        print "NEW MODULES (Python 2.7 Module Imports):"
        print "SUBPROCESS has been added for the OPEN command to run on macOS and Linux."
        print "NEW BUGFIXES:"
        print "OPEN command now has three modes: NT, DARWIN, and OTHER."
        print " - NT Mode operates through the OS module to open."
        print " - DARWIN Mode operates through SYS and SUBPROCESS modules, and runs"
        print " the macOS 'open' command."
        print " - OTHER Mode assumes you are on Linux and runs 'xdg-open' through"
        print " the SYS and SUBPROCESS modules."
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
        print "Closing Terminal process..."
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
        if os.name == 'nt':
            global inputopen
            os.startfile(inputopen)
        elif sys.platform == "darwin":
            global inputopen
            subprocess.call(["open", inputopen])
        else:
            global inputopen
            subprocess.call(["xdg-open", inputopen])
    elif input1 == "help open":
        print "An example of how to use open: open *click enter* c:/program files/VXZLTD/terminal/terminal.exe"
        print "Make sure you know the file path, make it lowercase, and use / instead of \, ok?"
    elif input1 == "ver info":
        print "~~~Vanva Terminal v.1.3c Update~~~"
        print "Created in Notepad++, a free source code editor and Notepad replacement that supports several languages."
        print "Coded in Python 2.7."
        print "Coded, Edited, and Tested by WG481."
        print "This is a build of canaryTerminal. Features remain thoroughly untested."
    elif input1 == "internet":
        print "Attempting an Internet Speed Test..."
        print "This should take about 30 seconds."
        try:
            st = speedtest.Speedtest()
            downloadspeed = int(st.download()) / 1000000
            uploadspeed = int(st.upload()) / 1000000
            print "Download speed: ", downloadspeed, " Mbps."
            print "Upload speed: ", uploadspeed, " Mbps."
            if downloadspeed > 50 and downloadspeed < 70:
                print "Your internet speed is good. You should be able to stream HD"
                print "video off of one device without too many problems."
            elif downloadspeed > 70 and downloadspeed < 120:
                print "Your internet speed is great! You should be able to handle a load"
                print "of multiple devices streaming HD video without any problems."
            elif downloadspeed > 120:
                print "Your internet speed is amazing! Downloading mass amounts of files"
                print "while streaming HD video should be ok!"
            elif downloadspeed < 50:
                print "Your internet speed is poor. HD video playback will be a problem."
            print ""
        except:
            print ""
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "An error occured while checking your network connection!"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print ""
            print "ERROR DETAILS:"
            print "Type: connection_failed"
            print "Name: Internet Connection"
            print ""
            print "Please check your internet connection and try again later."
            print ""
    elif input1 == "deactivate":
        os.remove(file_path)
        clear()
        print "Running deactivation..."
        time.sleep(2)
        print "Deactivation success. Now restarting the software..."
        time.sleep(2)
        clear()
        logo()
        main()
    elif input1 == "deactivate devpass":
        try:
            os.remove(devfile)
            print "Deactivating your Development Bypass settings..."
            time.sleep(2)
            print "Deactivation success. Now restarting the software..."
            time.sleep(2)
            clear()
            logo()
            main()
        except:
            print ""
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "An error occured while deactivating your software!"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print ""
            print "ERROR DETAILS:"
            print "Type: nonexistent_file_deletion_attempt"
            print "Name: devsettings.txt"
            print " "
            print "There is no Development Bypass to deactivate. This command"
            print "will not function unless you have Development Bypass enabled."
            print ""
    elif input1 == "deactivate all":
        clear()
        try:
            print "Deactivating your Development Bypass settings..."
            time.sleep(2)
            os.remove(devfile)
            print "Success."
            print "Running deactivation..."
            time.sleep(2)
            os.remove(file_path)
            print "The software has been deactivated. Now restarting for the change to take effect..."
            time.sleep(2)
            clear()
            logo()
            main()
        except:
            print ""
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "An error occured while deactivating your software!"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print ""
            print "ERROR DETAILS:"
            print "Type: nonexistent_file_deletion_attempt"
            print "Name: devsettings.txt"
            print ""
            print "To solve this problem, run standalone DEACTIVATE."
            print ""
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
