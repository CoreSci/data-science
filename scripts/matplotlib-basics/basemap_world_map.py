"""Draw a world coastline map in the Miller cylindrical projection with Basemap.

Problem: a minimal starting point for plotting geographic data on a map.

Adapted from: sentdex, "Basemap geographic plotting" tutorial (pythonprogramming.net).

Note: Basemap is in maintenance mode. For new work, Cartopy is the maintained successor.

Run: ``python basemap_world_map.py`` (``pip install basemap``). Saves
``world_map.png`` when no display is available.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

if __name__ == "__main__":
    m = Basemap(projection='mill')
    m.drawcoastlines()
    plt.title('World coastlines (Miller projection)')
    if plt.get_backend().lower() == "agg":
        plt.savefig('world_map.png', dpi=100, bbox_inches='tight')
    else:
        plt.show()
