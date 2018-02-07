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

    def writeOutput(self, output):
        return self.writer.write(output)

    def logError(self, error):
        self.logger.log(error)

    def addNumbers(self, line):
        try:
            numbers = [int(x) for x in line.split(" ")]
        except ValueError:
            self.logger.log(line)
            return "NaN"
        return sum(numbers)
    

    def run(self):
        pass