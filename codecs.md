# Codecs
A Codec is an individual Python program which can be run by the Terminal using special pointers.

## How do I use them?
Codec support is limited to the cTerminal release of Vanva Terminal. Right now, only 1 Codec is supported until a later update.
Make sure Python is set as the default source for CDEC files.
You'll need 3 files.
1. (filename).cdec - This is a Python script which has had its file extension changed to CDEC.
2. codec1.txt - This is a text file in which the only contents should be (filename).cdec. View the example Codec for more information.
3. codec1inv.txt - This is a text file in which there should only be one word. Upon entering that word into the terminal, your Codec should run.
Put these files in the same directory as cTerminal.py, then run the command "codecs" to see if the codec loaded correctly.

## How do I make one?
1. Make a Python 2.7 script and name it anything you want. It can perform any function. Example: text.py
2. Change the file extention of your script from .py to .cdec. Example: text.cdec
3. Create a codec1.txt and on the first line type the filename of your script.
4. Create a codec1inv.txt file and on the first line type one word you want to use to invoke the command. Example: text
5. Put the Codec and its associated text files in the same directory as cTerminal.py and run cTerminal.py.
6. Use the command "codecs" to see if your Codec appears.
