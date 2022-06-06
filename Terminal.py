#I get it. Lots of imports.
import time
from multiprocessing import Process, Queue
from datetime import datetime
from Tkinter import *
import os
import sys
import subprocess
from getpass import getpass
global speedtestimport
speedtestimport = 0
try:
    import speedtest
    speedtestimport += 1
except:
    uselessvariable = 1
#Unneeded loading screen. Intended to simulate actual loading.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print "Welcome to Vanva Terminal v.1.2"
print "Copyright (c) 2021-2022 WG481"
print "Provided under license."
print ""
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
        print "+ OPEN - Allows you to open a file by entering a path.        +"
        print "+ OPEN WINDOW - Opens a sample window.                        +"
        print "+ TIME - Prints the time.                                     +"
        print "+ VER INFO - Prints the version info of your build.           +"
        print "+ DEACTIVATE - Deactivates the software for testing purposes. +"
        print "+ CLS - Clears the screen. Add argument /nl for no logo.      +"
        print "+ OSC - Runs an OS level command.                             +"
        print "+ HELP OSC - Prints information for OSC.                      +"
        print "+ INTERNET - Prints internet download and upload.             +"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    elif input1 == "changelog":
        print "~~~Changes have been made to Vanva since your last installation.~~~"
        print "NEW FEATURES:"
        print "Added DEACTIVATE, a feature to remove your savefile."
        print "Added INTERNET, a feature which checks your internet download and upload"
        print "speeds. INTERNET requires the SPEEDTEST-CLI module to run, and will not"
        print "function without it."
        print "NEW BUGFIXES:"
        print "Removed the loading screen."
        print "OPEN command now has three modes: NT, DARWIN, and OTHER."
        print " - NT Mode operates through the OS module to open."
        print " - DARWIN Mode operates through SYS and SUBPROCESS modules, and runs"
        print "   the macOS 'open' command."
        print " - OTHER Mode assumes you are on Linux and runs 'xdg-open' through"
        print "   the SYS and SUBPROCESS modules."
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
        if os.name == 'nt':
            global inputopen
            os.startfile(inputopen)
        elif sys.platform == "darwin":
            global inputopen
            subprocess.call(["open", inputopen])
        else:
            global inputopen
            subprocess.call(["xdg-open", inputopen])
    elif input1 == "ver info":
        print "~~~Vanva Terminal v.1.1~~~"
        print "Made using Notepad++ and Visual Studio Code."
        print "Coded in Python 2.7."
        print "Coded, Edited, and Tested by WG481."
    elif input1 == "internet":
        if speedtestimport == 1:
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
        else:
            print ""
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "An error occured while checking your network connection!"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print ""
            print "ERROR DETAILS:"
            print "Type: module_unavailable"
            print "Name: Speedtest Module"
            print ""
            print "Please use PIP2 to install speedtest-cli for Python 2.7."
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
