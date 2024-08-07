from ast import Or
from turtle import width
import matplotlib
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from tkinter import messagebox


def genSphere(radius, xCenter,yCenter,zCenter,resolution,):
        u = np.linspace(0, 2 * np.pi, resolution)
        v = np.linspace(0, np.pi, resolution)

        u, v = np.meshgrid(u, v)

        x = radius * np.sin(v) * np.cos(u) + xCenter
        y = radius * np.sin(v) * np.sin(u) + yCenter
        z = radius * np.cos(v) + zCenter
        ax.plot_surface(x,y,z)

radiusUpperLim = 20
radiusLowerLim = 0 
plotSize = 200

def checkPlanetInputVals(radius,mass,xPos,yPos,zPos): 
    try: 
        radius = float(radius)
        if radius > radiusUpperLim or radius < radiusLowerLim:
            raise ValueError("Radius not within designated range")
        mass = float(mass)
        xPos = float(xPos)
        yPos = float(yPos)
        zPos = float(zPos)
        return True
    except ValueError as e: 
        tk.messagebox.showerror("Input Error", str(e))
        return False


resolution = 100
def plot():
    ax.clear() 
    halfPlotSize = plotSize / 2
    ax.set_xlim([-halfPlotSize, halfPlotSize])
    ax.set_ylim([-halfPlotSize, halfPlotSize])
    ax.set_zlim([-halfPlotSize, halfPlotSize])
    ax.set_box_aspect([1, 1, 1])

    if firstPlanetActive:
        radius = firstPlanetRadiusEntry.get()
        mass = firstPlanetMassEntry.get()
        xPos = firstPlanetXPositionEntry.get()
        yPos = firstPlanetYPositionEntry.get()
        zPos = firstPlanetZPositionEntry.get()

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos) == True: 
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution)

    if secondPlanetActive:
        radius = secondPlanetRadiusEntry.get()
        mass = secondPlanetMassEntry.get()
        xPos = secondPlanetXPositionEntry.get()
        yPos = secondPlanetYPositionEntry.get()
        zPos = secondPlanetZPositionEntry.get()

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos) == True: 
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution)
    
    if thirdPlanetActive:
        radius = thirdPlanetRadiusEntry.get()
        mass = thirdPlanetMassEntry.get()
        xPos = thirdPlanetXPositionEntry.get()
        yPos = thirdPlanetYPositionEntry.get()
        zPos = thirdPlanetZPositionEntry.get()

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos) == True: 
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution)
    
    canvas.draw()
    
matplotlib.use('TkAgg')
style.use("dark_background")

root = tk.Tk()
root.title("Orbital Simulator")
root.attributes('-fullscreen',True)
root.configure(background='#453C3A')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X)

inputFrame = tk.Frame(frame)
inputFrame.pack(pady=5)

firstPlanetActive = tk.IntVar()
secondPlanetActive = tk.IntVar()
thirdPlanetActive = tk.IntVar()

#region firstInputField

specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Planet 1: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

firstPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=firstPlanetActive, onvalue=1, offvalue=0)
firstPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius [{radiusLowerLim}-{radiusUpperLim}]:")
radiusLabel.pack(side=tk.LEFT, padx=5)
firstPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass:")
massLabel.pack(side=tk.LEFT, padx=5)
firstPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
firstPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
firstPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
firstPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
firstPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
firstPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
firstPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)

#endregion 
#region secondInputField
specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Planet 2: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

secondPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=secondPlanetActive, onvalue=1, offvalue=0)
secondPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius [{radiusLowerLim}-{radiusUpperLim}]:")
radiusLabel.pack(side=tk.LEFT, padx=5)
secondPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass:")
massLabel.pack(side=tk.LEFT, padx=5)
secondPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
secondPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
secondPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
secondPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
secondPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
secondPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
secondPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)
#endregion
#region thirdInputField
specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Planet 3: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

thirdPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=thirdPlanetActive, onvalue=1, offvalue=0)
thirdPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius [{radiusLowerLim}-{radiusUpperLim}]:")
radiusLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass:")
massLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
thirdPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
thirdPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=3)
thirdPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)
#endregion

runButtonFrame = tk.Frame(inputFrame)
runButtonFrame.pack(pady=5)

tk.Button(runButtonFrame, text="Generate Planets", command=plot).pack(side=tk.LEFT,padx=5)
tk.Button(runButtonFrame, text="Run Simulation",).pack(side=tk.LEFT,padx=5)


class Planet: 
    def __init__(self,planetaryRadius,mass,position): 
        self.planetaryRadius = planetaryRadius
        self.mass = mass
        self.position = position


root.mainloop()