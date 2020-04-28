
class Cell:
    PEDESTRIAN_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    PEDESTRIAN_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"
    OBSTACLE_COLOR_BG = "red"
    OBSTACLE_COLOR_BORDER = "red"
    TARGET_COLOR_BG = "blue"
    TARGET_COLOR_BORDER = "blue"

    def __init__(self, master, x, y, size):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.fill = False
        self.role = "G"

    def _switch(self, switchTo):
        """ Switch if the cell is filled or not. """
        self.fill = not self.fill

        if self.fill:
            self.role = switchTo

        else:
            self.role = "G"

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        if self.master != None :

            if self.role == "O":
                fill = Cell.OBSTACLE_COLOR_BG
                outline = Cell.OBSTACLE_COLOR_BORDER

            elif self.role == "P":
                fill = Cell.PEDESTRIAN_COLOR_BG
                outline = Cell.PEDESTRIAN_COLOR_BORDER

            elif self.role == "T":
                fill = Cell.TARGET_COLOR_BG
                outline = Cell.TARGET_COLOR_BORDER


            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)
