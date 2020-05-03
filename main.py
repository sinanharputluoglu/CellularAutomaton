from tkinter import *
from GUI.CellGrid import CellGrid
from Simulation.Simulation import Simulation


def createSimulationWindow():
    simulationWindow = Toplevel(app)

    grid = CellGrid(simulationWindow, int(heightEntry.get()), int(widthEntry.get()), 15)
    grid.pack()

    simulation = Simulation()

    readyButton = Button(simulationWindow, text="Ready", bg='red',
                         command=lambda: prepare_simulation(simulation,
                                                            grid))
    readyButton.pack()

    simulateButton = Button(simulationWindow, text="Simulate", bg='red',
                            command=lambda: simulate(simulation, grid))
    simulateButton.pack()

    autoSimulateButton = Button(simulationWindow, text="Auto Simulate", bg='red',
                            command=lambda: auto_simulate(simulation, grid))
    autoSimulateButton.pack()

def prepare_simulation(simulation, grid):

    pedestrian_indices = grid.get_pedestrians()
    obstacles_indices = grid.get_obstacles()
    target_index = grid.get_target()

    simulation.set_simulation(grid.get_width(), grid.get_height(), target_index[1], target_index[0],
                              pedestrian_indices, obstacles_indices)


def simulate(simulation, grid):
    simulation.epoch(dijsk=True)

    simulation.print_grid()

    new_pedestrians = simulation.get_pedestrians()

    grid.update_pedestrians(new_pedestrians)

def auto_simulate(simulation, grid):

    simulate(simulation,grid)

    if grid.get_pedestrians():
        app.after(1000, lambda: auto_simulate(simulation, grid))

if __name__ == "__main__":
    app = Tk()

    app.title("Define Simulation Grid")

    app.geometry('350x200')

    heightLabel = Label(app, text="Height : ")
    heightLabel.grid(column=0, row=0)

    heightEntry = Entry(app, width=15)
    heightEntry.grid(column=1, row=0)

    widthLabel = Label(app, text="Width : ")
    widthLabel.grid(column=0, row=1)

    widthEntry = Entry(app, width=15)
    widthEntry.grid(column=1, row=1)

    btn = Button(app, text="Create Simulation Grid", command=createSimulationWindow)
    btn.grid(column=0, row=2)

    app.mainloop()
