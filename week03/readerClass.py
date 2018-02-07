#!/usr/bin/env python3
import os

class reader:
    
    def __init__(self):
        pass
        
    def getContents(self):
        file = open("input.txt", "r")
        lines = [x.rstrip() for x in file.readlines()]
        return lines