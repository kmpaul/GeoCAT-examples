"""
NCL_dataonmap_10_lg.py
======================
This script illustrates the following concepts:
    - Plotting WRF data on native grid
    - Plotting data using wrf python functions
    - Overlaying continent outlines on a map
    - Following best practices when choosing a colormap.
      More information on colormap best practices can be found `here <https://geocat-examples.readthedocs.io/en/latest/gallery/Colors/CB_Temperature.html#sphx-glr-gallery-colors-cb-temperature-py>`_.
    
See following URLs to see the reproduced NCL plot & script:
    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/dataonmap_10.ncl
    - Original NCL plot: https://www.ncl.ucar.edu/Applications/Images/dataonmap_10_1_lg.png
"""

###############################################################################
# Import packages

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from wrf import (getvar, to_np, latlon_coords, get_cartopy)

import geocat.datafiles as gdf
from geocat.viz import util as gvutil

###############################################################################
# Read in the data

wrfin = Dataset(gdf.get("netcdf_files/wrfout_d01_2003-07-15_00_00_00"), decode_times=True)

q2 = getvar(wrfin, "Q2")

###############################################################################
# Plot the data

lats, lons = latlon_coords(q2)

# The `get_cartopy` wrf function will automatically find and use the 
# intended map projection for this dataset 
fig = plt.figure(figsize=(10,10))
cart_proj = get_cartopy(q2)
ax = plt.axes(projection=cart_proj)

# Add features to the map
ax.add_feature(cfeature.LAND, facecolor="", edgecolor="k", zorder=1)

# Add filled contours
plt.contourf(to_np(lons),
             to_np(lats),
             q2,
             levels=np.linspace(0.01125, 0.05, 32), cmap="magma",
             transform=ccrs.PlateCarree(),
             vmin=0,
             vmax=0.05)

# Add a colorbar
cbar = plt.colorbar(ax=ax,
                    orientation="vertical",
                    ticks=np.arange(0.0125, 0.0476, 0.0025),
                    drawedges=True,
                    extendrect=True,
                    shrink=0.7)
                    

# Format colorbar ticks and labels 
cbar.ax.tick_params(size=0, labelsize=10)

# Draw gridlines
gl = ax.gridlines(crs=ccrs.PlateCarree(),
                  draw_labels=True,
                  dms=False,
                  x_inline=False,
                  y_inline=False,
                  linewidth=1,
                  color="k",
                  alpha=0.25)

# Manipulate latitude and longitude gridline numbers and spacing
gl.top_labels = False
gl.right_labels = False
gl.xlocator = mticker.FixedLocator(np.arange(-105, -80, 5))
gl.ylocator = mticker.FixedLocator(np.arange(18,35,2))
gl.xlabel_style = {"rotation": 0, "size": 15}
gl.ylabel_style = {"rotation": 0, "size": 15}
gl.xlines = False
gl.ylines = False

# Add titles to the plot
gvutil.set_titles_and_labels(ax,
                             maintitle="WRF data on native grid",
                             lefttitle="QV at 2 M",
                             maintitlefontsize= 16,
                             lefttitlefontsize=14)

plt.show()