import random


class Road:
    def __init__(self, quantity):
        self.states = (2*quantity) * [0]

    def generate_next(self):
        length = len(self.states) - 1
        rand_this = random.randint(0, 4)
        if rand_this == 1 or rand_this == 2:
            self.states[length] = 1

    def refresh_states(self):
        i = 0
        while i < len(self.states)-1:
            self.states[i] = self.states[i+1]
            i += 1
        self.states[len(self.states) - 1] = 0
