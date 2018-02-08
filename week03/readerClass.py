#!/usr/bin/env python3
import urllib.request

class reader:

    def TrimLines(self, lines):
        return [x.rstrip() for x in lines]
        
    def readArray(self):
        file = open("input.txt", "r")
        return self.TrimLines(file.readlines())

class webReader(reader):

    def __init__(self, options):
        self.options = options

    def readArray(self):
        with urllib.request.urlopen(self.options['url']) as response:
            return response.read().decode("utf-8").split("\n")
