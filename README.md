# Pyfuck
The a fun little Project I did yesterday use to run BF code

The program will run Brainfuck code <br>
You can learn brainfuck here: https://en.wikipedia.org/wiki/Brainfuck <br>
Or watch this very good video about making an AI: https://www.youtube.com/watch?v=qK0vmuQib8Y&t=149s

## How to use writen by me
###### I'm not good at explaining or making a doc so I gonna try my best
You can import this module by just put pyfuck.py in your python project folder
and type `from pyfuck import runBFCode`

Ok so I don't want to waste your time so there a `ReadMePls.txt` goes with the project which is a faster version of this page and some example too. So just skip this whole page and start working. Anyway let start with the How to use part

This project only add 1 single module to your python project it **runBFcode()** <br>
What this function will do it excatly what is say run BF either internaly using a string or externaly using a file

The function take in **2 require argument** and **4 optional argument**

### Require Argument
- `runFile` (bool) Default = True <br>
Use to let the program to know if it open a file or run directly using a string

- `sourceCode` (str) Default = "main.bf" <br>
Take diffence thing dependenly on runFile:
    - if `runFile` is `True` input the external bf file name.
    - if `runFile` is `False` input the bf code string.
    
### Optional Argument
- `debugMode` (bool) Default = `True` <br>
If True make a log file containing the following:
    - How many cycle the program have do.
    - What command it executing at a certain cycle.
    - What the reader position at a certain cycle.
    - What the pointer position at a certain cycle.
    - What the memory string at a certain cycle.
    
###### P.S: It make the program run slower so if that program kinda heavy or long then it will prob crash the editor ur using

- `memoryStringLenght` (int) Default = 10 <br>
the lenght of the memory string 

###### P.S: this isn't very important because if it out of index it add it own cell to the memory string

- `cycleCap` (int) Default = 10000 <br>
The amount of cycle the program can do before stopping ***ignore if `noCap` = `True`***

- `noCap` (bool) Default = `False` <br>
If `True` ignore `cycleCap` and the program run until it done 

###### P.S: U can turn this one if ur certain thatt the program will stop if not it gonna run forever prob crash the editor ur using

## Usage
### Example: using internal BF code
```python
from pyfuck import runBFcode

sourceCode = "+++[>+++ <-]"
runBFcode(runFile=False, sourceCode=sourceCode)
```
You can also add `debugMode=True` in the argument list to create a log file to help debugging the BF code like this: 
```python
from pyfuck import runBFcode

sourceCode = "+++[>+++ <-]"
runBFcode(runFile=False, sourceCode=sourceCode, debugMode=True)
```
Which then give you a log file something like this:
```text
Source Code: +++[>+++ <-]

Cycle: 1
Command executing: +
Reader Position: 0
Pointer Position: 0
Memory String: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Cycle: 2
Command executing: +
Reader Position: 1
Pointer Position: 0
Memory String: [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### Example: using external BF file
Here a Brainfuck file name idk.bf:
```bf
+++
[
    >+++
    <-
]
```
You can run the file using this in your python file:
```python
from pyfuck import runBFcode

runBFcode(runFile=true, sourceCode="idk.bf")
```
Just like running BF code internaly you can add `debugMode=True` to the argument list to get log file like this:
```text
Source Code: +++[>+++ <-]

Cycle: 1
Command executing: +
Reader Position: 0
Pointer Position: 0
Memory String: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Cycle: 2
Command executing: +
Reader Position: 1
Pointer Position: 0
Memory String: [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

You can also add in `noCap=True`, `memoryStringLenght = 10000` or `cycleCap = 10` to customize it to do what you want <br>
The project come with a `example.bf` and `example.py` to get you started 
