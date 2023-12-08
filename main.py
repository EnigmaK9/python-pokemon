import time
import numpy as np
import sys

#delay printing
def delay_print(s):
    #print one character at a time
    #
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
# create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health ='====================')
    # save variables as attributes
    self.name = name
    self.types = types
    self.moves = moves
    self.attack = EVs['']

if __name__ == '__main__':
    pass
