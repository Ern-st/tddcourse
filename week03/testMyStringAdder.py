#!/usr/bin/env python3
import unittest
import unittest.mock as mock

from MyStringAdder  import MyStringAdder
from readerClass    import reader
from readerClass    import webReader
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

       #self.MyStringAdder = MyStringAdder(webReader({"url":"https://gist.githubusercontent.com/ernst-at-colourbox/3197dbb764785c309ea3af84d8a6727f/raw/c47d0cf76289cc54ad0dd437309f24752095f993/TDD_week03_input.txt"}), writer(), logger())
        #self.MyStringAdder = MyStringAdder(reader(), writer(), logger())

    def test_ICanLoadContents(self):
        expectedInput = ["test", "test2"]
        self.mock_reader.readArray.return_value = expectedInput
        
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
        self.mock_logger.log.assert_not_called()

    def test_AddingABlankLineReturnsZero(self):
        input = ""
        output = self.MyStringAdder.addNumbers(input)

        self.assertEqual(0, output)
        self.mock_logger.log.assert_not_called()

    def test_AddingBogusReturnsNaNAndLogsAnError(self):
        input = "Horse"
        output = self.MyStringAdder.addNumbers(input)

        self.assertEqual("NaN", output)
        self.mock_logger.log.assert_called_once_with(input)

    def test_thatTheAdderWorks(self):
        invalidLine = "Horse"
        self.mock_reader.readArray.return_value = ["0 5 6 4 8", invalidLine, "5", "", "5 6 7 8"]

        self.MyStringAdder.run()

        self.mock_logger.log.assert_called_once_with(invalidLine)
        self.mock_writer.write.assert_called_once_with("\n23\nNaN\n5\n0\n26")