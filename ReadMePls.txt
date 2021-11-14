The program will complier Brainfuck code
U can learn brainfuck here: https://en.wikipedia.org/wiki/Brainfuck
Or watch this very good video about making an AI: https://www.youtube.com/watch?v=qK0vmuQib8Y&t=149s
I'm not good at explaining or making a doc so I gonna try my best

You can import this module just put main.py in ur python project folder

HOW TO USE writen by u/IdkIWhyIHaveAReddit

The function to run bf code (runBFCode)take in 2 required argument and 4 optional argument for debuging:

Required argument:
runFile (bool): Default = True
it use to let the function know to open a file or run directly using a string

SourceCode (string): Default = "main.bf"
it take diffence thing dependenly on runFile
    if runFile is True input the external bf file name.
    if runFile is False input the bf code string.

Optional argument:
debugMode (bool): Default = True
if True make a log file containing the following:
    How many cycle the program have do.
    What command it executing at a certain cycle.
    What the reader position at a certain cycle.
    What the pointer position at a certain cycle.
    What the memory string at a certain cycle.
P.S: It make the program run slower so if that program kinda heavy or long then it will prob crash the editor ur using

memoryStringLenght (int): Default = 100
the lenght of the memory string 
P.S: this isn't very important because if it out of index it add it own cell to the memory string


cycleCap (int): Default = 10000
The amount of cycle the program can do before stopping ignore if noCap = True

noCap (bool): Default = False
If True ignore cycleCap and the program run until it done 
P.S: U can turn this one if ur certain taht the program will stop if not it gonna run forever prob crash the editor ur using
