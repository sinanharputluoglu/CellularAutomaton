from tkinter import *
from CellularAutomaton.GUI.Cell import Cell

class CellGrid(Canvas):

    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width=cellSize * columnNumber, height=cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        # memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        # bind click action
        self.bind("<Button-1>", self.handlePedestrianMouseClick)
        # bind moving while clicking
        self.bind("<B1-Motion>", self.handlePedestrianMouseMotion)
        # bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.bind("<Button-2>", self.handleTargetMouseClick)
        self.bind("<B2-Motion>", self.handleTargetMouseMotion)
        self.bind("<ButtonRelease-2>", lambda event: self.switched.clear())

        self.bind("<Button-3>", self.handleObstacleMouseClick)
        self.bind("<B3-Motion>", self.handleObstacleMouseMotion)
        self.bind("<ButtonRelease-3>", lambda event: self.switched.clear())

        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handlePedestrianMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch("P")
        cell.draw()
        # add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handlePedestrianMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch("P")
            cell.draw()
            self.switched.append(cell)

    def handleObstacleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch("O")
        cell.draw()
        # add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleObstacleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch("O")
            cell.draw()
            self.switched.append(cell)

    def handleTargetMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch("T")
        cell.draw()
        # add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleTargetMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch("T")
            cell.draw()
            self.switched.append(cell)
