# Animated Plots

See [matplotlib.animation](https://matplotlib.org/stable/api/animation_api.html) for more information. From [matplotlib.animation](https://matplotlib.org/stable/api/animation_api.html), PillowWriter will be used to write a matplotlib plot to a frame of a .gif. First, some imports:

```python
from matplotlib.animation import PillowWriter
from matplotlib.pyplot import plot, clf, figure, pause, xticks, yticks
from numpy import linspace, sin
from math import pi
```

Next, write a function that takes in an argument for what will be animated in the plot. In this example, a sine wave will be animated, and so the argument is the phase of the sine wave.

```python
def plot_function(a):
    f = lambda x: sin(a + x)
    x = linspace(0, 2 * pi, 100)
    plot(x, f(x))
    xticks([])
    yticks([])
```

Now, create some a values to loop over. Each iteration in the loop will be one frame in the animation.

```python
a_vals = linspace(0, 2*pi, 100)
```

To write frames to the animation, a writer object needs to defined with PillowWriter. Specify the frames per second. Additional metadata can also be specified in the PillowWriter object. Additionally, a matplotlib figure object needs to be defined. The PillowWriter object will pull frames from this figure object.

```python
fps = 30
dpi = 50
writer = PillowWriter(fps=fps)
 
fig = figure()
```

Use the "with" keyword to loop through the a values with the "saving" method of the PillowWriter object. Within this method, specify the figure object that is the target of the PillowWriter object, the file name, and the dpi of the output animation. Within the loop, use the "clf" function to clear the figure canvas between frames, and call the plot function. After the plot function is called, use the "get_frame" method of the PillowWriter object to save the plot to one frame of the animation. Additionally, use the "pause" function to preview the animation. Without the pause, the .gif will be written headlessly.

```python
with writer.saving(fig, "plot.gif", dpi):
    for a in a_vals:
        clf()
        plot_function(a)
        pause(fps/3600)
        writer.grab_frame()
```

See the result in Figure 1.

![Figure 1](plot.gif)

**Figure 1.** Animated sine wave .gif.

.gif files can be large and difficult to compress. Instead, use ffmpeg to create a video file by using FFMpegWriter. Note that ffmpeg must be installed before continuing. Additional imports need to defined.

```python
from matplotlib.animation import FFMpegWriter
from matplotlib.pyplot import plot, clf, figure, pause, xticks, yticks, rcParams
```

Tell matplotlib where to find the executable for ffmpeg by specifying the path within 'animation.ffmpeg_path' within the rcParams object.

```python
rcParams['animation.ffmpeg_path'] = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
```

Everything is done the same except change the writer object to FFMpegWriter.
github-dark 

```python
writer = FFMpegWriter(fps=fps)
```

Also, change the file name.

```python
with writer.saving(fig, "plot.mp4", dpi):
```

See the video in Figure 2.

<video controls>
  <source src="plot.mp4" type="video/mp4">
</video>

**Figure 2.** Animated sine wave .mp4.

View the code to create the [.gif](https://github.com/nibhscripta/nibhscripta.github.io/blob/main/animate-plots/animate%20gif.py) and the [.mp4](https://github.com/nibhscripta/nibhscripta.github.io/blob/main/animate-plots/animate%20mp4.py)