#!/usr/bin/env python3
import os

from MyStringAdder  import MyStringAdder
from readerClass    import reader
from readerClass    import webReader
from writerClass    import writer
from loggerClass    import logger
from loggerClass    import slackLogger

MyWebStringAdder = MyStringAdder(
    webReader({"url":"https://gist.githubusercontent.com/ernst-at-colourbox/3197dbb764785c309ea3af84d8a6727f/raw/c47d0cf76289cc54ad0dd437309f24752095f993/TDD_week03_input.txt"}), 
    writer(), 
    slackLogger({"webhook": os.environ['SLACK_WEBHOOK_ME']})
)

MyStringAdder = MyStringAdder(
    reader(), 
    writer(), 
    logger()
)

print("\na webReader run:")
MyWebStringAdder.run()

print("\na reader run:")
MyStringAdder.run()