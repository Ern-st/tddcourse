#!/usr/bin/env python3
import unittest
import unittest.mock as mock
from testfixtures import Comparison as C

from MyStringAdder import MyStringAdder
from readerClass import reader
from writerClass import writer
from loggerClass import logger

class testMyStringAdder(unittest.TestCase):

    def setUp(self):
        self.MyStringAdder = MyStringAdder()

    @mock.patch('readerClass.reader.getContents')
    def test_ICanLoadContents(self, mock_reader_getContents):
        expectedInput = ["test", "test2"]
        mock_reader_getContents.return_value = expectedInput
        
        MyReader    = reader()
        StringAdder = self.MyStringAdder
        StringAdder.loadInput(MyReader)
        actualInput = StringAdder.getInput()

        self.assertListEqual(expectedInput, actualInput)

    @mock.patch('writerClass.writer.write')
    def test_ICanWriteOutput(self, mock_writer_write):
        mock_writer_write.return_value = True

        MyWriter = writer()
        success = MyWriter.write(["test"])

        self.assertTrue(success)