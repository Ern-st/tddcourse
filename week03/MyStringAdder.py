#!/usr/bin/env python3

class MyStringAdder:
    """Adds all integers on a line

    Takes 3 arguments:  
    reader has a readArray() method, the method should return an array of strings  
    writer has a write() method, the method should take a multiline string and write it somewhere  
    logger has a log() method, that is used for logging errors  
    """

    def __init__(self, reader, writer, logger):
        self.reader = reader
        self.writer = writer
        self.logger = logger

    def loadInput(self):
        self.input = self.reader.readArray()

    def getInput(self):
        return self.input

    def writeOutput(self, output):
        return self.writer.write(output)

    def logError(self, error):
        self.logger.log(error)

    def addNumbers(self, line):
        if len(line) == 0:
            return 0
        try:
            numbers = [int(x) for x in line.split(" ")]
        except ValueError:
            self.logger.log(line)
            return "NaN"
        return sum(numbers)
    

    def run(self):
        self.loadInput()
        print(self.input)
        output = ""
        for line in self.input:
            result = self.addNumbers(line)
            output += "\n{}".format(result)
        self.writeOutput(output)