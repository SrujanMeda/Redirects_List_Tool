import sys
import re

output = ""
with open("redir1.txt") as f:
    for line in f:
        if not line.isspace():
            line = line.replace('\t', ' ')
            line = ' '.join(line.split())+"\n"
            output += line

    f.write(output)

f = open("output.txt", "w")
f.write(output)