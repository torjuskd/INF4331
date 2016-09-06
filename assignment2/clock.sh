#!/bin/bash
#A simple clock that prints the current time every second.
#If "-AMPM" flag is supplied, the format will be am/pm.
storedCommand="date +%R"
declare -i seconds; seconds=$(date +%s);

while [ 1 ]; do
    newtime=$(date +%s)
    if [ "$newtime" -ne "$seconds" ]; then
	((seconds=newtime))
	if [ "$1" == "--AMPM" ]; then
	    if [ $(date +%k) -gt "12" ]; then
		storedCommand="date +\"%I:%M PM\""
	    else
		storedCommand="date +\"%I:%M AM\""
	    fi
	fi
	clear
	eval $storedCommand
    fi
done
