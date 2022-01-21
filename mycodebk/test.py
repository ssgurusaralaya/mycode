#!/usr/bin/env python3

file=open("lines.txt", "r")
lines=file.readlines()
for line in lines:
    if line=="\n":
        print("Empty Line")
    else:
        print("Non-empty line")
