#!/usr/bin/env python3
from MyStringAdder  import MyStringAdder
from readerClass    import reader
from readerClass    import webReader
from writerClass    import writer
from loggerClass    import logger
from loggerClass    import slackLogger

MyWebStringAdder = MyStringAdder(
    webReader({"url":"https://gist.githubusercontent.com/ernst-at-colourbox/3197dbb764785c309ea3af84d8a6727f/raw/c47d0cf76289cc54ad0dd437309f24752095f993/TDD_week03_input.txt"}), 
    writer(), 
    slackLogger({"webhook":" https://hooks.slack.com/services/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"})
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