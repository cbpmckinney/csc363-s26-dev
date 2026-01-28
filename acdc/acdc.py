from charstream import CharStream
from tokenizer import Tokenizer
from tokenstream import TokenStream
from tokens import *

import sys

# Expectation of program: 
# input filename will be sys.argv[1]
# output filename will be sys.argv[2] (not implemented yet)
# Program will read source ac code from the input file, strip new lines and whitespaces
# For now, program will create charstream, tokenize to a tokenstream, and print the tokenstream to stdout


# Get input from file
with open(sys.argv[1], 'r') as inputfile:
    inputcontents = inputfile.read()

print("\n")
print(f"Tokenizing {sys.argv[1]}...")
print(f"Input contents:")
print(inputcontents)    

cs = CharStream(inputcontents)

ts = Tokenizer(cs).tokenize()

with open(sys.argv[2], 'w') as outputfile:
    for token in ts:
        outputfile.write(str(token) + "\n")    

for token in ts:
    print(token)


print(f"Tokenizing succeeded.  Output written to {sys.argv[2]}.")

