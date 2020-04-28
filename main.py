from tkinter import *
from GUI.CellGrid import CellGrid


def createSimulationWindow():
    simulationWindow = Toplevel(app)

    grid = CellGrid(simulationWindow, int(heightEntry.get()), int(widthEntry.get()), 15)
    grid.pack()

    simulateButton = Button(simulationWindow, text="Simulate", bg='red',
                            command=createSimulationWindow)  # TODO : Change callback command to Simulate
    simulateButton.pack()


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
