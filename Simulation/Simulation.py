from Simulation.SimGrid import SimGrid

from typing import List
class Simulation:
    def __init__(self):
        self.sim_grid = None # type: SimGrid

    def set_simulation(self, x, y, target_x, target_y, pedestarians: List, obstacles: List):
        self.sim_grid = SimGrid(x, y)
        self.sim_grid.set_target(target_x, target_y)
        self.sim_grid.set_pedestarians(pedestarians)
        self.sim_grid.set_obstacles(obstacles)
        print("Updating utilites...")
        self.sim_grid.update_utilities()
        print("Updating distances...")
        self.sim_grid.update_distances()
        print("Setup complete.")


    def epoch(self, dijsk):
        self.sim_grid.simulate_one_step(dijsktra=dijsk)
        self.sim_grid.simulate_next_step()
        return  self.sim_grid.get_grid()

    def print_grid(self):
        self.sim_grid.print_grid()


