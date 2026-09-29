"""Matplotlib chart-type reference: line, bar, histogram, scatter and plot-from-file.

Problem: a quick, runnable cheat sheet for the five basic chart types, each
with a title, axis labels and a legend.

How it works: each function draws one figure. ``main()`` renders them all and
saves them as PNGs in ``output/``, or shows them when a display is available.

Data: small inline lists, plus ``sample_xy.txt`` (comma-separated x,y integers).

Adapted from: sentdex, "Matplotlib tutorial series" (pythonprogramming.net),
basic chart parts. (The tutorial's stock-price chart lives in
``finance-2016/stock_price_chart.py``.)

Run: ``python matplotlib_chart_types.py``
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def line_chart() -> None:
    """Two labelled lines on one axis."""
    x = [1, 2, 3]
    y = [5, 7, 4]
    x2 = [1, 2, 3]
    y2 = [10, 14, 12]
    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')
    plt.xlabel('Plot Number')
    plt.ylabel('Value')
    plt.title('Line chart: two series')
    plt.legend()


def bar_chart() -> None:
    """Two interleaved bar series in different colours."""
    plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example one")
    plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example two", color='g')
    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.title('Bar chart: interleaved series')


def histogram() -> None:
    """Distribution of ages over fixed-width bins."""
    population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111,
                       115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
    plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='ages')
    plt.xlabel('age')
    plt.ylabel('count')
    plt.title('Histogram: age distribution')
    plt.legend()


def scatter_plot() -> None:
    """Scatter plot with a custom marker."""
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]
    plt.scatter(x, y, label='points', color='k', s=25, marker="o")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter plot')
    plt.legend()


def plot_from_file(path: Path = HERE / "sample_xy.txt") -> None:
    """Line chart of x,y integer pairs read from a CSV-style text file."""
    x = []
    y = []
    with open(path, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if len(row) == 2:
                x.append(int(row[0]))
                y.append(int(row[1]))
    plt.plot(x, y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Plot from file: {path.name}')
    plt.legend()


def main() -> None:
    out = HERE / "output"
    headless = plt.get_backend().lower() == "agg"
    for fn in (line_chart, bar_chart, histogram, scatter_plot, plot_from_file):
        plt.figure()
        fn()
        if headless:
            out.mkdir(exist_ok=True)
            plt.savefig(out / f"{fn.__name__}.png", dpi=100, bbox_inches="tight")
            plt.close()
        else:
            plt.show()
    if headless:
        print(f"saved 5 charts to {out}")


if __name__ == "__main__":
    main()
