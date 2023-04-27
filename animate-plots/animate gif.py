from matplotlib.animation import PillowWriter
from matplotlib.pyplot import plot, clf, figure, pause, xticks, yticks
from numpy import linspace, sin
from math import pi

def plot_function(a):
    f = lambda x: sin(a + x)
    x = linspace(0, 2 * pi, 100)
    plot(x, f(x))
    xticks([])
    yticks([])

a_vals = linspace(0, 2*pi, 100)

fps = 30
dpi = 50
writer = PillowWriter(fps=fps)

fig = figure()

with writer.saving(fig, "plot.gif", dpi):
    for a in a_vals:
        clf()
        plot_function(a)
        pause(fps/3600)
        writer.grab_frame()