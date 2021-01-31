import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Parse the fixed width texts into structured numerical data.
ColSpecs = [(11, 20), (21, 30)]
stations = pd.read_fwf("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt", colspecs=ColSpecs, header=None)

# Plot the stations on a global map.
fig, ax = plt.subplots(figsize=(24,16))
earth = Basemap(ax=ax)
earth.drawcoastlines(color='#556655', linewidth=0.5)
ax.scatter(stations[1], stations[0], c='blue', alpha=0.5, zorder=1)
ax.set_xlabel("GHCN Stations")

print("--------------------")
print("Save the image into a PNG file.")
fig.savefig("/home/dning/GHCN/station_scatter.png")