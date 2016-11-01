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

    for lineN in range(len(arr1)):
        line1=arr1[lineN]
        line2=arr2[lineN]
        if len(arr2) < lineN: #File1 longer than file2, assume line have been deleted
            output=output +"-" + line1 + "\n"
            continue
            
        if arr1[lineN] == arr2[lineN]: #Lines are equal
            output=output +"0" + line1 + "\n"
        else: #Lines are different
            output=output +"-" + line1 + "\n"
            output=output +"+" + line2 + "\n"

    if len(arr2) > len(arr1): #File2 longer than file 1, assume line has been added
        for lineN in range(len(arr1), len(arr2)):
            line2=arr2[lineN]
            output=output +"+" + line2 + "\n"

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
