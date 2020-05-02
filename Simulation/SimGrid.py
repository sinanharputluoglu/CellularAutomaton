from Simulation.SimCell import SimCell
from typing import List
import math
class SimGrid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = []
        self.targetCell = None # type: List[List[SimCell]]
        for row in range(size_y):
            line = []
            for column in range(size_x):
                line.append(SimCell(column, row))
            self.grid.append(line)

    def get_grid(self):
        return self.grid

    def print_grid(self):
        for i in range(0, self.size_x):
            for j in range(0, self.size_y):
                print(self.grid[i][j].state, end="  ")
            print(" ")

    def set_target(self, x, y):
        self.targetCell = SimCell(x, y)
        self.grid[y][x].set_state('T')

    def set_pedestarians(self, ped_list: List):
        for value in ped_list:
            self.grid[value[0]][value[1]].set_state('P')

    def set_obstacles(self, obs_list: List):
        for value in obs_list:
            self.grid[value[0]][value[1]].set_state('O')

    def update_utilities(self):
        for row in range(self.size_y):
            for column in range(self.size_x):
                    self.grid[row][column].update_utility_score(self.targetCell)

    def update_distances(self):
        row = self.targetCell.y
        column = self.targetCell.x
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


    def simulate_next_step(self, dijsktra=False):
        for row in range(self.size_y):
            for column in range(self.size_x):
                self.grid[row][column].set_next_state()

    def simulate_one_step(self, dijsktra=False):
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
        print(min_column, min_row)
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


