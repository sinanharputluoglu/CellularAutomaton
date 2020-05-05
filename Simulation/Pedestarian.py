import math
MAX_SPEED = 100

class Pedestarian:

    def __init__(self, y, x, speed):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.speed = speed
        self.adj_speed = 100 / speed
        self.finished = False
        self.sim_time = math.inf

    def set_coordinate(self, y, x):
        self.x = x
        self.y = y

    def found_target(self, t):
        print("Pedestrian started at x:{}, y:{} having speed {} reached target in {}th iteration".format(self.start_x, self.start_y, self.speed, t))
        self.finished = True
        self.sim_time = t

    def is_active(self):
        return not self.finished