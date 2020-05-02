from Simulation import SimCell
from typing import List
import math
class SimGrid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = [] # type: List[List[SimCell]]
        self.targetCell = None
        for row in range(size_y):
            line = []
            for column in range(size_x):
                line.append(SimCell(column, row))
            self.grid.append(line)

    def set_target(self, target):
        self.targetCell = target

    def update_utilities(self):
        for row in range(self.size_y):
            for column in range(self.size_x):
                    self.grid[row][column].update_utility_score(self.targetCell)

    def update_distances(self, target_x, target_y):
        row = target_x
        column = target_y
        if row != 0:
            self.find_distance_to_target(row - 1, column)

        if column != 0:
            self.find_distance_to_target(row, column - 1)

        if row !=0 and column !=0:
            self.find_distance_to_target(row - 1, column - 1)

        if row != self.size_y - 1:
            self.find_distance_to_target(row + 1, column)

        if column != self.size_x - 1:
            self.find_distance_to_target(row, column + 1)

        if row != self.size_y - 1 and column != self.size_x - 1:
            self.find_distance_to_target(row + 1, column + 1)

        if row != 0 and column != self.size_x - 1:
            self.find_distance_to_target(row - 1, column + 1)

        if row != self.size_y - 1 and column != 0:
            self.find_distance_to_target(row + 1, column - 1)




    def update_map(self, dijsktra=False):
        for row in range(self.size_y):
            for column in range(self.size_x):
                if self.grid[row][column].is_person():
                    if self.update_movement(row, column, dijsktra):
                        self.grid[row][column].set_state('E')

    def update_movement(self, row, column, dijsktra):
        neighbouring_cells = {}
        if row != 0:
            if self.grid[row - 1][column].is_target():
                return True
            neighbouring_cells[(row - 1, column)] = self.grid[row - 1][column].get_score(dijsktra)

        if column != 0:
            if self.grid[row][column - 1].is_target():
                return True
            neighbouring_cells[(row, column - 1)] = self.grid[row][column - 1].get_score(dijsktra)

        if row !=0 and column !=0:
            if self.grid[row - 1][column - 1].is_target():
                return True
            neighbouring_cells[(row-1, column-1)] = self.grid[row - 1][column-1].get_score(dijsktra)

        if row != self.size_y - 1:
            if self.grid[row+1][column].is_target():
                return True
            neighbouring_cells[(row+1, column)] = self.grid[row + 1][column].get_score(dijsktra)

        if column != self.size_x - 1:
            if self.grid[row][column + 1].is_target():
                return True
            neighbouring_cells[(row, column+1)] = self.grid[row][column+1].get_score(dijsktra)

        if row != self.size_y - 1 and column != self.size_x - 1:
            if self.grid[row + 1][column + 1].is_target():
                return True
            neighbouring_cells[(row+1, column+1)] = self.grid[row+1][column+1].get_score(dijsktra)

        if row != 0 and column != self.size_x - 1:
            if self.grid[row - 1][column + 1].is_target():
                return True
            neighbouring_cells[(row-1, column+1)] = self.grid[row-1][column+1].get_score(dijsktra)

        if row != self.size_y - 1 and column != 0:
            if self.grid[row + 1][column - 1].is_target():
                return True
            neighbouring_cells[(row+1, column-1)] = self.grid[row+1][column-1].get_score(dijsktra)

        min_row, min_column = min(neighbouring_cells, key=neighbouring_cells.get)
        self.grid[min_row][min_column].set_state('P')
        return True


    def find_distance_to_target(self, row, column):
        if self.grid[row][column].is_visited():
            pass
        else:
            neighbouring_cells = {}
            if row != 0:
                neighbouring_cells[(row - 1, column)] = self.grid[row - 1][column].get_distance()

            if column != 0:
                neighbouring_cells[(row, column - 1)] = self.grid[row][column - 1].get_distance()

            if row != 0 and column != 0:
                neighbouring_cells[(row - 1, column - 1)] = self.grid[row - 1][column - 1].get_distance()

            if row != self.size_y - 1:
                neighbouring_cells[(row + 1, column)] = self.grid[row + 1][column].get_distance()

            if column != self.size_x - 1:
                neighbouring_cells[(row, column + 1)] = self.grid[row][column + 1].get_distance()

            if row != self.size_y - 1 and column != self.size_x - 1:
                neighbouring_cells[(row + 1, column + 1)] = self.grid[row + 1][column + 1].get_distance()

            if row != 0 and column != self.size_x - 1:
                neighbouring_cells[(row - 1, column + 1)] = self.grid[row - 1][column + 1].get_distance()

            if row != self.size_y - 1 and column != 0:
                neighbouring_cells[(row + 1, column - 1)] = self.grid[row + 1][column - 1].get_distance()

            min_value = neighbouring_cells[min(neighbouring_cells, key=neighbouring_cells.get)]
            self.grid[row][column].set_distance(min_value + 1)
            for key, value in neighbouring_cells.items():
                rr, cc = key
                self.find_distance_to_target(rr, cc)


