#!/usr/bin/env python3

class reader:
        
    def getContents(self):
        file = open("input.txt", "r")
        lines = [x.rstrip() for x in file.readlines()]
        return lines