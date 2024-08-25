from ast import Or
import math
from turtle import width
import matplotlib
import time
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from tkinter import messagebox

radiusUpperLim = 0.5
radiusLowerLim = 0 
plotSize = 10 #AU
timestep = 60*60*24*10 #10 days
resolution = 20
planets = []
paused = False # is sim paused? 
massScaleFactor = 1e23 

def genSphere(radius, xCenter,yCenter,zCenter,resolution,planet):
    radiusAU = MtoAU(radius)
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)

    u, v = np.meshgrid(u, v)

    x = radiusAU * np.sin(v) * np.cos(u) + MtoAU(xCenter)
    y = radiusAU * np.sin(v) * np.sin(u) + MtoAU(yCenter)
    z = radiusAU * np.cos(v) + MtoAU(zCenter)
    colormap = ""
    if planet.name == "Planet 1": 
        colormap = 'magma'
    elif planet.name == "Planet 2":
        colormap = 'viridis'
    else: 
        colormap = 'cividis'
    ax.plot_surface(x,y,z,cmap=colormap)

def checkPlanetInputVals(radius,mass,xPos,yPos,zPos,xVel,yVel,zVel): 
    try: 
        radius = float(radius)
        if radius > radiusUpperLim or radius < radiusLowerLim:
            raise ValueError("Radius not within designated range")
        mass = float(mass)
        xPos = float(xPos)
        yPos = float(yPos)
        zPos = float(zPos)
        xVel = float(xVel)
        yVel = float(yVel)
        zVel = float(zVel)

        return True
    except ValueError as e: 
        tk.messagebox.showerror("Input Error", str(e))
        return False

def plot():

    ax.clear() 
    halfPlotSize = MtoAU(plotSize / 2)
    ax.set_xlim([-halfPlotSize, halfPlotSize])
    ax.set_ylim([-halfPlotSize, halfPlotSize])
    ax.set_zlim([-halfPlotSize, halfPlotSize])
    ax.set_box_aspect([1, 1, 1])

    global planets
    planets = []
    
    if firstPlanetActive.get():
        #region statements
        radius = firstPlanetRadiusEntry.get()
        mass = firstPlanetMassEntry.get()
        xPos = firstPlanetXPositionEntry.get()
        yPos = firstPlanetYPositionEntry.get()
        zPos = firstPlanetZPositionEntry.get()
        xVel = firstPlanetXVelocityEntry.get()
        yVel = firstPlanetYVelocityEntry.get()
        zVel = firstPlanetZVelocityEntry.get() 
        #endregion

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos,xVel,yVel,zVel) == True: 
            velocity = [float(xVel),float(yVel),float(zVel)]
            position = [float(xPos),float(yPos),float(zPos)]
            scaledMass = float(mass)*massScaleFactor
            planets.append(Planet("Planet 1",float(radius),scaledMass,position,velocity))
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution,planets[0])

    if secondPlanetActive.get():
        #region statements
        radius = secondPlanetRadiusEntry.get()
        mass = secondPlanetMassEntry.get()
        xPos = secondPlanetXPositionEntry.get()
        yPos = secondPlanetYPositionEntry.get()
        zPos = secondPlanetZPositionEntry.get()
        xVel = secondPlanetXVelocityEntry.get()
        yVel = secondPlanetYVelocityEntry.get()
        zVel = secondPlanetZVelocityEntry.get()
        #endregion

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos,xVel,yVel,zVel) == True: 
            velocity = [float(xVel),float(yVel),float(zVel)]
            position = [float(xPos),float(yPos),float(zPos)]
            scaledMass = float(mass)*massScaleFactor
            planets.append(Planet("Planet 2",float(radius),scaledMass,position,velocity))
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution,planets[1])
    
    if thirdPlanetActive.get():
        #region statements
        radius = thirdPlanetRadiusEntry.get()
        mass = thirdPlanetMassEntry.get()
        xPos = thirdPlanetXPositionEntry.get()
        yPos = thirdPlanetYPositionEntry.get()
        zPos = thirdPlanetZPositionEntry.get()
        xVel = thirdPlanetXVelocityEntry.get()
        yVel = thirdPlanetYVelocityEntry.get()
        zVel = thirdPlanetZVelocityEntry.get()
        #endregion

        if checkPlanetInputVals(radius,mass,xPos,yPos,zPos,xVel,yVel,zVel) == True: 
            velocity = [float(xVel),float(yVel),float(zVel)]
            position = [float(xPos),float(yPos),float(zPos)]
            scaledMass = float(mass)*massScaleFactor
            planets.append(Planet("Planet 3",float(radius),scaledMass,position,velocity))
            genSphere(float(radius),float(xPos), float(yPos), float(zPos),resolution,planets[2])
    
    canvas.draw()

def PauseSimulation(): 
    global paused
    paused = not paused
    pauseButton.config(text="Resume Simulation" if paused else "Pause Simulation")
#MASS for star 100000000000000 SPEED 20000000
def RunSimulation(): 
    
    for i in range(1000):  # Run for 1000 time steps
        if paused:
            root.update_idletasks()
            root.update()
            time.sleep(0.1)
        else: 
            for planet in planets:
                totalForce = np.array([0.0,0.0,0.0])
                for otherPlanet in planets: 
                    if planet is not otherPlanet: 
                        force = planet.GravitationalForce(otherPlanet)
                        totalForce += force
                planet.updateVelocity(totalForce) 
                planet.updatePosition()
            
            ax.clear()
            halfPlotSize = MtoAU(plotSize / 2)
            ax.set_xlim([-halfPlotSize, halfPlotSize])
            ax.set_ylim([-halfPlotSize, halfPlotSize])
            ax.set_zlim([-halfPlotSize, halfPlotSize])
            ax.set_box_aspect([1, 1, 1])
            
            for planet in planets:
                planet.draw(ax)
        
            canvas.draw()
            canvas.flush_events()
            root.update_idletasks()
            root.update()  
            time.sleep(0.005)  

def AUtoM(AUVal): 
    mVal = AUVal * 149597870700
    return mVal

def MtoAU(mVal):
    AUVal = mVal/149597870700
    return AUVal

class Planet:
    def __init__(self, name, radius, mass, position, velocity):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.position = np.array(position)  # [x, y, z]
        self.velocity = np.array(velocity)  # [vx, vy, vz]
        self.history = [self.position.copy()] 

    def updatePosition(self):
        self.position += MtoAU(self.velocity * timestep)
        self.history.append(self.position.copy())

    def GravitationalForce(self,otherPlanet): 
        G = 6.67430e-11 
        r = AUtoM(self.calculateDistance(otherPlanet))
        if r == 0: 
            return np.array([0.0,0.0,0.0]) #avoids division by 0
        selfMass = float(self.mass)
        otherPlanetMass = float(otherPlanet.mass)
        forceMagnitude = (G*selfMass*otherPlanetMass)/r**2
        forceDirection = (AUtoM(otherPlanet.position) - AUtoM(self.position)) / r
        return forceMagnitude*forceDirection
    
    def updateVelocity(self,force): 
        acceleration = force/float(self.mass)
        self.velocity += acceleration * timestep

    def draw(self, ax):
        genSphere(float(self.radius), 
        float(self.position[0]), 
        float(self.position[1]), 
        float(self.position[2]), resolution, self)
        if len(self.history) > 1:
            history_array = np.array(self.history)
            history_array = MtoAU(history_array)
            ax.plot(history_array[:, 0], history_array[:, 1], history_array[:, 2], 'purple', alpha=0.5)
    
    def calculateDistance(self, otherPlanet):
        return np.linalg.norm(self.position - otherPlanet.position)

def topDown(): 
    ax.view_init(elev=90, azim=-90)
    canvas.draw()
def genPosData(): 
    with open("planet_positions.txt", "w") as file:
        for planet in planets:
            file.write(f"{planet.name}\n")
            file.write("Position History (x, y, z)\n")
            for pos in planet.history:
                file.write(f"{pos[0]}, {pos[1]}, {pos[2]}\n")
            file.write("\n")  
    tk.messagebox.showinfo("File Created", "Position data has been saved to planet_positions.txt")


#region tkinterConfig
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
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
toolbar.pack(side=tk.TOP, fill=tk.X)

frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X, before=canvas.get_tk_widget())

inputFrame = tk.Frame(frame)
inputFrame.pack(pady=5)

firstPlanetActive = tk.IntVar()
secondPlanetActive = tk.IntVar()
thirdPlanetActive = tk.IntVar()
#endregion
#region firstInputField

specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Body 1: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

firstPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=firstPlanetActive, onvalue=1, offvalue=0)
firstPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius [{radiusLowerLim}-{radiusUpperLim}]AU:")
radiusLabel.pack(side=tk.LEFT, padx=5)
firstPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass (10^23):")
massLabel.pack(side=tk.LEFT, padx=5)
firstPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
firstPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
firstPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
firstPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)

velocityLabel = tk.Label(specificPlanetInputFrame, text="Initial Velocity [vx,vy,vz]:")
velocityLabel.pack(side=tk.LEFT, padx=5)
firstPlanetXVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetXVelocityEntry.pack(side=tk.LEFT, padx=5)
firstPlanetYVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetYVelocityEntry.pack(side=tk.LEFT, padx=5)
firstPlanetZVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
firstPlanetZVelocityEntry.pack(side=tk.LEFT, padx=5)

#endregion 
#region secondInputField

specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Body 2: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

secondPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=secondPlanetActive, onvalue=1, offvalue=0)
secondPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius[{radiusLowerLim}-{radiusUpperLim}]AU:")
radiusLabel.pack(side=tk.LEFT, padx=5)
secondPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass (10^23):")
massLabel.pack(side=tk.LEFT, padx=5)
secondPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
secondPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
secondPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
secondPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)

velocityLabel = tk.Label(specificPlanetInputFrame, text="Initial Velocity [vx,vy,vz]:")
velocityLabel.pack(side=tk.LEFT, padx=5)
secondPlanetXVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetXVelocityEntry.pack(side=tk.LEFT, padx=5)
secondPlanetYVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetYVelocityEntry.pack(side=tk.LEFT, padx=5)
secondPlanetZVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
secondPlanetZVelocityEntry.pack(side=tk.LEFT, padx=5)

#endregion
#region thirdInputField
specificPlanetInputFrame = tk.Frame(inputFrame)
specificPlanetInputFrame.pack(padx=5)

planetNameLabel = tk.Label(specificPlanetInputFrame,text="Body 3: ")
planetNameLabel.pack(side=tk.LEFT,padx=5)

thirdPlanetActivationCheckbox = tk.Checkbutton(specificPlanetInputFrame, variable=thirdPlanetActive, onvalue=1, offvalue=0)
thirdPlanetActivationCheckbox.pack(side=tk.LEFT,padx=3)

radiusLabel = tk.Label(specificPlanetInputFrame, text=f"Radius[{radiusLowerLim}-{radiusUpperLim}]AU:")
radiusLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetRadiusEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetRadiusEntry.pack(side=tk.LEFT, padx=5)
    
massLabel = tk.Label(specificPlanetInputFrame, text="Mass (10^23):")
massLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetMassEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetMassEntry.pack(side=tk.LEFT, padx=5)

positionLabel = tk.Label(specificPlanetInputFrame, text="Position [x,y,z]:")
positionLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetXPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetXPositionEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetYPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetYPositionEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetZPositionEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetZPositionEntry.pack(side=tk.LEFT, padx=5)

velocityLabel = tk.Label(specificPlanetInputFrame, text="Initial Velocity [vx,vy,vz]:")
velocityLabel.pack(side=tk.LEFT, padx=5)
thirdPlanetXVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetXVelocityEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetYVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetYVelocityEntry.pack(side=tk.LEFT, padx=5)
thirdPlanetZVelocityEntry = tk.Entry(specificPlanetInputFrame, width=5)
thirdPlanetZVelocityEntry.pack(side=tk.LEFT, padx=5)
#endregion

runButtonFrame = tk.Frame(inputFrame)
runButtonFrame.pack(pady=5)

tk.Button(runButtonFrame, text="Generate Planets", command=plot).pack(side=tk.LEFT,padx=5)
tk.Button(runButtonFrame, text="Run Simulation",command=RunSimulation).pack(side=tk.LEFT,padx=5)
pauseButton = tk.Button(runButtonFrame, text="Pause Simulation",command=PauseSimulation)
pauseButton.pack(side=tk.LEFT,padx=5)
tk.Button(runButtonFrame, text="2D View",command=topDown).pack(side=tk.LEFT,padx=5)
tk.Button(runButtonFrame, text="Generate Position File", command=genPosData).pack(side=tk.LEFT,padx=5)

root.mainloop()