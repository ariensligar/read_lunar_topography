import imageio
import pyvista as pv
from PIL import Image
import numpy as np

Image.MAX_IMAGE_PIXELS = 363894400

def read_jpg2000(file_path):
    image = imageio.v3.imread(file_path)
    return image

def convert_to_stl(image_data, output_file,start_x=0,stop_x=100,start_y=0,stop_y=0):
    # Create a uniform grid from the image data


    shape= image_data.shape
    x_step = (stop_x-start_x)/shape[0]
    y_step = (stop_y - start_y) / shape[1]
    x_range = np.linspace(start_x,stop_x,num=shape[0])
    y_range = np.linspace(start_y, stop_y, num=shape[1])
    xx,yy= np.meshgrid(x_range,y_range)
    z = np.ravel(image_data)
    x = np.ravel(xx)
    y = np.ravel(yy)
    xyz = np.stack((x, y, z)).T
    grid = pv.PolyData(xyz)
    grid.delaunay_2d(inplace=True)
    #grid["elevation"] = image_data.flatten(order="F")  # Flatten image data and add as point array

    # Save the grid as an STL file
    grid.plot()
    # grid.save(output_file)

# Usage
file_path = 'example_data/SLDEM2015_512_30N_60N_180_225.JP2'
output_file = 'output.stl'

# ds = rasterio.open(file_path)
# ds.read(1)
#
image_data = read_jpg2000(file_path)
convert_to_stl(image_data, output_file)
