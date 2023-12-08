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
    self.attack = EVs['ATTACK']
    self.defense = EVs['DEFENSE']
    self.bars = 20 # amount of health bars

    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
        # Print fight information
        print("--- Pokémon Battle ---")
        print(f"\n{self.name}")
        print("TYPE/")

if __name__ == '__main__':
    pass
