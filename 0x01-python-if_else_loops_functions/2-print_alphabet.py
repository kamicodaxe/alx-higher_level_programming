#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(i)), end="" if i < ord('z') else "\n")
