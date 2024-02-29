#I get it. Lots of imports.
import time
from multiprocessing import Process, Queue
from datetime import datetime
from tkinter import *
import os
import sys
import subprocess
from getpass import getpass
global speedtestimport
speedtestimport = 0
global inputopen
global inputpip1
global inputpip2
global commandtorun
global now
try:
    import speedtest
    print("Speedtest imported.")
    speedtestimport += 1
except:
    print("Could not import speedtest.")
#Unneeded loading screen. Intended to simulate actual loading.
devfile = "devsettings.txt"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
errorthrown = 0
print("Welcome to Vanva Terminal v.1.3x")
print("Copyright (c) 2021-2024 WG481")
print("Provided under license.")
print(" ")
def logo():
    print(" ___      ___ ________  ________   ___      ___ ________      ")
    print("|\\  \\    /  /|\\   __  \\|\\   ___  \\|\\  \\    /  /|\\   __  \\     ")
    print("\\ \\  \\  /  / | \\  \\|\\  \\ \\  \\\\ \\  \\ \\  \\  /  / | \\  \\|\\  \\    ")
    print(" \\ \\  \\/  / / \\ \\   __  \\ \\  \\\\ \\  \\ \\  \\/  / / \\ \\   __  \\   ")
    print("  \\ \\    / /   \\ \\  \\ \\  \\ \\  \\\\ \\  \\ \\    / /   \\ \\  \\ \\  \\  ")
    print("   \\ \\__/ /     \\ \\__\\ \\__\\ \\__\\\\ \\__\\ \\__/ /     \\ \\__\\ \\__\\ ")
    print("    \\|__|/       \\|__|\\|__|\\|__| \\|__|\\|__|/       \\|__|\\|__| ")
    print("")
    print('Github Canary Warning: This is a build of canaryTerminal, which has features that are not wholeheartedly tested.')
    global devfile
    if os.path.exists(devfile):
        with open(devfile, "r") as f:
            if f.read(1) == "1":
                print("Development Settings are enabled due to Development Bypass.")  
logo()
# This ungodly mixture of code you see here is an attempt at savefile.txt activation. Basically, a product key activation system designed to create a savefile.
# The biggest issue is that the activation could always be fudged via savefile.txt having a 1 written to it by itself, so I'm deciphering other methods like
# saving a string of numbers unique to the product itself. I wish myself good luck with that.
def main():
    global file_path
    file_path = "savefile.txt"
    if check_activation(file_path):
        while True:
            terminal()
        pass
    else:
        prod_key = input('Enter product key: ')
        if prod_key == "18333792D1CF9":
            with open(file_path, "w") as f:
                f.write("SSdg61Daj6bghLd1Wyxu")
            print("Product activation successful!")
            print('')
            main()
        elif prod_key == "Devpass":
            with open(file_path, "w") as f:
                f.write("SSdg61Daj6bghLd1Wyxu")
            global devfile
            with open(devfile, "w") as f:
                f.write("1")
            print("Development bypass enabled.")
            print('')
            main()
        else:
            print("Failed. Try again.")
            print('')
            main()
#This does what it says. Checks savefile.txt for important data.
def check_activation(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f: 
            return f.read(20) == "SSdg61Daj6bghLd1Wyxu"
    return False
#This is the basic terminal function. 
def terminal():
    input1 = input("Ready for command >>>: ")
    if input1 == "help":
        print(" ")
        print("                   ~~~Vanva Help Command~~~")
        print(" ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+ CHANGELOG - Prints update notes.                            +")
        print("+ ECHO - Echoes some text that is inputted into a window.     +")
        print("+ HELP - Prints help text.                                    +")
        print("+ HELP OPEN - Prints OPEN syntax.                             +")
        print("+ OPEN - Allows you to open a file by entering a path.        +")
        print("+ OPEN WINDOW - Opens a sample window.                        +")
        print("+ TIME - Prints the time.                                     +")
        print("+ VER INFO - Prints the version info of your build.           +")
        print("+ DEACTIVATE - Deactivates the software for testing purposes, +")
        print("+ and can run alone or with two arguments: DEVPASS and ALL,   +")
        print("+ which deactivate Development Bypass, or everything.         +")
        print("+ CLS - Clears the screen. Add argument /nl for no logo.      +")
        print("+ OSC - Runs an OS level command.                             +")
        print("+ HELP OSC - Prints information for OSC.                      +")
        print("+ INTERNET - Prints internet download and upload.             +")
        print("+ PIP - Installs a package with PIP2.                         +")
        print("+ CODECS - Prints available Codecs.                           +")
        print("+ END - Ends your Vanva session.                              +")
        print("+                                                             +")
        print("+ You may also type a Codec Invocation command to run a       +")
        print("+ specific Codec in your installation folder.                 +")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif input1 == "changelog":
        print("~~~Changes have been made to Vanva since your last installation.~~~")
        print("NEW FEATURES:")
        print("PIP is now available! Install a Python 3 module right from Vanva Terminal!")
        print("(Requires PIP3, a stable internet connection, and Python 3.)")
        print("NEW MODULES (Python 3 Module Imports):")
        print("SUBPROCESS has been added for the OPEN command to run on macOS and Linux.")
        print("NEW BUGFIXES:")
        print("OPEN command now has three modes: NT, DARWIN, and OTHER.")
        print(" - NT Mode operates through the OS module to open.")
        print(" - DARWIN Mode operates through SYS and SUBPROCESS modules, and runs")
        print(" the macOS 'open' command.")
        print(" - OTHER Mode assumes you are on Linux and runs 'xdg-open' through")
        print(" the SYS and SUBPROCESS modules.")
        print("INTERNET checks for the SPEEDTEST-CLI module to prevent errors.")
        print("")
        print("~~~Python 3.x Support!~~~")
        print("Now introducing the Xenolith builds :)")
        print("Xenolith is the tagline for any Python 3 build at this moment.")
        print("Soon, stable releases of Python 3 editions will come out, and 2.7")
        print("will be served its obsolescence it so deserves after its long years")
        print("of service. Xenolith builds are ports of Canary, sans all of the")
        print("Codec loading. Xenolith will soon have ports of Mainline and Codec,")
        print("just to please the masses.")
    elif input1 == "time":
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
    elif input1 == "open window":
        root = Tk()
        root.geometry("500x500")
        root.title('Vanva Terminal')
        btn1 = Button(root, text="Pointless Button", command=root.destroy).pack()
    elif input1 == "end":
        print("Ending Vanva processes...")
        time.sleep(1)
        print("Closing Vanva files and windows...")
        time.sleep(2)
        print("Closing Terminal process...")
        time.sleep(3)
        quit()
    elif input1 == "help osc":
        print("~~~ OSC HELP ~~~")
        print("OSC is a command used to run OS-level commands directly through the terminal.")
        print("As of now, and command using SUDO is not supported nor reccommended.")
        print("This feature is used at your own risk, and we are not responsible for any")
        print("damages caused by running OS-level commands.")
        print(" ")
    elif input1 == "osc":
        oscinput = input('Enter OS command: ')
        os.system(oscinput)
    elif input1 == "cls":
        clear()
        logo()
    elif input1 == "cls /nl":
        clear()
    elif input1 == "open":
        inputopen = input("Path to the file? >>>: ")
        if os.name == 'nt':
            
            os.startfile(inputopen)
        elif sys.platform == "darwin":
            
            subprocess.call(["open", inputopen])
        else:
            
            subprocess.call(["xdg-open", inputopen])
    elif input1 == "help open":
        print("An example of how to use open: open *click enter* c:/program files/VXZLTD/terminal/terminal.exe")
        print("Make sure you know the file path, make it lowercase, and use / instead of \\, ok?")
    elif input1 == "ver info":
        print("~~~Vanva Terminal v.1.3x Update~~~")
        print("          Xenolith Build          ")
        print("")
        print("Written using Notepad++, VSCode, IDLE.")
        print("Programmed in Python 3.")
        print("Programmed, Edited, and Tested by LatinDiacritics.")
        print("Product Key: 18333792D1CF9")
        print("Development Bypass support: Yes")
        print("This build is a port of canaryTerminal from Python 2.7 to Python 3.x.")
        print("Features still remain unstable, and still require testing before an")
        print("official release of 1.3/1.4 is ported to Python 3 for LTS.")
        print("")
        print("Vanva Terminal is a concept for an easy to use terminal. Its purpose is to eliminate the")
        print("the verbosity of the difficult-to-use Microsoft Command Prompt and PowerShell. Certain")
        print("commands provide Unix support, but the main purpose is to eliminate the complexity of")
        print("using the Microsoft Windows terminal when commands need to be run. At the moment, though,")
        print(".localized")
    elif input1 == "internet":
        if speedtestimport == 1:
            print("Attempting an Internet Speed Test...")
            print("This should take about 30 seconds.")
            try:
                st = speedtest.Speedtest()
                downloadspeed = int(st.download()) / 1000000
                uploadspeed = int(st.upload()) / 1000000
                print("Download speed: ", downloadspeed, " Mbps.")
                print("Upload speed: ", uploadspeed, " Mbps.")
                if downloadspeed > 50 and downloadspeed < 70:
                    print("Your internet speed is good. You should be able to stream HD")
                    print("video off of one device without too many problems.")
                elif downloadspeed > 70 and downloadspeed < 120:
                    print("Your internet speed is great! You should be able to handle a load")
                    print("of multiple devices streaming HD video without any problems.")
                elif downloadspeed > 120:
                    print("Your internet speed is amazing! Downloading mass amounts of files")
                    print("while streaming HD video should be ok!")
                elif downloadspeed < 50:
                    print("Your internet speed is poor. HD video playback will be a problem.")
                print("")
            except:
                print("")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("An error occured while checking your network connection!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("")
                print("ERROR DETAILS:")
                print("Type: connection_failed")
                print("Name: Internet Connection")
                print("")
                print("Please check your internet connection and try again later.")
                print("")
        else:
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("An error occured while checking your network connection!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            print("ERROR DETAILS:")
            print("Type: process_failed_no_code")
            print("Name: Speedtest")
            print("")
            print("Enter pip, 1, speedtest-cli. Then, restart Vanva. (Refer to each , as a time you press enter.)")
    elif input1 == "pip":
        inputpip1 = "1"
        inputpip2 = "null"
        commandtorun = "null"
        print("Please choose an option:")
        print("1. Install")
        print("2. Uninstall")
        inputpip1 = str(input("Enter option: "))
        if inputpip1 == "1":
            inputpip2 = input("Module to install: ")
            commandtorun = str("pip3 install " + inputpip2)
            os.system(commandtorun)
        elif inputpip1 == "2":
            inputpip2 = input("Module to uninstall: ")
            commandtorun = str("pip3 uninstall" + inputpip2)
            os.system(commandtorun)
        else:
            print("Please enter a valid number.")
    elif input1 == "deactivate":
        os.remove(file_path)
        clear()
        print("Running deactivation...")
        time.sleep(2)
        print("Deactivation success. Now restarting the software...")
        time.sleep(2)
        clear()
        logo()
        main()
    elif input1 == "deactivate devpass":
        try:
            os.remove(devfile)
            print("Deactivating your Development Bypass settings...")
            time.sleep(2)
            print("Deactivation success. Now restarting the software...")
            time.sleep(2)
            clear()
            logo()
            main()
        except:
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("An error occured while deactivating your software!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            print("ERROR DETAILS:")
            print("Type: failed_deactivation_attempt")
            print("Name: devsettings.txt")
            print(" ")
            print("There is no Development Bypass to deactivate. This command")
            print("will not function unless you have Development Bypass enabled.")
            print("")
    elif input1 == "deactivate all":
        clear()
        try:
            print("Deactivating your Development Bypass settings...")
            time.sleep(2)
            os.remove(devfile)
            print("Success.")
            print("Running deactivation...")
            time.sleep(2)
            os.remove(file_path)
            print("The software has been deactivated. Now restarting for the change to take effect...")
            time.sleep(2)
            clear()
            logo()
            main()
        except:
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("An error occured while deactivating your software!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            print("ERROR DETAILS:")
            print("Type: failed_deactivation_attempt")
            print("Name: devsettings.txt")
            print("")
            print("To solve this problem, run standalone DEACTIVATE.")
            print("")
    elif input1 == "echo":
        inputecho = input("Echo what? >>>:")
        root = Tk()
        root.title('Vanva Terminal Tkinter Window')
        text1 = Text(root)
        text1.insert(INSERT, inputecho)
        text1.pack()
    #Surprise to those of you who read the source code:
    #VanvaX may be returning. I need to figure out dev processes, but I'll find a way to return it cuz it's fun.
    else:
        print("Invalid command. Type 'help' for command list or try again.")
#This loops the code forever until quit() is ran.
while True:
    main()
