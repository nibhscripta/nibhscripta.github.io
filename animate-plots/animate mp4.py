from matplotlib.animation import FFMpegWriter
from matplotlib.pyplot import plot, clf, figure, pause, xticks, yticks, rcParams
from numpy import linspace, sin
from math import pi

rcParams['animation.ffmpeg_path'] = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"

def plot_function(a):
    f = lambda x: sin(a + x)
    x = linspace(0, 2 * pi, 100)
    plot(x, f(x))
    xticks([])
    yticks([])

a_vals = linspace(0, 2*pi, 100)

fps = 30
dpi = 50
writer = FFMpegWriter(fps=fps)

fig = figure()

with writer.saving(fig, "plot.mp4", dpi):
    for a in a_vals:
        clf()
        plot_function(a)
        pause(fps/3600)
        writer.grab_frame()