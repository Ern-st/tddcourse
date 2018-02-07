#!/usr/bin/env python3

class writer:
    
    def write(self, output):
        try:
            for line in output:
                print(line)
        except Exception:
            return False
        return True