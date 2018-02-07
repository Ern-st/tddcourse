#!/usr/bin/env python3

class logger:
    
    def log(self, error):
        with open('logfile.log', 'a') as logfile:
            logfile.write('{}\n'.format(error))