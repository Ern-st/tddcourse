#!/usr/bin/env python3
import unittest
import unittest.mock as mock

from MyStringAdder  import MyStringAdder
from readerClass    import reader
from writerClass    import writer
from loggerClass    import logger

class testMyStringAdder(unittest.TestCase):

    @mock.patch('readerClass.reader')
    @mock.patch('writerClass.writer')
    @mock.patch('loggerClass.logger')
    def setUp(self, mock_reader, mock_writer, mock_logger):
        self.mock_reader = mock_reader
        self.mock_writer = mock_writer
        self.mock_logger = mock_logger

        self.MyStringAdder = MyStringAdder(self.mock_reader, self.mock_writer, self.mock_logger)
        #self.MyStringAdder = MyStringAdder(reader(), writer(), logger())

    def test_ICanLoadContents(self):
        expectedInput = ["test", "test2"]
        self.mock_reader.getContents.return_value = expectedInput
        
        StringAdder = self.MyStringAdder
        StringAdder.loadInput()
        actualInput = StringAdder.getInput()

        self.assertListEqual(expectedInput, actualInput)

    def test_ICanWriteOutput(self):
        self.mock_writer.write.return_value = True

        success = self.MyStringAdder.writeOutput(["test","test2"])

        self.assertTrue(success)

    def test_ICanAddNumbers(self):
        input = "0 4 3 2 3"
        output = self.MyStringAdder.addNumbers(input)
        
        self.assertEqual(12, output)

    def test_AddingBogusReturnsNaN(self):
        input = "Horse"
        output = self.MyStringAdder.addNumbers(input)

        self.assertEqual("NaN", output)