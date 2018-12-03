#!/usr/local/bin/python3
import sys
import os
import time
import random
import crayons
import json
import os.path as pathf

version = "v2.5"
platform = "running on " + "x86_64"

env_var_all = dict()
env_functions_all = dict()
options = dict()

options["1"] = "on"
options["2"] = "on"
options["3"] = "on"

cmdmode = 0
promptchar = "-"
rnarg = False
errocc = False


def prefSaver():
    with open(os.getcwd() + '/birpref', 'w') as outfile:
        json.dump(options, outfile)
        
def prefUpdater():
    with open(os.getcwd() + '/birpref', 'r') as outfile:
        options = json.load(outfile)


def genFEHdr(fne):
    fnHeader = crayons.red("░░░░ birchEditor ░ File: " + fne + " ░░░░", bold=True)
    return fnHeader
def editorMain(fn):
    if options["2"] == "off":
        crayons.disable()
    with open(os.getcwd() + "/" + fn, mode="r") as filereadr:
        filecn = filereadr.read()
    linenum = 0
    filecn4 = filecn
    filecn4 = filecn4.split("\n")
    linenum = len(filecn4)+1
    num = 0
    while True:
        linenum += 1
        os.system('printf "\e[48;5;241m \n"')
        os.system('printf "\e[8;20;46t"')
        clearScreen()
        print(genFEHdr(fn))
        filecn3 = filecn
        filecn3 = filecn3.split("\n")
        filecn2 = "1 "
        j = 0
        while j<len(filecn3):
            if str(filecn3[j]).startswith('^== '):
                filecn3[j] = str(crayons.black(filecn3[j]))
            filecn2 = filecn2 + filecn3[j]+"\n"+crayons.yellow(str(j+2))+" "
            j+=1
        filecn2 = filecn2.replace('prog', str(crayons.green("prog"))).replace('print', str(crayons.blue("print"))).replace('eq', str(crayons.blue("eq"))).replace('stop', str(crayons.yellow("stop"))).replace('debugOff', str(crayons.cyan("debugOff"))).replace('debugOn', str(crayons.cyan("debugOn"))).replace('$', str(crayons.magenta("$"))).replace('+', str(crayons.cyan("+"))).replace('*', str(crayons.cyan("*"))).replace('/', str(crayons.cyan("/"))).replace('-', str(crayons.cyan("-"))).replace('error', str(crayons.cyan("error"))).replace('err', str(crayons.cyan("error")))
        print("\n" + crayons.yellow(filecn2))
        c = input(crayons.yellow(str(linenum) + " ")) # Not fully implemented
        num += 1
        if num==5:
            num = 0
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)
        addf = True
        if c == "****exit":
            os.system('printf "\e[48;5;0m \n"')
            addf = False
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)
            clearScreen()
            sys.exit()

        if c == "****save":
            addf = False
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)

        if c == "****run":
            addf = False
            if options["3"]=="on":
                with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                    filereadr.write(filecn)
                ResizeList(sys.argv, 2, fill_with=0)
                sys.argv[1] = fn
                frmain()
                input("++Press enter to return to editor++")           
            

        if c == "****options":
            addf = False
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)
            clearScreen()
            print(crayons.red("░░░░ birchEditor ░ Edit Settings   ░░░░", bold=True))
            print(crayons.red("Autosave:  " + options["1"] + "                      1  !"))
            print(crayons.red("Color:     " + options["2"] + "                      2 ok"))
            print(crayons.red("Run EDCMD: " + options["3"] + "                      3 ok"))
            setting = input(crayons.yellow("change setting ['number,on/off']: "))
            setting = setting.split(',')
            options[setting[0]] = setting[1].lower()
            prefSaver()

        if c == "****jump":
            addf = False
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)
            clearScreen()
            print(crayons.red("░░░░ birchEditor ░ Jump to Line    ░░░░", bold=True))
            setting = input(crayons.yellow("line number: "))
            print(crayons.cyan("""
Function Not available:
line text processing is in beta""",bold=True))
            time.sleep(2)

        # Cursor Functions
        if c == "^[[A":
            addf = False
            linenum -= 1
        if c == "^[[B":
            addf = False
            linenum += 1
        if c == "^[[D":
            addf = False
            clearScreen()
            print(crayons.yelow("Saved code"))
            with open(os.getcwd() + "/" + fn, mode="w") as filereadr:
                filereadr.write(filecn)
            time.sleep(2)

        if c == "^[[C":
            clearScreen()
            d = input(crayons.yelow("Line Text [raw]: "))
            c=d
            
        if addf==True:
            filecn = filecn + "\n" + c
        

def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns the character of the key that was pressed (zero on
    KeyboardInterrupt which can happen when a signal gets handled)

    """
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    try:
        ret = sys.stdin.read(1) # returns a single character
    except KeyboardInterrupt: 
        ret = 0
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return ret

def clearScreen():
 os.system("clear")

def exprerr():
    print("Error: Expression on line: " + str(line))
    if cmdmode == 1:
        sys.exit()
    errocc = True

def inputerr():
    print("Error: Bad Input")
    if cmdmode == 1:
        sys.exit()
    errocc = True

def varerr():
    print("Error: Unknown Var on line")
    if cmdmode == 1:
        sys.exit()
    errocc = True

def commanderr():
    print("Error: Command on line: " + str(line))
    if cmdmode == 1:
        sys.exit()
    errocc = True

def expr_run(exprall):
    if exprall[0] == "$":
        if exprall[1].lower().isalpha():
            if exprall[1].lower() in env_var_all.keys():
                return env_var_all[exprall[1].lower()]
            else:
                varerr()
                return ""
        else:
            exprerr()
    else:
        ndnum = 0
        cextq = 0
        if exprall[0].isalpha():
            return exprall
        else:
            u = 0
            for g in exprall:
                # If it is a number
                if g.isnumeric():
                    ndnum += 1
                else:
                    cexteq = u
                    break
                u += 1

            if ndnum > 0:
                fnum = ""
                i = 0
                while i <= ndnum-1:
                    fnum += exprall[i]
                    i += 1

                if ndnum == 1:
                    if exprall[cextq-2] == "*":
                        return int(fnum) * int(exprall.split(exprall[cextq+1])[1])
                    if exprall[cextq-2] == "/":
                        return int(fnum) / int(exprall.split(exprall[cextq+1])[1])
                    if exprall[cextq-2] == "+":
                        return int(fnum) + int(exprall.split(exprall[cextq+1])[1])
                    if exprall[cextq-2] == "-":
                        return int(fnum) - int(exprall.split(exprall[cextq+1])[1])
                    if exprall[cextq-2] == "|":
                        return int(fnum) // int(exprall.split(exprall[cextq+1])[1])
                if ndnum == 2:
                    if exprall[cextq+2] == "*":
                        return int(fnum) * int(exprall.split(exprall[cextq-3])[1])
                    if exprall[cextq+2] == "/":
                        return int(fnum) / int(exprall.split(exprall[cextq-3])[1])
                    if exprall[cextq+2] == "+":
                        return int(fnum) + int(exprall.split(exprall[cextq-3])[1])
                    if exprall[cextq+2] == "-":
                        return int(fnum) - int(exprall.split(exprall[cextq-3])[1])
                    if exprall[cextq+2] == "|":
                        return int(fnum) // int(exprall.split(exprall[cextq-3])[1])
            else:
                exprerr()
               

def execLine(linecode):
        rnarg = False
    
        if (' ' in linecode)==False:
            inputerr()

        linec = linecode
        cmdr = linec.split(" ")[0]
        args = linec.split(" ")[1]

        if cmdr == "prt":
            finalassembledstr = ""
            if '_' in args:
                i = 0
                lc2 = args.split("_")
                while i < len(lc2):
                    finalassembledstr = finalassembledstr + lc2[i] + " "
                    i+=1
            else:
                finalassembledstr = expr_run(args)
            print(finalassembledstr)

        if cmdr == "d":
            print("",end="")
        
        if cmdr == "cm":
            os.system(args)

        if cmdr == "sp":
            time.sleep(int(args))

        if cmdr == "prg":
            rnarg = False
            if args[1].split(",")[0]=="stop":
                line = len(lineout)+1
            if args[1].split(",")[0]=="err":
                print("Error on line " + line + ": " + args[1].split(",")[1])
                line = len(lineout)+1
            if args[1].split(",")[0]=="debugOn":
                debug = True
            if args[1].split(",")[0]=="debugOff":
                debug = False

        if cmdr == "eq":           
            env_var_all[args[1]] = expr_run(args.split(",")[1])
            
        if cmdr == "ic":
            env_var_all[args[1]] = env_var_all[args[1]] + int(args.split(",")[1])

        if cmdr == "dc":
            env_var_all[args[1]] = env_var_all[args[1]] - int(args.split(",")[1])

        if cmdr == "cp":
            env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] + env_var_all[str(args.split(",")[2])[1]]

        if cmdr == "cn":
            env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] - env_var_all[str(args.split(",")[2])[1]]

        if cmdr == "st":
            env_var_all[args[1]] = int(args.split(",")[1])


def frmain():
    debug = False
    line = 0
    if pathf.isfile(os.getcwd() + "/birpref") == False:
        prefSaver()
    else:
        prefUpdater()
    if len(sys.argv)>1:
        cmdmode = 1
        with open(os.getcwd() + "/" + sys.argv[1], mode="r") as fileread:
            code = fileread.read()
            lineout = code.split("\n")

        # Compile Code to interpreter style
        if os.path.isfile(os.getcwd() + "/" + sys.argv[1].split(".")[0] + ".brc") == False:
            ln = 0
            while ln<(len(lineout)-1):
                if ('^==' in lineout[ln])==True:
                    lineout[ln] = "DEL_"
                ln += 1
            ln = 0
            lnCode = ""
            while ln<(len(lineout)):
                lnCode += lineout[ln]+"\n"
                ln += 1
            lnCode = lnCode.replace("\n\n", "\n")
            lnCode = lnCode.replace("DEL_\n", "")
            
            lnCode = lnCode.replace("print", "prt")
            lnCode = lnCode.replace("bash_com", "cm")
            lnCode = lnCode.replace("deincr", "dc")
            lnCode = lnCode.replace("incr", "ic")
            lnCode = lnCode.replace("comppos", "cp")
            lnCode = lnCode.replace("compneg", "cn")
            lnCode = lnCode.replace("setvar", "st")
            lnCode = lnCode.replace("prog", "prg")
            lnCode = lnCode.replace("prompt", "pr")

            with open(os.getcwd() + "/" + sys.argv[1].split(".")[0] + ".brc", mode="w") as fileread:
                fileread.write(lnCode+"d ")

        # Open compiled '.brc' file
        with open(os.getcwd() + "/" + sys.argv[1].split(".")[0] + ".brc", mode="r") as fileread:
            code = fileread.read()
            lineout = code.split("\n")
            
        while line<(len(lineout)-1):
            rnarg = False
            
            linecr = lineout[line].split(";")
        
            if (' ' in lineout[line])==False:
                if debug==True:
                    print("line: " + lineout[line])
                inputerr()

            linec = linecr[0]
            cmdr = linec.split(" ")[0]
            args = linec.split(" ")[1]

            #if cmdr == "^==":
            #    print("")

            if debug==True:
                print("command: " + cmdr)
                print("\nargs: " + args)

            if debug==True:
                print("looking for command matches: " + cmdr)
                
            if cmdr == "prt":               
                finalassembledstr = ""
                if '_' in args:
                    i = 0
                    lc2 = args.split("_")
                    while i < len(lc2):
                        finalassembledstr = finalassembledstr + lc2[1] + " "
                else:
                    finalassembledstr = expr_run(args)
                print(finalassembledstr)

            if cmdr == "d":
                print("",end="")
            
            if cmdr == "cm":
                os.system(args)

            if cmdr == "sp":
                time.sleep(int(args))

            if cmdr == "if":
                ln = args.split(",")
                #print(linec.split(" ")[2]+" "+linec.split(" ")[3])
                #print(ln[1])
                #print(str(ln[0])[1])
                #print(str(ln[2])[1])

                if ln[1]=="==" and expr_run(str(ln[0])) == expr_run(str(ln[2])):
                    execLine(linec.split(" ")[2]+" "+linec.split(" ")[3])
                if ln[1]==">=" and expr_run(str(ln[0])) >= expr_run(str(ln[2])):
                    execLine(linec.split(" ")[2]+" "+linec.split(" ")[3])
                if ln[1]=="<=" and expr_run(str(ln[0])) <= expr_run(str(ln[2])):
                    execLine(linec.split(" ")[2]+" "+linec.split(" ")[3])
                if ln[1]==">" and expr_run(str(ln[0])) > expr_run(str(ln[2])):
                    execLine(linec.split(" ")[2]+" "+linec.split(" ")[3])
                if ln[1]=="<" and expr_run(str(ln[0])) < expr_run(str(ln[2])):
                    execLine(linec.split(" ")[2]+" "+linec.split(" ")[3])

            if cmdr == "prg":
                rnarg = False
                if args[1].split(",")[0]=="stop":
                    line = len(lineout)+1
                if args[1].split(",")[0]=="err":
                    print("Error on line " + line + ": " + args[1].split(",")[1])
                    line = len(lineout)+1
                if args[1].split(",")[0]=="debugOn":
                    debug = True
                if args[1].split(",")[0]=="debugOff":
                    debug = False

            if cmdr == "pr":
                finalassembledstr = ""
                if '_' in args:
                    i = 0
                    lc2 = str(args[1].split(",")[1]).split("_")
                    while i < len(lc2):
                        finalassembledstr = finalassembledstr + lc2[1] + " "
                else:
                    finalassembledstr = expr_run(args)
                env_var_all[args[1]] = int(input(finalassembledstr))
                
            if cmdr == "eq":
                env_var_all[args[1]] = expr_run(args.split(",")[1])

            if cmdr == "ic":
                env_var_all[args[1]] = env_var_all[args[1]] + int(args.split(",")[1])

            if cmdr == "dc":
                env_var_all[args[1]] = env_var_all[args[1]] - int(args.split(",")[1])

            if cmdr == "cp":
                env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] + env_var_all[str(args.split(",")[2])[1]]

            if cmdr == "cn":
                env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] - env_var_all[str(args.split(",")[2])[1]]

            if cmdr == "st":
                env_var_all[args[1]] = int(args.split(",")[1])

            line += 1
    else:
        mainMenu()
        cmdmode = 0
        while True:
            rnarg = True
            pIn = input(promptchar + "> ")

            if (' ' in pIn)==False:
                inputerr()
                continue

            linecr = pIn.split(";")
            linec = linecr[0]
            cmdr = linec.split(" ")[0]
            args = linec.split(" ")[1]

            if debug==True:
                print("command: " + cmdr)
                print("\nargs: " + args)

            if debug==True:
                print("looking for command matches: " + cmdr)
                
            if cmdr == "^==":
                print("")
                # Do Nothing
                
            if cmdr == "print":
                rnarg = False
                print(expr_run(args))

            if cmdr == "if":
                args = args.split(",")
                if args[0]=="==" and expr_run(args[1]) == expr_run(args[2]):
                    execLine(linec.split(" ")[3]+linec.split(" ")[4])
                if args[0]==">=" and expr_run(args[1]) >= expr_run(args[2]):
                    execLine(linec.split(" ")[3]+linec.split(" ")[4])
                if args[0]=="<=" and expr_run(args[1]) <= expr_run(args[2]):
                    execLine(linec.split(" ")[3]+linec.split(" ")[4])
                if args[0]==">" and expr_run(args[1]) > expr_run(args[2]):
                    execLine(linec.split(" ")[3]+linec.split(" ")[4])
                if args[0]=="<" and expr_run(args[1]) < expr_run(args[2]):
                    execLine(linec.split(" ")[3]+linec.split(" ")[4])
            if cmdr == "prog":
                rnarg = False
                print("prog(system control) command not available in prompt mode!")
                """if args[1].split(",")[0]=="stop":
                    line = len(lineout)+1
                if args[1].split(",")[0]=="err":
                    print("Error on line " + line + ": " + args[1].split(",")[1])
                    line = len(lineout)+1
                if args[1].split(",")[0]=="debugOn":
                     debug = True
                if args[1].split(",")[0]=="debugOff":
                     debug = False"""
            if cmdr == "bash_com":
                rnarg = False
                os.system(args)

            if cmdr == "sleep":
                rnarg = False
                time.sleep(int(args))

            if cmdr == "eq":
                rnarg = False
                env_var_all[args[1]] = expr_run(args.split(",")[1])

            if cmdr == "incr":
                rnarg = False
                env_var_all[args[1]] = env_var_all[args[1]] + int(args.split(",")[1])

            if cmdr == "deincr":
                rnarg = False
                env_var_all[args[1]] = env_var_all[args[1]] - int(args.split(",")[1])

            if cmdr == "comppos":
                rnarg = False
                env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] + env_var_all[str(args.split(",")[2])[1]]

            if cmdr == "compneg":
                rnarg = False
                env_var_all[args[1]] = env_var_all[str(args.split(",")[1])[1]] - env_var_all[str(args.split(",")[2])[1]]
                
            if cmdr == "setvar":
                rnarg = False
                env_var_all[args[1]] = int(args.split(",")[1])

            if rnarg == True:
                commanderr()
                
def ResizeList(l, size, fill_with=None):
    l += [fill_with]*(size-len(l))

def mainMenu():
    clearScreen()
    print(crayons.red("|*|*|*|*|*|*| Birch Micro IDE " + version + " |*|*|*|*|*|*|"))
    print(crayons.yellow("1.Editor"))
    print(crayons.yellow("2.Parser"))
    print(crayons.yellow("3.Open File"))
    print(crayons.yellow("4.New File"))
    print(crayons.yellow("5.Check for errors in code"))
    print(crayons.green("6.Scan project for files"))
    menuopt = input(crayons.yellow("\noption [1-3]: ",bold=True))

    if menuopt=="1":
        clearScreen()
        ffn = input("\n\nfilename: ")
        editorMain(ffn)
    if menuopt=="2":
        clearScreen()
        print("birch-prompt " + version + " " + platform)
        return
    if menuopt=="3":
        clearScreen()
        ResizeList(sys.argv, 2, fill_with=0)
        sys.argv[1] = input("\n\nfilename: ")
        frmain()
    if menuopt=="4":
        clearScreen()
        nfn = input("\n\nnew filename: ")
        with open(nfn, "w") as nfile:
            nfile.write("^== Made with " + crayons.yellow("Birch", bold=True) + crayons.magenta("Micro", bold=True) + crayons.cyan("IDE", bold=True) + "\n")
        editorMain(nfn)
    if menuopt=="5":
        clearScreen()
        ResizeList(sys.argv, 2, fill_with=0)
        sys.argv[1] = input("\n\nfilename: ")
        frmain()
    if menuopt=="6":
        clearScreen()
        inFdir = input("Project Directory: ")
        filesall = dict()
        e = 1
        print("\n\n")
        for root, dirs, files in os.walk(os.getcwd()+"/"+inFdir):
            for file in files:
                if file.endswith(".bir") or file.endswith(".brc"):
                     print(crayons.magenta(str(e)+". "+os.path.join(root, file)))
                     filesall[str(e)] = os.path.join(root, file)
                     e+=1
        fname = input("\nfile number: ")
        clearScreen()
        ResizeList(sys.argv, 2, fill_with=0)
        sys.argv[1] = str(filesall[fname]).replace(os.getcwd()+"/", "")
        frmain()
        sys.exit()
        
frmain()
