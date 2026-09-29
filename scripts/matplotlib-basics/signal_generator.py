"""Stream a synthetic sampled sine wave into ``example.txt`` for ``live_graph.py``.

Problem: the live graph needs a data source that changes in real time.

How it works: for each of ``PERIODS`` sweeps, appends ``i,sin(2*pi*f*i/fs)``
lines (i = 0, 5, ..., 995) every 30 ms, then clears the file and starts again.
With f = 500 Hz sampled at fs = 800 Hz, the signal is deliberately undersampled,
so the plot shows an aliasing pattern instead of a clean 500 Hz sine.

Run: ``python signal_generator.py`` (about 6 s per sweep, 10 sweeps).
"""
from __future__ import annotations

import time
from math import pi, sin

DATA_FILE = 'example.txt'
PERIODS = 10          # number of sweeps
SIGNAL_FREQ = 500     # Hz
SAMPLE_RATE = 800     # Hz
STEP = 5              # index increment per sample
DELAY_S = 0.030       # pause between samples


def reset_file() -> None:
    """Truncate the data file."""
    open(DATA_FILE, 'w').close()


def main() -> None:
    reset_file()
    for k in range(PERIODS):
        i = 0
        j = 0.0
        while i < 1000:
            with open(DATA_FILE, 'a') as f:
                f.write(f"{i},{j}\n")
            i = i + STEP
            j = sin(2 * pi * SIGNAL_FREQ * i / SAMPLE_RATE)
            time.sleep(DELAY_S)

        print("PERIOD : ", k)
        reset_file()


if __name__ == "__main__":
    main()
