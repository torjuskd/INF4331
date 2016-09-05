#!/bin/bash -x
option=$1;
case "$option" in
    -S)
	#Sum 
	;;
    -P)
	#Product
	;;
    -M)
	#Maximum
	;;
    -m)
	#Minimum
	;;
    *)
	echo "$0: invalid option \"$option\""; exit ;;
esac


