#!/bin/bash
#A simple clock that prints the current time every second.
#If "-AMPM" flag is supplied, the format will be am/pm.
storedCommand="date +%H:%M:%S"
declare -i seconds; seconds=$(date +%s);

while [ 1 ]; do
    newtime=$(date +%s)
    if [ "$newtime" -ne "$seconds" ]; then
	((seconds=newtime))
	if [ "$1" == "--AMPM" ]; then
	    if [ $(date +%k) -gt "12" ]; then
		storedCommand="date +\"%I:%M:%S PM\"" #Kunne brukt %p, men det
	    else                                   #funker vel ikke med locale
		storedCommand="date +\"%I:%M:%S AM\""
	    fi
	fi
	clear
	eval $storedCommand
    fi
done
