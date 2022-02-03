"""The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled."""

import random

# Constructs a new Seeker.
class Seeker:
    
    def __init__(self):
        self._location = random.randint(1, 1000)
       
# Gets the current location.
    def get_location(self):
        return self._location

# Moves to the given location.
    def move_location(self, location):
        self._location = location