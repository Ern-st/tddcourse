#!/usr/bin/env python3
import unittest
import unittest.mock as mock
from testfixtures import Comparison as C

from MyStringAdder import MyStringAdder
from readerClass import reader 

class testMyStringAdder(unittest.TestCase):
    
    def test_IHaveAClass(self):
        MyStringAdder()

    @mock.patch('readerClass.reader.getContents')
    def test_ICanLoadContents(self, mock_reader_getContents):
        expectedInput = ["test", "test2"]
        mock_reader_getContents.return_value = expectedInput
        
        MyReader = reader()
        StringAdder = MyStringAdder()
        StringAdder.loadInput(MyReader)
        actualInput = StringAdder.getInput()

        self.assertListEqual(expectedInput, actualInput)