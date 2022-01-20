import random

# 1) Add the class declaration. Use the following class comment.

class Die:

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        self.value = 0
        self.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        self.value = random.randint(1,6)
        if self.value == 5:
            self.points = 50

        elif self.value == 1:
            self.points = 100
        
        else:
            self.points = 0