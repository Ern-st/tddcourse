#!/usr/bin/env python3

class MyStringAdder:

    def __init__(self, reader, writer, logger):
        self.reader = reader
        self.writer = writer
        self.logger = logger

    def loadInput(self):
        self.input = self.reader.getContents()

    def getInput(self):
        return self.input
    
    def run(self):
        pass