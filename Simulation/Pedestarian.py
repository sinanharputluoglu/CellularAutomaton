MAX_SPEED = 100

class Pedestarian:

    def __init__(self, y, x, speed):
        self.x = x
        self.y = y
        self.adj_speed = 100 / speed
        self.finished = False

    def set_coordinate(self, y, x):
        self.x = x
        self.y = y

    def found_target(self):
        self.finished = True

    def is_active(self):
        return not self.finished