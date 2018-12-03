# |OO 	      _
# |OO 	   . | |
# |   \/   | |_|
#     /
# By: Ari Stehney
# Shell IO Library for Python3
# 
# Classes:
#	colors
#	command
#	fill
#	programcontrol

import sys
import os
import time
 
class colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    black = '\033[0m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    def printcolor(strText, colorName="", bold=False, underlineon=False):
        #if bold==True:
        #colorStr += '\033[1m'
        #if underlineon==True:
        #colorStr += '\033[4m'
        colorStr = ""
        colorStr = colorStr + str(colorName)
        colorStr = colorStr + strText
        colorStr = colorStr + '\033[0m'
        print(colorStr)


class command:
    def runcommand(command):
        os.system(command)

    def checkcommand(command):
        os.system("man -k " + command)

class programcontrol:
    def showerror(error):
        print("\033[1m\033[91m" + error + "\033[0m")
        sys.exit()

    def getargument(argn):
        return sys.argv[argn+1]

    def waitenter(choice):
        print("press enter to " + choice)
        input("")

class fill:
    header = '\e[48;5;95m'
    blue = '\e[48;5;94m'
    green = '\e[48;5;92m'
    red = '\e[48;5;93m'
    error = '\e[48;5;91m'
    black = '\e[48;5;0m'
    endc = '\e[48;5;0m'
    bold = '\e[48;5;1m'
    undeline = '\e[48;5;4m'
    def changefill(colorName):
        os.system('printf "' + colorName + '"')
