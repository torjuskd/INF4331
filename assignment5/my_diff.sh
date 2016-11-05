#!/bin/bash
#A simple shortcut-like script for using the my_diff.py script and highlighting afterwards.
#ex: ./my_diff.sh <file1> <file2>
if [ $# -lt 2 ]
  then
    echo "Call with: ./my_diff.sh <file1> <file2>"
else
    python my_diff.py $1 $2 my_diff.sh.output.txt && 
    python highlighter.py diff.syntax diff.theme my_diff.sh.output.txt && 
    rm my_diff.sh.output.txt
fi
