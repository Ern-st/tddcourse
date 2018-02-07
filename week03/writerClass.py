#!/usr/bin/env python3

class writer:
    
    def write(self, output):
        try:
            print(output)
        except Exception:
            return False
        return True