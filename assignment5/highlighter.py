#!/usr/bin/env python3
# Takes as input a regex, a color theme and a file and
# outputs the file with colorized syntax to standard out.
# Called with:
# python3 highlighter.py <syntaxfile> <themefile> <sourcefile>.

import sys
import re

#class something
class asdf:
    asdfasdf=0

def readrulefile(rulefilename, syntax=False):
    """Reads rule-defining files in format <regex>: <rulename>
        
        Args:
            rulefilename (filename): File containing the rules to process

        Returns:
            rules (list): List containing the rules to use
        """
    rules = []
    with open(rulefilename) as rulefile:
        for line in rulefile:
            if syntax:
                rules.append([re.search(r"^\"(.*)\":", line).group(1), re.search(r": (.*)(?:$|\n)", line).group(1).strip()])
            else:
                rules.append(line.strip().split(": "))
    return rules

def highlight(syntaxrules, themerules, sourcefilename):
    """Colorizes the file according to the specified rules, and prints result to terminal
        
        Args:
            syntaxrules (list): Containing the syntax rules to use
            themerules (list): Containig the theme (colors, etc.) to use
            sourcefile (filename): File to highlight

        Returns:
            <none>
        """
    with open(sourcefilename) as sourcefile:
        read_data = sourcefile.read()
        data = read_data
        for syntaxrule in syntaxrules:
            for themerule in themerules:
                if themerule[0] == syntaxrule[1]:
                    data = re.sub("("+syntaxrule[0]+")", "\033[{}m".format(themerule[1]) + r"\1" + "\033[0m", data, flags=re.MULTILINE)
    print(data)

# Nice to have:
if __name__ == "__main__":
    if len(sys.argv) < 4: # Print help
        print("Usage: python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>")
        sys.exit()
    syntaxrules = readrulefile(sys.argv[1], syntax=True)
    themerules = readrulefile(sys.argv[2])
    highlight(syntaxrules, themerules, sourcefilename=sys.argv[3])
    # print(syntaxrules)
