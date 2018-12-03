#!/bin/bash

#############################################                                        
# ,---.|              |    ,---.          
# |    |---.,---.,---.|__/ `---.,   .,---.
# |    |   ||---'|    |  \     ||   |`---.
# `---'`   '`---'`---'`   ``---'`---|`---'
#                               `---'    
# by: Ari Stehney
#
# Verify BirchParser function compatibility
#
#
#############################################

$COLOROK = 0
$DEPOK = 0

echo "CheckSys V2.1 for BirchParser"
sleep 1

clear

# Check For VT100
for((i=16; i<256; i++)); do
    printf "\e[48;5;${i}m%03d" $i;
    printf '\e[0m';
    [ ! $((($i - 15) % 6)) -eq 0 ] && printf ' ' || printf '\n'
done

echo "do you see colors [y/n]: "
read rdchoice

if [ "$rdchoice" = "y" ]; then 
    $COLOROK = $((COLOROK+1))
else
    echo "VT100 Color terminal required for BirchMicroIDE and BirchParser use!"  
fi;


# Check for Dependecies

if ! [ -x "$(command -v python3)" ]; then
    echo "Python3 required for BirchMicroIDE and BirchParser use!"
else
    $DEPOK=$((DEPOK+1))
fi

if ! [ -x "$(command -v pip3)" ]; then
    echo "Pip3 required for BirchMicroIDE and BirchParser use!"
else
    $DEPOK=$((DEPOK+1))
fi

if ! [ -x "$(command -v git)" ]; then
    echo "GIT required for BirchMicroIDE and BirchParser use!"
else
    $DEPOK=$((DEPOK+1))
fi

# Install Pip3 Dependecies
pip3 install crayons
pip3 install flask


# Check all errors

if [ "$DEPOK" = "5" ]; then 
    echo "Install OK"
else
    echo "DEP ERROR!!!"  
fi;