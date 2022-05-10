class Dino:
    """Representing of charakter's attributes"""
    def __init__(self, x, y, height, length, position):
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.is_alive = True
        self.image = None
        self.position = position
        self.is_jump = False

    def inc_y(self, game, plus):
        if game.is_run:
            self.y += plus

    def dec_y(self, game, minus):
        if game.is_run:
            self.y -= minus

    def set_new_y(self, y, game):
        if game.is_run:
            self.y = y

    def check_alive(self, road):
        if road.states[self.position-1] == 1 and (not self.is_jump):
            self.is_alive = False

    def set_jump(self, state):
        self.is_jump = state
