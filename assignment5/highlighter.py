#!/usr/bin/env python3
# Takes as input a regex, a color theme and a file and
# outputs the file with colorized syntax to standard out.
# Called with:
# python3 highlighter.py <syntaxfile> <themefile> <sourcefile>.
import sys


def highlight(syntaxfile, themefile, sourcefile):
    """Colorizes the file according to the specified rules
        
        Args:
            syntaxfile (filename): File containing the syntax rules to use
            themefile (filename): File containig the theme (colors, etc.) to use
            sourcefile (filename): File to highlight

        Returns:
            <none>
        """
    

# Nice to have:
if __name__ == "__main__":
    if len(sys.argv) < 4: # Print help
        print("syntax: python3 highlighter.py <syntaxfile> <themefile> <sourcefile>")
        sys.exit()
    
    highlight(syntaxfile=sys.argv[1], themefile=sys.argv[2], sourcefile=sys.argv[3])
