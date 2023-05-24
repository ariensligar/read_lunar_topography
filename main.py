'''

This uses a modified library, it was out of date and didn't work with python3
https://pdsimage.readthedocs.io/en/master/PDS_Extractor.html

'''

import os
import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv
from pdsimage_mod.PDS_Extractor import BinaryTable

# what/where to extract
radius_to_extract_km = 200
center_lat = -60
center_long = 120
ldem = BinaryTable('ldem_16')


boundary = ldem.lambert_window(radius_to_extract_km,center_lat,center_long) #100km area extracted
X, Y, Z = ldem.extract_grid(*boundary)
plt.imshow(Z)
plt.show()

z = np.array(Z).T
# Not sure about X and Y values here, might need to use actual lat/lon conversion to get absolute value
x = np.linspace(-radius_to_extract_km*1e3,radius_to_extract_km*1e3,num=z.shape[1])
y = np.linspace(-radius_to_extract_km*1e3,radius_to_extract_km*1e3,num=z.shape[0])

xx, yy = np.meshgrid(x, y)


# test = pv.PolyData(xyz)
# test.delaunay_2d(inplace=True)
grid = pv.StructuredGrid(xx,yy,z)
grid['elev'] = z.ravel(order='f')

grid.plot(show_axes=True,show_grid=True)
out = grid.extract_geometry()
out.save("out.stl")

