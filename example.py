from os import truncate
from pyfuck import runBFcode

# this part to run via string you comment 1 of these example out to test
sourceCode = "+++[>+++ <-]"
runBFcode(runFile=False, sourceCode=sourceCode, debugMode=True)

# this part run via file
runBFcode(debugMode=True, sourceCode="example.bf")
