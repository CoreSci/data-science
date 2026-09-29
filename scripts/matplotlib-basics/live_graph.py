"""Live-updating line chart that re-reads a data file several times per second.

Problem: watch a signal while it is being produced, like a lightweight live
dashboard, without a database or web stack.

How it works: ``FuncAnimation`` calls ``animate`` every 10 ms. It re-reads
``example.txt`` (one ``x,y`` pair per line), which ``signal_generator.py``
keeps appending to, and redraws the plot.

Adapted from: sentdex, "Matplotlib tutorial series" (pythonprogramming.net),
live-graph part.

Run: start ``python signal_generator.py`` in one terminal, then
``python live_graph.py`` in another, from the same folder.
"""
from __future__ import annotations

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i: int) -> None:
    """Redraw the full contents of example.txt."""
    try:
        graph_data = open('example.txt', 'r').read()
    except FileNotFoundError:
        return  # generator not started yet
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            # bug fix: plot numbers, not strings (strings become categorical axis labels)
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_title('Live signal (example.txt)')
    ax1.set_xlabel('sample index')
    ax1.set_ylabel('amplitude')


if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=10, cache_frame_data=False)
    plt.show()
