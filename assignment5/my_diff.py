#!/usr/bin/env python3
# An alternative implementation of the diff utility

import sys
import re

def readfile(filename):
    """Reads file and outputs string holding contents of file
        
        Args:
            filename (string): Filename of the file to read from

        Returns:
            filecontents (string): String holding contents of file
        """
    with open(filename) as file:
        return file.read()

def writefile(string, filename="diff_output.txt"):
    """Writes input string to file
        
        Args:
            string (string): string to print to file
            filename (string): Filename of output file

        Returns:
            <None>
        """
    file=open(filename, 'w')
    file.write(string)
    file.close()

def diff(string1, string2):
    """Outputs a "diff" string with lines starting with the following symbols:
        0: Line has not been modified    
        +: Line has been added
        -: Line has been deleted
        
        Args:
            string1 (string): String containing the original file
            string2 (string): String containing the modified file

        Returns:
            output (string) : Output string containing differences
        """
    output=""
    arr1=string1.split("\n")
    arr2=string2.split("\n")
    line2N=0
    line1N=0

    while line1N < len(arr1) or line2N < len(arr2):
        
        if line2N >= len(arr2): #File1 longer than file2, assume line deleted
            line1=arr1[line1N]
            output=output + "-" + line1 + "\n"
            line1N=line1N+1
            continue
        elif line1N >= len(arr1): #File2 longer than file1, assume line added
            line2=arr2[line2N]
            output=output + "+" + line2 + "\n"
            line2N=line2N+1
            continue

        line1=arr1[line1N]
        line2=arr2[line2N]
            
        if arr1[line1N] == arr2[line2N]: #Lines are equal
            output=output +"0" + line1 + "\n"
        else: #Lines are different
            if line1 in arr2: #assume that line appears later
                output=output + "+" + line2 + "\n"
                line1N=line1N-1
            elif line1 not in arr2: #line is nowhere in file2, assume deleted
                output=output + "-" + line1 + "\n"
                line2N=line2N-1
            else: #default behaviour
                output=output + "-" + line1 + "\n"
                output=output + "+" + line2 + "\n"
        line2N=line2N+1
        line1N=line1N+1

    return output

# Nice to have:
if __name__ == "__main__":
    if len(sys.argv) < 3: # Print help
        print("Usage: python3 my_diff.py <original_file> <modified_file> <output_filename (optional)>")
        sys.exit()
    string1=readfile(sys.argv[1])
    string2=readfile(sys.argv[2])
    output=diff(string1, string2)
    if len(sys.argv) > 3: #filename has been supplied
        writefile(output, sys.argv[3])
    else: #No filename given: print to standard out
        writefile(output)
        print(output)
