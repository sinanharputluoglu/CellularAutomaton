from tkinter import *
from GUI.CellGrid import CellGrid
from Simulation.Simulation import Simulation
from time import sleep

grid = None

def createSimulationWindow():
    simulationWindow = Toplevel(app)

    grid = CellGrid(simulationWindow, int(heightEntry.get()), int(widthEntry.get()), 15)
    grid.pack()

    simulateButton = Button(simulationWindow, text="Simulate", bg='red',
                            command=createSimulationWindow)  # TODO : Change callback command to Simulate
    simulateButton.pack()

def draw_board(gridd, x, y):
    for i in range(0, x):
        for j in range(0, y):
            grid[i][j].role = gridd[i][j].state
    grid.draw()


if __name__ == "__main__":
    # app = Tk()
    #
    # app.title("Define Simulation Grid")
    #
    # app.geometry('350x200')
    #
    # heightLabel = Label(app, text="Height : ")
    # heightLabel.grid(column=0, row=0)
    #
    # heightEntry = Entry(app, width=15)
    # heightEntry.grid(column=1, row=0)
    #
    # widthLabel = Label(app, text="Width : ")
    # widthLabel.grid(column=0, row=1)
    #
    # widthEntry = Entry(app, width=15)
    # widthEntry.grid(column=1, row=1)
    #
    # btn = Button(app, text="Create Simulation Grid", command=createSimulationWindow)
    # btn.grid(column=0, row=2)
    #
    # app.mainloop()

    simulation = Simulation()
    simulation.set_simulation(16, 16, 15, 7, [[1,1], [3,4]], [[5,5], [5,6], [5,7]])
    i = 0
    while(True):
        simulation.print_grid()
        grid = simulation.epoch(False)
        #visaulize grid
        sleep(1)
        i += 1
        print(i)
