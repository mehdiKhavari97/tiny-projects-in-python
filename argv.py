"""" Getting input from cmd
First index ([0]) is for the file name so, we start from [1]
"""
import sys

firstInput = int(sys.argv[1])
secondInput = int(sys.argv[2])

print(firstInput + secondInput)