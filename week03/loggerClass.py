#!/usr/bin/env python3
import urllib.request
import json

class logger:
    
    def log(self, error):
        with open('logfile.log', 'a') as logfile:
            logfile.write('{}\n'.format(error))

class slackLogger(logger):

    def __init__(self, options):
        self.options = options

    def log(self, error):
        data = {"text": ":warning: ERROR: {}".format(error), "username": "Python", "icon_emoji": ":snake:"}
        dataJson = json.dumps(data, sort_keys=True).encode('utf8')
        req = urllib.request.Request(
            self.options['webhook'],
            data=dataJson,
            headers={'content-type': 'application/json'}
        )
        urllib.request.urlopen(req)