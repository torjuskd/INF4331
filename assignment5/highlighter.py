#!/usr/bin/env python3
# Takes as input a regex, a color theme and a file and
# outputs the file with colorized syntax to standard out.
# Called with:
# python3 highlighter.py <syntaxfile> <themefile> <sourcefile>.

import sys
import re

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
            line=line.strip()
            if line.startswith("#"):
                continue #interpret line as comment; do nothing.
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
    #select: 1: colortag1, 2: selection up to 2. colortag, 3: 2. colortag, 4: selec. up to colortag 2. end, 5: colortag 2. end
    regex="(\\033\[\d+;\d+m)((?:(?!\\033\[0m).)*)(\\033\[\d+;\d+m)(.*?)(\\033\[0m)"

    with open(sourcefilename) as sourcefile:
        read_data = sourcefile.read()
        data = read_data
        for syntaxrule in syntaxrules:
            for themerule in themerules:
                if themerule[0] == syntaxrule[1]:
                    data = re.sub("("+syntaxrule[0]+")", ("\033[{}m".format(themerule[1]) + r"\1" + "\033[0m"), data, flags=re.MULTILINE) #do the color formatting
                    data = re.sub(regex, (r"\1\2" + "\033[0m" + r"\3\4\5\1"), data, flags=re.MULTILINE) #"fix" colors inside each other
                    break #we found corresponding theme and syntax, jump to next syntax rule
        return data

# Nice to have:
if __name__ == "__main__":
    if len(sys.argv) < 4: # Print help
        print("Usage: python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>")
        sys.exit("Commandline arguments error.")
    syntaxrules = readrulefile(sys.argv[1], syntax=True)
    themerules = readrulefile(sys.argv[2])
    data=highlight(syntaxrules, themerules, sourcefilename=sys.argv[3])
    print(data)

