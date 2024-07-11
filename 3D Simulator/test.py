from turtle import width
import matplotlib
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style

matplotlib.use('Qt5Agg')
style.use("dark_background")

root = tk.Tk()
root.title("Orbital Simulator")
root.attributes('-fullscreen',True)
root.configure(background='#453C3A')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.tight_layout()

fig2, ax2 = plt.subplots(2,1)
fig2.tight_layout()

frame = tk.Frame(root)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP)

canvas2 = FigureCanvasTkAgg(fig2, master=root,)
canvas2.get_tk_widget().pack(side=tk.TOP)

frame.pack()

class Planet: 
    def __init__(self,radius,mass,density): 
        self.radius = radius
        self.mass = mass
        self.density = density




root.mainloop()