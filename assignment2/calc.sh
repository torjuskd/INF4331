#!/bin/bash
option=$1; shift;
declare -i result

case "$option" in
    -S)
	#Sum
	result=0
	for arg in $@; do
	    ((result+=arg))
	done
	echo "$result"
	;;
    -P)
	#Product
	result=1
	for arg in $@; do
	    ((result*=arg))
	done
	echo "$result"
	;;
    -M)
	#Maximum
	result=$1; shift
	for arg in $@; do
	    [ "$arg" -gt "$result" ] && ((result=arg))
	done
	echo "$result"
	;;
    -m)
	#Minimum
	result=$1; shift
	for arg in $@; do
	    [ "$arg" -lt "$result" ] && ((result=arg))
	done
	echo "$result"
	;;
    *)
	echo "$0: invalid option \"$option\""; exit ;;
esac
