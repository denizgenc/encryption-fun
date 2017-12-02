# -*- coding: utf-8 -*-
# rotemake.py
# Makes a ROT file, using a plaintext (or any?) source file as input, and
# running it through mod 26.

# Usage:
# python rotemake.py [-n|-a] inputfile outputfile
# -n means output comma seperated integers (default)
# -a means output a string of characters instead
# inputfile and outputfile is the name of the source and ROT file respectively

import sys, string, os.path

def rot_convert_csv(byte):
    """Takes a byte, makes it an integer, finds integer mod 26, then returns a
string with said integer and a comma immediately after."""
    return str((int.from_bytes(byte, sys.byteorder) % 26)) + ","

def rot_convert_alpha(byte):
    """Takes a byte, makes it an integer, finds integer mod 26, converts that
into a lowercase ascii character, then returns that character."""
    alpha_index = int.from_bytes(byte, sys.byteorder) % 26
    return string.ascii_lowercase[alpha_index]

def make_rot():
    inputfile = open(sys.argv[-2], "rb")
    if os.path.exists(sys.argv[-1]):
        if str(input("{} already exists, overwrite? (y/n) ".format(sys.argv[-1]))).lower()[0] == "y":
            outputfile = open(sys.argv[-1], "w")
        else: exit()
    else: outputfile = open(sys.argv[-1], "w")
    
    byte = inputfile.read(1)
    
    while byte != b"": # Reached EOF
        if sys.argv[1] == "-a":
            outputfile.write(rot_convert_alpha(byte))
        else: # This WILL break if we add any other options beyond -n, but it
              # works for now
            outputfile.write(rot_convert_csv(byte))
        
        byte = inputfile.read(1)    
            
option_given = False
if "-n" in sys.argv or "-a" in sys.argv:
    option_given = True

if len(sys.argv) > 4:
    print("Too many arguments.")
    exit()
if len(sys.argv) == 4 and not option_given:
    print("Too many arguments.")
    exit()
if len(sys.argv) == 3 and option_given:
    print("You have either forgotten to specify a source file or the name of the ROT file.")
    exit()
if len(sys.argv) < 3:
    print("Too few arguments.")
    exit()
    
make_rot()
