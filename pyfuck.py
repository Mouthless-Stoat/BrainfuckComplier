import os


def runBFcode(sourceCode: str = "main.bf", runFile: bool = True, debugMode: bool = False, memoryStringLenght: int = 10, cycleCap: int = 10000, noCap: bool = False):

    os.system('cls' if os.name == 'nt' else 'clear')  # clear the terminal

    # region Important stuff to read bf code pls don't edit
    # get program file name
    if runFile:
        codeFile = open(sourceCode, "r")
        code = codeFile.read()
    else:
        code = sourceCode

    # make some varible to help read bf code
    memoryString = []
    for i in range(memoryStringLenght):
        memoryString.append(0)

    pointerPos = 0  # pointer position
    readerPos = 0
    outputStr = ""

    # get the bf code and remove all the space for easy reading
    for char in code:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_:;'\"\?`~=\n ":
            code = code.replace(char, "")
    # endregion

    # region Stuff for debugging Log file, etc
    logFile = open("Log.txt", "w")
    logFile.write(f"Source Code: {sourceCode}\n\n")
    print(f"Executing Code: {code}")  # print the code
    print(f"Amount of Command Executing: {len(code)}")
    # endregion

    if noCap:
        cycleCap = 100
        
    cycle = 1

    while readerPos < len(code) and cycle < cycleCap:

        command = code[readerPos]

        # have a check for every command to do do stuff
        if command == ">":
            pointerPos += 1  # move the pointer to the right
            if pointerPos >= len(memoryString):
                memoryString.append(0)

        elif command == "<":
            pointerPos -= 1  # move the pointer to the left

        elif command == "+":
            memoryString[pointerPos] += 1  # add value at pointer postion

        elif command == "-":
            memoryString[pointerPos] -= 1  # take value at pointer position

        elif command == "[":
            # check if value at pointer position to find the other brace to end the loop
            if memoryString[pointerPos] == 0:
                open_braces = 1
                while open_braces > 0:
                    readerPos += 1

                    if code[readerPos] == '[':
                        open_braces += 1

                    elif code[readerPos] == ']':
                        open_braces -= 1

        elif command == "]":
            open_braces = 1
            while open_braces > 0:
                readerPos -= 1
                if code[readerPos] == '[':
                    open_braces -= 1

                elif code[readerPos] == ']':
                    open_braces += 1

            readerPos -= 1

        elif command == ".":
            print(chr(memoryString[pointerPos]), end="")

        elif command == ",":
            i = input("Input: ")
            memoryString[pointerPos] = ord(i[0])

        if debugMode:
            logFile.writelines(
                [f"Cycle: {cycle}\n", f"Command executing: {command}\nReader Position: {readerPos}\nPointer Position: {pointerPos}\n", f"Memory String: {memoryString}\n\n"])

        readerPos += 1
        cycle += 1
        if noCap:
            cycleCap += 1

    logFile.close()
    print(f"Memory String(Final): {memoryString}")
